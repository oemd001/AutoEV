# Webcam/Camera Test

import os
import cv2 as cv

cv.namedWindow("test")

# VideoCapture(0) will use iPhone camera.
# VideoCapture(1) will use built in iSight camera.
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
