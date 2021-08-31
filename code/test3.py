# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 21:51:25 2021

@author: hp
"""

# Load the libraries
import cv2
import pytesseract
# Load the image
img = cv2.imread("D:/LYIT/repository/bin1.png")

# Convert it to the gray-scale
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# OCR detection
d = pytesseract.image_to_data(gry, config="--psm 6", output_type=pytesseract.Output.DICT)

# Get ROI part from the detection
n_boxes = len(d['level'])

# For each detected part
for i in range(n_boxes):

    # Get the localized region
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])

    # Draw rectangle to the detected region
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 5)

    # Crop the image
    crp = gry[y:y+h, x:x+w]

    # OCR
    txt = pytesseract.image_to_string(crp, config="--psm 6")
    print(txt)

    # Display the cropped image
    cv2.imshow("crp", crp)
    cv2.waitKey(0)

# Display
cv2.imshow("img", img)
cv2.waitKey(0)
