# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 20:41:40 2021

@author: hp
"""

import imquality.brisque as brisque
import PIL.Image
from skimage import color
from skimage import io
import os

import warnings

import pandas
base_path = 'D:/LYIT/dissertation/poor_quality/reflection/'

setDir = fullfile(toolboxdir(base_path),'imdata');
imds = imageDatastore(setDir,'FileExtensions',{'.jpg'});
opinionScores = 100*rand(1,size(imds.Files,1));
print('.............', opinionScores)



model = fitbrisque(imds,opinionScores')

I = imread(base_path + 'a1.jpg');
imshow(I)

brisqueI = brisque(I,model);
fprintf('BRISQUE score for the image is %0.4f.\n',brisqueI)