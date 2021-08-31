# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:23:42 2021

@author: Administrator
"""
import cv2 # 彩色转黑白
img = cv2.imread('C:/Users/Administrator/Downloads/ArteMeter/40.jpg',0)


Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 先要转换为灰度图片
ret, thresh = cv2.threshold(Grayimg, 150, 255,cv2.THRESH_BINARY) # 这里的第二个参数要调，是阈值！！

#cv2.imwrite('33.png', thresh)     
cv2.imshow(thresh)
