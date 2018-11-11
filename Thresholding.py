import cv2
import numpy as np

def thresholdImage(img):
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
    cv2.imshow("Thresholded", threshold)
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imshow('Adaptive threshold',th)
    retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('Otsu threshold',threshold2)


#Read from main camera
video =  cv2.VideoCapture(0)
while(True):
    res,initImage = video.read()
    #Show the frame scaled
    scale = 0.25
    initImage = cv2.resize(initImage, None, fx=scale, fy=scale)
    cv2.imshow('Video Stream',initImage)
    thresholdImage(initImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
video.release()
cv2.destroyAllWindows()

