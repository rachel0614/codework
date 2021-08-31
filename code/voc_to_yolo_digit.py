import os
import xml.etree.ElementTree as ET
import cv2
import argparse
from tqdm import tqdm
 
# 根据已有的VOC2007标注格式生成YOLO格式到ResultLabels目录
# 如果图片不存在会报错
# 一个图例只有一个标注
def xml_to_txt(xml_dir,img_dir,out_dir):
    if not os.path.exists(out_dir):  # 如果输出路径不存在，创建输出路径
        os.makedirs(out_dir)
    #print("\n read xml..." + xml_dir)

    annotations = os.listdir(xml_dir)  # 获取指定文件夹的文件列表
    #tqdm是用来显示进度条的，可以改成你原来那样子就不会有进度条了
    for i, file in tqdm(enumerate(annotations),desc='已经处理了',total=len(annotations),unit='xml_file'):
        txt_name = file.split('.')[0] + '.txt'#txt的文件名
        txt_pos = out_dir + '/' + txt_name#txt文件带路径的文件名
        
        print(txt_pos + '\n' + txt_pos)

    
        with open(txt_pos,mode='w') as f_txt:#f_txt是用于txt文件读写的文件对象
            with open(xml_dir+'/'+file,encoding='utf-8') as f_xml:#f_xml是用于xml文件读写的文件对象
                tree = ET.parse(f_xml)
                root = tree.getroot()
                img_src = img_dir + str(root.find('filename').text)
                print("\n filename = " + img_src)
                     
                
                for obj in root.iter('object'):
                    #src = cv2.imread(str(root.find('path').text))
                    src = cv2.imread(img_src)
                    #src = cv2.imread(img_dir+'/img{:0>5d}.jpg'.format(i+1))
                    
                    width=src.shape[1]
                    height=src.shape[0]
 
                    xmlbox=obj.find('bndbox')
                    #获取对应的bndbox中的对应的坐标值文本并转为int型
                    x_max=int(xmlbox.find('xmax').text)
                    x_min=int(xmlbox.find('xmin').text)
                    y_max=int(xmlbox.find('ymax').text)
                    y_min=int(xmlbox.find('ymin').text)
                    #计算对应的x y w h
                    x = ((x_min + x_max) / 2.0)*(1.0/width)
                    y = ((y_min + y_max) / 2.0)*(1.0/height)
                    w = (x_max-x_min)*(1.0/width)
                    h = (y_max-y_min)*(1.0/height)
 
                    f_txt.write('0' + ' ')
                    f_txt.write(str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + ' ')
                    f_txt.write('\n')
 
 
if __name__ == '__main__':
 #   parser = argparse.ArgumentParser()
 #   parser.add_argument('--xml_dir', type=str, default='Annotations', help='xml文件所在目录')
 #   parser.add_argument('--img_dir', type=str, default='JPEGImages', help='图片文件所在目录')
 #   parser.add_argument('--out_dir', type=str, default='resultLabels', help='输出文件夹')
 #   opt = parser.parse_args()
    #base_dir = "D:/LYIT/DissertaionWorkshop/dissertation-image-reading/dataset/MeterDataset/Gas-Meter-Counter/"
    base_dir = 'D:/LYIT/dissertation/repository/yolo训练/labelled_digit'
    xml_dir = base_dir
    img_dir = base_dir
    out_dir = 'D:/LYIT/dissertation/repository/yolo训练/labelled_digit/label_result'
    xml_to_txt(xml_dir,img_dir,out_dir)