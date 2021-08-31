# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 01:49:39 2021

@author: Administrator
"""
import os, random, shutil
import uuid
from string import Template

IMAGE_SAVE_PATH = 'D:\\LYIT\\dissertation\\repository\\yolo训练\\labelled_digit\\tmp\\'  # 图片转换后的地址
TEMPLATE_PATH = IMAGE_SAVE_PATH + "template.xml"


t = Template('I am $name from $city')
print('Template String =', t.template)
print(t.substitute({'name':'xxxxxxx','city':'zzzzzzz'}))

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
selected_digits = random.sample(digits, 7)

tags = {
    'd1': selected_digits[0],
    'd2': selected_digits[1],
    'd3': selected_digits[2],
    'd4': selected_digits[3],
    'd5': selected_digits[4],
    'd6': selected_digits[5],
    'd7': selected_digits[6]
}
print(tags)
with open(TEMPLATE_PATH, 'r' , encoding='utf-8') as f:
    s = f.read()
    src = Template(s)
    # Create a template that has placeholder for value of x
    #t = Template('x is $x')
    #print(src.template)
    result = src.substitute(tags)
    print(result)
    #print (src.substitute({'2' : 1}))
