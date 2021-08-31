#%%

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Administrator/Downloads/ArteMeter/40.jpg',0)

ret, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu阈值
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# 11为block size，2为C值
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY,11,2 )
th4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY,11,2)

titles = ['original image', 'global thresholding (v=127)', 'otus thresholding','Adaptive mean thresholding', 'adaptive gaussian thresholding']
images = [img,th1,th2,th3,th4]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
#plt.savefig('duibi.png')
plt.show()

#cv2.imshow('Original', img)
cv2.imshow('BINARY', th1)
#cv2.imshow('OTSU', th2)
#cv2.imshow('ADAPTIVE_THRESH_MEAN', th3)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN', th4)



cv2.waitKey(0)
cv2.destroyAllWindows()