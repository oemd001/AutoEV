import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("kok.jpeg")
# Video input? Uncomment the line below. Comment line above.
# vid = cv2.VideoCapture("filename.filetype")

# Changing the image format to an OpenCV 'readable' format.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Include xml data. 
fullbody_data = cv2.CascadeClassifier("haarcascade_fullbody.xml")
lowerbody_data = cv2.CascadeClassifier("haarcascade_lowerbody.xml")
upperbody_data = cv2.CascadeClassifier("haarcascade_upperbody.xml")

# Setting minimum body size
full_detect = fullbody_data.detectMultiScale(img_gray, minSize = (2, 5)) #minSize = (2, 5)
lowerbody_detect = lowerbody_data.detectMultiScale(img_gray, minSize = (2, 5))
upperbody_detect = upperbody_data.detectMultiScale(img_gray, minSize = (2, 5))

count_full = len(full_detect)
count_lower = len(lowerbody_detect)
count_upper = len(upperbody_detect)

#if (count_full != 0):
for (x, y, width, height) in full_detect:
    cv2.rectangle(img_rgb, (x, y), (x + height, y + width), (0, 255, 0), 5)
        
# if (count_lower != 0):
for (x, y, width, height) in full_detect:
    cv2.rectangle(img_rgb, (x, y), (x + height, y + width), (0, 255, 0), 5)
        
#if (count_upper != 0):
for (x, y, width, height) in full_detect:
    cv2.rectangle(img_rgb, (x, y), (x + height, y + width), (0, 255, 0), 5)

# Returns image with rectangle(s)
plt.subplot(1, 1, 1) 
plt.imshow(img_rgb) 
plt.show() 
