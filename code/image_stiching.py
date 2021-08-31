# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:45:31 2021

@author: hp
"""

from Stitcher import Stitcher
import cv2
base_path = 'D:/LYIT/repository/yolo/labelled_digit/MR-AMR Dataset/v1/0/'
# 读取拼接图片
imageA = cv2.imread("01283_882.jpg")
imageB = cv2.imread("01348_043.jpg")

# 把图片拼接成全景图
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# 显示所有图片
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()