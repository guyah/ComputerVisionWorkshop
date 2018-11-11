import cv2
import numpy as np

def getRedColor(image):
    image_blur = cv2.GaussianBlur(image, (7, 7), 0)
    #Numpy is BGR and cv is RGB
    #HSV is Hue saturation value (or brightness)
    image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_BGR2HSV)
    min_red = np.array([0, 100, 80])
    max_red = np.array([10, 256, 256])
    mask1 = cv2.inRange(image_blur_hsv, min_red, max_red)
    min_red2 = np.array([170, 100, 80])
    max_red2 = np.array([180, 256, 256])
    mask2 = cv2.inRange(image_blur_hsv, min_red2, max_red2)
    mask = mask1 + mask2
    rgb_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    img = cv2.addWeighted(rgb_mask, 0.5, image, 0.2, 0)
   
    cv2.imshow("Output", img)
    
    
#Read from main camera
video =  cv2.VideoCapture(0)
while(True):
    res,initImage = video.read()
    #Show the frame scaled
    scale = 0.25
    initImage = cv2.resize(initImage, None, fx=scale, fy=scale)
    cv2.imshow('Video Stream',initImage)
    getRedColor(initImage)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
video.release()
cv2.destroyAllWindows()
   

