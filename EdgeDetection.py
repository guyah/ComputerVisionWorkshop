import cv2
import numpy as np

#Read from main camera
video =  cv2.VideoCapture(0)
while(True):
    res,initImage = video.read()
    #Show the frame scaled
    scale = 0.25
    initImage = cv2.resize(initImage, None, fx=scale, fy=scale)
    cv2.imshow('Video Stream',initImage)
    canyEdge = cv2.Canny(initImage, 100, 200)
    cv2.imshow("Canny",canyEdge)
    sobel = cv2.Sobel(initImage,cv2.CV_8U,1,1,ksize=5)
    cv2.imshow("Sobel",sobel)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
video.release()
cv2.destroyAllWindows()