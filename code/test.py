# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:40:56 2021

@author: Administrator
"""

from PIL import Image
import pytesseract
import cv2
import os

preprocess = 'blur' #thresh

image = cv2.imread('F:\\Program Files\\Tesseract-OCR\\testing\\x.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

if preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)
    
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
    
text = pytesseract.image_to_string(Image.open(filename))
print(text)
os.remove(filename)
  
