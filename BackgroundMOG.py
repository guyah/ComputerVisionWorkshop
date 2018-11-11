import cv2
import numpy as np
 

#Read from main camera
video =  cv2.VideoCapture(0)
subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)
while(True):
    res,initImage = video.read()
    #Show the frame scaled
    scale = 0.25
    initImage = cv2.resize(initImage, None, fx=scale, fy=scale)
    mask = subtractor.apply(initImage)
    cv2.imshow("mask", mask)
    cv2.imshow('Video Stream',initImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
video.release()
cv2.destroyAllWindows()