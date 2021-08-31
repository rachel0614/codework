# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 20:16:12 2021

@author: hp
"""

import matplotlib.image as im
import matplotlib.pyplot as plt
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
import PIL
from PIL import Image
base_path = "D:/LYIT/dissertation/dataset/incorrect/"

list_im =  ['1.jpg','2.jpg','3.jpg', '4.jpg']

imgs    = [ PIL.Image.open(base_path + i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save(base_path + 'Trifecta.jpg' )    

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( base_path + 'Trifecta_vertical.jpg' )