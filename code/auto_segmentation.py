# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 16:33:46 2021

@author: hp
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import cv2 
from scipy.ndimage import interpolation as inter

base_dir = 'D:/LYIT/repository/yolo/labelled_digit/MR-AMR Dataset/v1_mix/0/'

input_file = base_dir + 'erosin.png'
img = im.open(input_file)
# convert to binary
wd, ht = img.size
pix = np.array(img.convert('1').getdata(), np.uint8)
bin_img = 1 - (pix.reshape((ht, wd)) / 255.0)
plt.imshow(bin_img, cmap='gray')
plt.savefig(base_dir +'binary.png')
def find_score(arr, angle):
    data = inter.rotate(arr, angle, reshape=False, order=0)
    hist = np.sum(data, axis=1)
    score = np.sum((hist[1:] - hist[:-1]) ** 2)
    return hist, score
delta = 1
limit = 5
angles = np.arange(-limit, limit+delta, delta)
scores = []
for angle in angles:
    hist, score = find_score(bin_img, angle)
    scores.append(score)
best_score = max(scores)
best_angle = angles[scores.index(best_score)]
#print('Best angle: {}'.formate(best_angle))
# correct skew
data = inter.rotate(bin_img, best_angle, reshape=False, order=0)
img = im.fromarray((255 * data).astype("uint8")).convert("RGB")
img.save(base_dir + 'skew_corrected.png')


# Reading image from folder where it is stored 
img = cv2.imread(base_dir + '76.jpg') 
# denoising of image saving it into dst image 
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15) 
# Plotting of source and destination image 
plt.subplot(121), plt.imshow(img) 
plt.subplot(122), plt.imshow(dst) 
#plt.show()
plt.savefig(base_dir +'test.png')


"""
# erosion of the input image
name = '65.jpg'
img = cv2.imread(base_dir + name,0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
plt.imshow(erosion, cmap='gray')
plt.savefig(base_dir +'erosin.png')
"""