# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:59:38 2021
convert label to recognition data
@author: hp
"""

import csv

base_path = 'D:/LYIT/repository/yolo/detect_digit/testimages/exp2_digit/labels/'
with open(base_path + '1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    line_count = 0
    for row in csv_reader:
     print(row[0])

sortedlist = sorted(csv_reader, key=lambda row: row[0], reverse=True)

# load the Digits class labels our YOLO model was trained on
labelsPath = os.path.sep.join([args["yolo"], "obj.names"])
LABELS = open(base_path).read().strip().split("\n")

###GIVE IMAGE PATH
image_path = "images/276_png.rf.f50ce99ca94a273d837031b9b2d95e17.jpg"


image = cv2.imread(image_path)

(H, W) = image.shape[:2]