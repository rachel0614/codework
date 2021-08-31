# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:08:01 2021

@author: Administrator
"""

import cv2
import argparse
import glob
from skimage.io import imread_collection

base_path = 'D:/LYIT/repository/yolo/labelled_meter/clear/sample/*.jpg'
base_path = 'D:/LYIT/repository/runs/counter140/unclear/*.jpg'

#creating a collection with the available images
def blur_detection(threshold, image):
    print(".....................................")
    n = 0
    #ap = argparse.ArgumentParser()
    #ap.add_argument('-i', '--images', required=True,)
    #ap.add_argument('-t', '--threshold', type=float)
    #args = vars(ap.parse_args())
    #images = [cv2.imread(file) for file in glob.glob(base_path)]
    images = imread_collection(base_path)
    for image in images:
    #for img in glob.glob(base_path):
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     fm = cv2.Laplacian(gray, cv2.CV_64F).var()
     text = "Not Blurry"
     #print(images.files[n])
     print(images.files[n],'\t',fm)
     n += 1
# =============================================================================
#      if fm < args["threshold"] : #
#        text = "Blurry"
#        cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
#     		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
#        cv2.imshow("Image", image)
#        cv2.waitKey(0)
# =============================================================================

   # args = {"threshold": 30, "images": "D:\\LYIT\\dissertation\\poor_quality\\00883201372517_0.jpg"}
    
    #print(args["images"])
blur_detection(0.5, base_path  )