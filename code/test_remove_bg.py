# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 14:24:30 2021

@author: Administrator
"""

import cv2
import numpy as np

def method_1(img_src):
    # 灰度处理
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    ret, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    #127 是最小值。低于此值的会被认为是背景而剔除
    return img_bin

def method_2(img_src):
    blocksize = 3
    C = -5
    # 灰度处理
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    img_bin = cv2.adaptiveThreshold(img_gray, 127, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize, C)
    return img_bin

#读取图片
img_src = cv2.imread("C:/Users/Administrator/Downloads/exp17/crops/ArteMeter/26.jpg")
img_src = cv2.imread("C:/Users/Administrator/Downloads/exp17/crops/ArteMeter/43.jpg")

img_bin = method_1(img_src)
# 3.连通域分析
contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 不同版本返回的个数不同。有2个的，也有3个的。
# 制作掩膜
img_mask = np.zeros(img_src.shape, np.uint8)
cv2.drawContours(img_mask, contours, -1, (255, 255, 255), -1)
#位与运算
img_result = cv2.bitwise_and(img_src, img_mask)

#显示结果
cv2.imshow('1:src', img_src)
cv2.imshow("2:mask", img_mask)
cv2.imshow("3:result", img_result)

cv2.waitKey()
cv2.destroyAllWindows()