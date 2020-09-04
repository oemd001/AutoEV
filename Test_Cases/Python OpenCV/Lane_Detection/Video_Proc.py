import cv2 as cv
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from moviepy.video.io.VideoFileClip import VideoFileClip
import numpy as np
import moviepy
import sys
import os

# Adding the list of images to imgFiles via the append method. 
imgDir = "Test_Images/"
imgFiles = os.listdir(imgDir)
imgList = []
for i in range(len(imgFiles)):
    imgList.append(mpimg.imread(imgDir + imgFiles[i])) # mpimg is part of matplotlib

# Adding webcam test program


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
    #return result

# self explanatory. Converts RGB to grayscale. 
def grayscale(image):
    return cv.cvtColor(image, cv.COLOR_RGB2GRAY)

def canny(image):
    lower = 50
    upper = 120
    return cv.Canny(grayscale(image), lower, upper)

rightSlope, leftSlope, rightIntercept, leftIntercept = [],[],[],[]

def draw_lines(img, lines, thickness=5):
    global rightSlope, leftSlope, rightIntercept, leftIntercept
    rightColor=[0,255,0]
    leftColor=[255,0,0]
    #this is used to filter out the outlying lines that can affect the average
    #We then use the slope we determined to find the y-intercept of the filtered lines by solving for b in y=mx+b
    for line in lines:
        for x1,y1,x2,y2 in line:
            slope = (y1-y2)/(x1-x2)
            if slope > 0.3:
                if x1 > 500 :
                    yintercept = y2 - (slope*x2)
                    rightSlope.append(slope)
                    rightIntercept.append(yintercept)
                else: None
            elif slope < -0.3:
                if x1 < 600:
                    yintercept = y2 - (slope*x2)
                    leftSlope.append(slope)
                    leftIntercept.append(yintercept)
    #We use slicing operators and np.mean() to find the averages of the 30 previous frames
    #This makes the lines more stable, and less likely to shift rapidly
    leftavgSlope = np.mean(leftSlope[-30:])
    leftavgIntercept = np.mean(leftIntercept[-30:])
    rightavgSlope = np.mean(rightSlope[-30:])
    rightavgIntercept = np.mean(rightIntercept[-30:])
    #Here we plot the lines and the shape of the lane using the average slope and intercepts
    try:
        left_line_x1 = int((0.65*img.shape[0] - leftavgIntercept)/leftavgSlope)
        left_line_x2 = int((img.shape[0] - leftavgIntercept)/leftavgSlope)
        right_line_x1 = int((0.65*img.shape[0] - rightavgIntercept)/rightavgSlope)
        right_line_x2 = int((img.shape[0] - rightavgIntercept)/rightavgSlope)
        pts = np.array([[left_line_x1, int(0.65*img.shape[0])],[left_line_x2, int(img.shape[0])],[right_line_x2, int(img.shape[0])],[right_line_x1, int(0.65*img.shape[0])]], np.int32)
        pts = pts.reshape((-1,1,2))
        cv.fillPoly(img,[pts],(0,0,255))
        cv.line(img, (left_line_x1, int(0.65*img.shape[0])), (left_line_x2, int(img.shape[0])), leftColor, 10)
        cv.line(img, (right_line_x1, int(0.65*img.shape[0])), (right_line_x2, int(img.shape[0])), rightColor, 10)
    except ValueError:
    #I keep getting errors for some reason, so I put this here. Idk if the error still persists.
        pass
    
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.
    """
    lines = cv.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

def linedetect(img):
    return hough_lines(img, 1, np.pi/180, 10, 20, 100) # Changed the number of intersections required from 10 to 5

def overlayImage(setInput):
    image = list(setInput)
    return cv.addWeighted(image[0], 1, image[1], 0.8, 0)

def imageProcess(image):
    imageFilter = filterImage(image)
    imageInterest = regionofInterest(imageFilter)
    cannyImage = canny(imageInterest)
    imageLine = hough_lines(cannyImage, 1, np.pi/180, 5, 20, 5)
    result = cv.addWeighted(imageLine, 1, image, 0.8, 0)
    return imageInterest

def showVideo():
    cv.namedWindow("test")
    videoCapture = cv.VideoCapture(0)

    if videoCapture.isOpened():
        rval, frame = videoCapture.read() # attempts to read the first frame
    else:
        rval = False
    while rval:
        cv.imshow("test", frame)
        rval, frame = videoCapture.read()
        key = cv.waitKey(20)
        if key == 27: # aka escape key
            break
    cv.destroyWindow("test")

showVideo()
# find the vales for x and y. May need to manually modify those values to better include region of interest. 
