# non curvature ref program

# Import necessary libraries
import cv2 as cv
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

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

# displays region of interest in said image. 
def regionofInterest(image):
    x = int(image.shape[1])
    y = int(image.shape[0])
    shape = np.array([[int(0), int(y)], [int(x), int(y)], [int(0.55*x), int(0.6*y)], [int(0.45*x), int(0.6*y)]])
    mask = np.zeros_like(image)
    if (len(image.shape) > 2):
        channelCount = image.shape[2]
        ignoreMaskColor = (255,) * channelCount
    else:
        ignoreMaskColor = 255 * channelCount
    cv.fillPoly(mask, np.int32([shape]), ignoreMaskColor)
    result = cv.bitwise_and(image, mask)
    return result
    
        
    

# displayImage(imgList)
# filterPlaceholder = list(map(filterImage, imgList))
# interestRegion = list(map(regionofInterest, imgList))
