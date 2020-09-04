# Webcam/Camera Test

import os
import cv2 as cv

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
