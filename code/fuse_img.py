# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:27:20 2021

@author: hp
"""
import cv2 
import os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

import time
#  Opencv doesn't support image paths which contain unicode characters
path = "D:\\LYIT\\repository\\yolo\\labelled_digit\\MR-AMR Dataset\\v1\\0\\"
#path = 'D:\\LYIT\\repository\\images\\poor_quality\\good\\'
#Read the two images

# Standard imports
import cv2
import numpy as np 

# Read images


# Read images : obj image will be cloned into im

# Standard imports
import cv2
import numpy as np 

# Read images
src = cv2.imread(path + "2.jpg")
dst = cv2.imread(path + "x.jpg")
# Create a rough mask around the airplane.
src_mask = np.zeros(src.shape, src.dtype)
poly = np.array([ [4,80], [30,54], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))

# This is where the CENTER of the airplane will be placed
center = (150,10)

# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)

# Save result
cv2.imwrite(path + "result.jpg", output);

################################################

# Read images : src image will be cloned into dst

obj = cv2.imread(path + "x.jpg")
im = cv2.imread(path + "x.jpg")
# Create an all white mask
mask = 255 * np.ones(obj.shape, obj.dtype)

# The location of the center of the src in the dst
width, height, channels = im.shape
center = (height/2, width/2)

# Seamlessly clone src into dst and put the results in output
normal_clone = cv2.seamlessClone(obj, im, mask, center, cv2.NORMAL_CLONE)
mixed_clone = cv2.seamlessClone(obj, im, mask, center, cv2.MIXED_CLONE)

# Write results
cv2.imwrite(path + "result2.jpg", normal_clone)
cv2.imwrite(path + "result3.jpg", mixed_clone)