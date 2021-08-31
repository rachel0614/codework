# create 99 samples
import PIL.Image as Image
import os, random, shutil
import uuid
from string import Template
import numpy as np
from random import randrange
base = 'D:\\LYIT\\repository\\yolo\\'

# synthetic 2-digit samples 20210720
IMAGES_PATH = base + '\\labelled_digit\\MR-AMR Dataset\\v1_latest\\'  # 图片集地址
IMAGES_FORMAT = ['.jpg', '.JPG', 'png']  # 图片格式
IMAGE_SIZE = 45  # 每张小图片的大小
IMAGE_ROW = 2  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 2  # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = base + 'labelled_digit\\tmp99\\'  # 图片转换后的地址
TEMPLATE_PATH = base + "labelled_digit\\template\\template99.xml"
#print(randrange(10))

# select IMAGE_COLUMN digit numbers from 0 - 9
#digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#digits = ['0', '1']
def get_images(num1, num2,num3,num4):
    #selected_digits = random.sample(digits, IMAGE_COLUMN)
    selected_digits = [num1, num2, num3, num4]
    current_dir = ""
    image_names = [''] * IMAGE_COLUMN * IMAGE_ROW
    for idx in range(0,4):
        current_dir = IMAGES_PATH + str(selected_digits[idx]) + "\\"
        filename = random.choice(os.listdir(current_dir))
        print(IMAGES_PATH  + str(idx) + "\\" + filename)
        image_names[idx] = current_dir + filename
    return selected_digits, image_names    
# generate label file 


def image_label(selected_digits, img_file):
    tags = {
        'd1': str(selected_digits[0]) ,
        'd2' : str(selected_digits[1]),
		'd3' : str(selected_digits[2]),
		'd4' : str(selected_digits[3]),
        'file_name':img_file + ".jpg",
        'full_file_name':IMAGE_SAVE_PATH + img_file + ".jpg"
    }
    with open(TEMPLATE_PATH, 'r' , encoding='utf-8') as f:
        src = Template(f.read())
        result = src.substitute(tags)
        #print(result)
    xml_file = IMAGE_SAVE_PATH + img_file + ".xml"
    with open(xml_file, "w", encoding = 'utf-8') as f:
        print(result, file = f)
    return True 
# 简单的对于参数的设定和实际图片集的大小进行数量判断
#if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
#    raise ValueError("合成图片的参数和要求的数量不能匹配！" + str(len(image_names)))


def image_compose(num1, num2,num3, num4):
    selected_digits, image_names = get_images(num1, num2,num3,num4)
	
    image_names.append(image_names.copy())
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE)) #创建一个新图
    save_file_name =  uuid.uuid4().hex
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    suffix = str(uuid.uuid4().hex)[-4: ]
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            file_name = image_names[IMAGE_COLUMN * (y - 1) + x - 1]
            from_image = Image.open(file_name).resize(
                (IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
            image_label(selected_digits, str(num1) + str(num2) + str(num3) + str(num4) + '_' + suffix)

   
    #c_folder = IMAGE_SAVE_PATH + str(num1) + str(num2) + '\\'
    c_folder = IMAGE_SAVE_PATH 
    if not os.path.isdir(c_folder):
      os.makedirs(c_folder)
    return to_image.save( c_folder + str(num1) + str(num2)+ str(num3) + str(num4) + '_' + suffix + ".jpg") # 保存新图
for n in range(0,10):
 for x in range(0,10):
  for y in range(0,10):
   print(x , ",", y)
   image_compose(x,x,y,y)
   image_compose(x,y,x,y)
   image_compose(x,y,y,x)
   image_compose(y,x,x,y)
      