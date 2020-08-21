# non curvature ref program

# Import necessary libraries
import cv2 as cv
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# If you only have one image, uncomment this code. It's better to have multiple to have better results from the ML
# img = cv.imread("image.jpg")
# img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

# Adding the list of images to imgFiles via the append method. 
imgDir = "Test_Images/"
imgFiles = os.listdir(imgDir)
imgList = []
for i in range(len(imgFiles)):
    imgList.append(mpimg.imread(imgDir + imgFiles[i])) # mpimg is part of matplotlib

# Run this method to test whether the program actually detects the given images. 
def displayImage(images, cmap = None):
    plt.figure(figsize=(40, 40))
    for i, image in enumerate(images):
        plt.subplot(3, 2, i + 1)
        plt.imshow(image, cmap)
        plt.autoscale(tight = True)
    plt.show()

# HLS color filtering.
# BGR is uncesseary as HLS removes all extraneous colors
def filterImage(image):
    hls = cv.cvtColor(image, cv.COLOR_RGB2HLS)
    whiteLower = np.array([0, 190, 0])
    whiteUpper = np.array([255, 255, 255])
    yellowLower = np.array([10, 0, 90])
    yellowUpper = np.array([50, 255, 255])
    yellowMask = cv.inRange(hls, yellowLower, yellowUpper)
    whiteMask = cv.inRange(hls, whiteLower, whiteUpper)
    mask = cv.bitwise_or(yellowMask, whiteMask)
    maskResult = cv.bitwise_and(image, image, mask = mask)
    return maskResult

displayImage(imgList)