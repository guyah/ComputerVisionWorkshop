import cv2
import numpy as np
from time import sleep 


def subUsingDiff(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
 
    difference = cv2.absdiff(first_gray, gray_frame)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
 
    cv2.imshow("First frame", first_img)
    cv2.imshow("Frame", frame)
    cv2.imshow("difference", difference)
 

 #Read from main camera
video =  cv2.VideoCapture(0)
sleep(2)
_,first_img = video.read()
first_gray = cv2.cvtColor(first_img, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)
while(True):
    res,initImage = video.read()
    #Show the frame scaled
    #scale = 0.25
    #initImage = cv2.resize(initImage, None, fx=scale, fy=scale)
    cv2.imshow('Video Stream',initImage)
    subUsingDiff(initImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
video.release()
cv2.destroyAllWindows()


