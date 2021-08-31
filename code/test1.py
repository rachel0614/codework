# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:23:39 2021

@author: Administrator
"""

import pytesseract
import cv2

img_path = "C:/Users/Administrator/Downloads/exp17/crops/ArteMeter/3.jpg"

# 下面一行代码很重要
tessdata_dir_config = '--tessdata-dir "F:/Program Files/Tesseract-OCR/tessdata"'

im = cv2.imread(img_path)
img = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(img,lang= 'eng',config= tessdata_dir_config,)
print("result...........")
print(text)

