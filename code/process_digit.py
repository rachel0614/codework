# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 00:12:46 2021
for processing the dataset
@author: hp
"""

import step1_voc_to_yolo_digits
import step2_split_dataset
import step3_config_meter



step1_voc_to_yolo_digits.doStep1('D:/LYIT/repository/yolo/labelled_digit')
# for test & val
train_test_percent = 1
train_valid_percent= 1

# for train
# generate dataset WITHOUT TEST step2_split_dataset.doStep2('D:/LYIT/repository/yolo/labelled_digit',1,0.9)

#step2_split_dataset.doStep2('D:/LYIT/repository/yolo/labelled_digit',1,0.9)

# generate dataset with only test set
step2_split_dataset.doStep2('D:/LYIT/repository/yolo/labelled_digit',0.9,0.9)


step3_config_meter.doStep3('D:/LYIT/repository/yolo/labelled_digit/')

