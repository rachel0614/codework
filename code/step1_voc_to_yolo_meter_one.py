# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:42:01 2021

@author: hp
"""

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
# step1 - label conversion
# read voc label file, generate yolo format
# all classes
#classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'd']
classes = ['ArteMeter']
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    if w>=1:
        w=0.99
    if h>=1:
        h=0.99
    return (x,y,w,h)

def convert_annotation(rootpath,xmlname):
    xmlpath = rootpath + '/Annotations'
    xmlfile = os.path.join(xmlpath,xmlname)
    with open(xmlfile, "r", encoding='UTF-8') as in_file:
      txtname = xmlname[:-4]+'.txt'
      print(txtname)
      txtpath = rootpath + '/label_result'  #generated label files
      if not os.path.exists(txtpath):
        os.makedirs(txtpath)
      txtfile = os.path.join(txtpath,txtname)
      with open(txtfile, "w+" ,encoding='UTF-8') as out_file:
        tree=ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)
        out_file.truncate()
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            print(cls)

            if cls not in classes or int(difficult)==1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
            print(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == "__main__":
    #rootpath = 'D:/LYIT/dissertation/repository/yolo训练/labelled_digit'
    rootpath = 'D:/LYIT/repository/dataset/training/'

    xmlpath=rootpath+'/Annotations'
    list=os.listdir(xmlpath)
    for i in range(0,len(list)) :
        path = os.path.join(xmlpath,list[i])
        if ('.xml' in path)or('.XML' in path):
            convert_annotation(rootpath,list[i])
            print('done', i)
        else:
            print('not xml file',i)