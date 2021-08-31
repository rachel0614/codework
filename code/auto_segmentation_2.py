# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 17:33:34 2021

@author: hp
"""


import numpy as np
import argparse
import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import cv2 
from scipy.ndimage import interpolation as inter
base_dir = 'D:/LYIT/repository/yolo/labelled_digit/MR-AMR Dataset/v1_mix/0/'
name = '24.jpg'
image=cv2.imread(base_dir + name)

grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grayimage,(5,5),0)
cv2.imshow("Image", image)
ret, im_th = cv2.threshold(grayimage, 90, 255, cv2.THRESH_BINARY_INV)
#edged = cv2.Canny(blurred, 30, 150)
#cv2.imshow("Edges", edged)
(_, cnts, _) = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


print(len(cnts))

cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key =lambda x: x[1])
for (c, _) in cnts:
	(x, y, w, h) = cv2.boundingRect(c)
	if w >= 6 and h >= 20:
		cv2.rectangle(image, (x-6, y-6), (x + w+6, y + h+6),(0, 255, 0), 1)
cv2.imshow("image", image)
#plt.imshow(image, cmap='gray')
plt.savefig(base_dir +'erosin.png')
#cv2.waitKey(0)