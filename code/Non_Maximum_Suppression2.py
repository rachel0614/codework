# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 00:52:29 2021

@author: hp
"""


import matplotlib.pyplot as plt
import matplotlib.patches as patches

base_path = 'D:/LYIT/repository/runs/nms/'
image = plt.imread(base_path + '005472.jpg')

# draw emtpy figure
fig = plt.figure()

# define axis
ax = fig.add_axes([0, 0, 1, 1])

# plot image
plt.imshow(image)
      
# create rectangular patch
#dog
rect_0 = patches.Rectangle((190, 380), 300, 150, edgecolor='red', facecolor='none', linewidth=2)
rect_1 = patches.Rectangle((300, 420), 150, 210, edgecolor='green', facecolor='none', linewidth=2)
rect_2 = patches.Rectangle((320, 360), 200, 230, edgecolor='blue', facecolor='none', linewidth=2)

#person
rect_3 = patches.Rectangle((390, 50), 300, 330, edgecolor='red', facecolor='none', linewidth=2)
rect_4 = patches.Rectangle((490, 45), 200, 500, edgecolor='green', facecolor='none', linewidth=2)
rect_5 = patches.Rectangle((480, 130),150,400, edgecolor='blue', facecolor='none', linewidth=2)
    
# add patch
#dog
ax.add_patch(rect_0)
ax.text(188, 376, 'Box0:90%', color='red')
ax.add_patch(rect_1)
ax.text(328, 416, 'Box1:98%', color='green')
ax.add_patch(rect_2)
ax.text(318, 356, 'Box2:82%', color='blue')

#person
ax.add_patch(rect_3)
ax.text(388, 44, 'Box3:87%', color='red')
ax.add_patch(rect_4)
ax.text(492, 33, 'Box4:98%', color='green')
ax.add_patch(rect_5)
ax.text(478, 126, 'Box5:82%', color='blue')

# show figure
plt.show()


import torch
from torchvision.ops import nms


boxes = torch.tensor([[190,380,(190+300),(380+150)],
                      [300,420,(300+150),(420+210)],
                      [320,360,(320+200),(360+230)],

                      [390,50,(390+300),(50+330)],
                      [490,45,(490+200),(45+500)],
                      [480,130,(480+150),(130+400)]], dtype=torch.float32)

scores = torch.tensor([[0.90],[0.98],[0.82], [0.87],[0.98],[0.82]], dtype=torch.float32)

nms(boxes = boxes, scores = scores, iou_threshold=0.2)