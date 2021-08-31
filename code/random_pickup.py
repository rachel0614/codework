# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 21:47:19 2021

@author: hp
"""

import PIL.Image as Image
import os, random, shutil
import uuid
from string import Template
import numpy as np
from random import randrange

IMAGES_PATH = 'D:\\LYIT\\repository\\dataset\\OriginalMeterDataset\\100counters\\ArteMeter\\'
TARGET_PATH = 'D:\\LYIT\\repository\\dataset\\OriginalMeterDataset\\label\\'
image_names = [''] * 10
for idx in range(0,10):
 current_dir = IMAGES_PATH
 filename = random.choice(os.listdir(current_dir))
 #print(IMAGES_PATH  + str(idx) + "\\" + filename)
 image_names[idx] = current_dir + filename
 shutil.copy(image_names[idx], TARGET_PATH + filename)
print(image_names)

