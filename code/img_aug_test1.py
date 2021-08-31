# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 23:03:06 2021
https://neptune.ai/blog/data-augmentation-in-python
@author: hp
"""

from deepaugment.deepaugment import DeepAugment
my_images = "D:/LYIT/repository/tesseract/002-IMG-MED.jpg"
deepaug = DeepAugment(my_images, my_labels)
best_policies = deepaug.optimize(300)