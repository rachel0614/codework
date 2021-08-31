# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 00:55:31 2021

@author: Administrator
"""
# five digits with 5 classses
import PIL.Image as Image
import os, random, shutil
import uuid
from string import Template
import numpy as np
from random import randrange


BASE_PATH = 'D:/LYIT/repository/yolo/labelled_digit/'
IMAGES_PATH = 'D:\\LYIT\\repository\\yolo\\labelled_digit\\MR-AMR Dataset\\v1_011\\'  # 图片集地址
SELECTION_COUNT  = 8 #select number of images from each folder
IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
IMAGE_SIZE = 45  # 每张小图片的大小
IMAGE_ROW = 1  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 1 #5  # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = 'D:\\LYIT\\repository\\yolo\\labelled_digit\\tmp9\\'  # 图片转换后的地址
TEMPLATE_PATH = "D:\\LYIT\\repository\\yolo\\labelled_digit\\template\\template9.xml"

# 获取图片集地址下的所有图片名称
#print(randrange(10))

# select IMAGE_COLUMN digit numbers from 0 - 9
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_images(n):
    #selected_digits = digits #random.sample(digits, IMAGE_COLUMN)
    image_names = [''] * SELECTION_COUNT
    current_dir = ''
    idx = 0
    # class folder
    current_dir = IMAGES_PATH + str(n)
    g = os.walk(current_dir)
    for path,dir_list,file_list in g:  
        for file_name in file_list:  
            filefullname = os.path.join(path, file_name)
            image_names[idx] = filefullname
            if idx == SELECTION_COUNT - 1:
                break
            idx += 1
    return image_names    
# generate label file 


def image_label(n, img_file):
    tags = {
        'd': n,
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
# 定义图像拼接函数
def image_compose(n):
    image_names = get_images(n)
    print(image_names)
    print('load from ',n)
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for file_name in image_names:
        to_image = Image.new('RGB', (IMAGE_SIZE, IMAGE_SIZE)) #创建一个新图
        save_file_name =  "".join(str(n)) + "_" + str(uuid.uuid4().hex)[:3]
        from_image = Image.open(file_name).resize(
            (IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
        to_image.paste(from_image)
        to_image.save(IMAGE_SAVE_PATH + save_file_name + ".jpg")
        image_label(n, save_file_name)
        #print(IMAGE_SAVE_PATH + save_file_name)
    return to_image.save(IMAGE_SAVE_PATH + save_file_name + ".jpg") # 保存新图
for n in digits:
    image_compose(n) #调用函数