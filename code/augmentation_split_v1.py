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
IMAGES_PATH = BASE_PATH + 'MR-AMR Dataset/v1/'  # 图片集地址
SELECTION_COUNT  = 8 #select number of images from each folder
IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
IMAGE_SIZE = 45  # 每张小图片的大小
IMAGE_ROW = 1  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 1 #5  # 图片间隔，也就是合并成一张图后，一共有几列

# 获取图片集地址下的所有图片名称
#print(randrange(10))

# select IMAGE_COLUMN digit numbers from 0 - 9
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

def get_images(n):
    #selected_digits = digits #random.sample(digits, IMAGE_COLUMN)
    image_names = [] #[''] * SELECTION_COUNT
    current_dir = ''
    idx = 0
    # class folder
    current_dir = IMAGES_PATH + str(n)
    print('current_dir=',current_dir)
    g = os.walk(current_dir)
    for path,dir_list,file_list in g:
        for file_name in file_list:  
            if file_name.endswith(('.jpg', '.png')):
                filefullname = os.path.join(path, file_name)
                image_names.append(filefullname)
    np.random.shuffle(image_names)
    return image_names

for n in digits:
    images = get_images(n) #调用函数
    pos = int(len(images)/2)
    list1 = images[0:pos]
    list2 = images[pos:]
    #print('total=',len(images),'len1=',len(list1),'...list2=',len(list2),',pos=', pos)
    for file_name in list1 :
        shutil.copy2(file_name, file_name.replace('v1','v1_0'))
    for file_name in list2 :
        shutil.copy2(file_name, file_name.replace('v1','v1_1'))     
# =============================================================================
#     shuffle_images = random.shuffle(images)
#     print('shuffle',shuffle_images)
#     pos = len(shuffle_images)
#     print(len,'.....',pos)
#     list1 = images[0::pos]
#     list2 = images[pos:]
#     print(list1)
#     print(list2)
# =============================================================================
# =============================================================================
