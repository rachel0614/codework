# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:22:22 2021

@author: hp
this is the image quality assessment experiment
"""

import imquality.brisque as brisque
import PIL.Image
from skimage import color
from skimage import io
import os
import csv

import warnings
import cv2

import pandas

def calculate_brisque_features(image, kernel_size=7, sigma=7/6):
    def calculate_features(coefficients_name, coefficients, accum=np.array([])):
        alpha, mean, sigma_l, sigma_r = asymmetric_generalized_gaussian_fit(coefficients)

        if coefficients_name == 'mscn':
            var = (sigma_l ** 2 + sigma_r ** 2) / 2
            return [alpha, var]
        
        return [alpha, mean, sigma_l ** 2, sigma_r ** 2]
    
    mscn_coefficients = calculate_mscn_coefficients(image, kernel_size, sigma)
    coefficients = calculate_pair_product_coefficients(mscn_coefficients)
    
    features = [calculate_features(name, coeff) for name, coeff in coefficients.items()]
    flatten_features = list(chain.from_iterable(features))
    return np.array(flatten_features)

# good performance for quality assessment!!!
# 0728
#path = r'D:/LYIT/dissertation/poor_quality/00883201355884_0.jpg'
#img = PIL.Image.open(path)
#img1 = color.rgb2gray(img)
warnings.simplefilter(action='ignore', category=FutureWarning)
#base_path = 'D:/LYIT/dissertation/dataset/'  #13 of 75 >=70
#base_path = 'D:/LYIT/dissertation/poor_quality/test/'
#base_path = 'D:/LYIT/dissertation/poor_quality/good/'
#base_path = 'D:/LYIT/repository/images/good_quality/' #4 of 114
#base_path = 'D:/LYIT/repository/yolo/labelled_meter/clear/'
#base_path = 'D:/LYIT/repository/yolo/detect_digit/exp18/'
base_path = 'D:/LYIT/repository/runs/counter140/unclear/'

src_path = base_path 
src_path = base_path
result_path = base_path + 'assessment/'
result_path = base_path
import shutil
# result csv

csvfile = open(result_path + 'result.csv', 'w')
fieldnames = ['file_name', 'score']
csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
csvwriter.writeheader()
    
print('load images from folder ' + base_path)
list = os.listdir(base_path)
file = ''
n = 0
score = 0;
m = 0
poor = []

for filename in os.listdir(src_path):
    #img = color.rgb2gray(io.imread(path))
    img = cv2.imread(os.path.join(src_path,filename))
    print(filename)
    print("aaaaaaaa............")
    #print(img)
    #height, width = img.shape[:2]
    bigger = cv2.resize(img, (200, 200), interpolation = cv2.INTER_CUBIC)

    score = brisque.score(bigger)
    print('checking the ', str(m))
    m += 1
    if score >= 70 :
        n += 1
        #poor.append(path)
        print(' image..' , str(n) , ' of ' , str(len(list)) , 'images has more than 70 sccore')
    #shutil.copy(src_path + filename, result_path + str(round(score)) + '_' + filename)
    csvwriter.writerow({'file_name': filename, 'score': score})
csvfile.close()

