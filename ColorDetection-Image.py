import cv2
import numpy as np

def getRedColor(image):
    image_blur = cv2.GaussianBlur(image, (7, 7), 0)
    #Numpy is BGR and cv is RGB
    min_red = np.array([0, 0, 0])
    max_red = np.array([50, 50, 255])
    mask = cv2.inRange(image, min_red, max_red)
    #Add mask to image
    rgb_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    img = cv2.addWeighted(rgb_mask, 0.5, image, 0.5, 0)
    #Show images
    cv2.imshow("Gaussian Blurred",image_blur)
    cv2.imshow("Mask", img)
    
    
#Read from directory
initImage = cv2.imread("ballons.jpg")
#Show the image scaled
scale = 0.25
initImage = cv2.resize(initImage, None, fx=scale, fy=scale)
cv2.imshow("Input",initImage)
getRedColor(initImage)
#This code waits for any key to be pressed
cv2.waitKey(0)
if cv2.waitKey(1) & 0xFF == ord('q'): 
    #Once pressed destroy all opened windows
    cv2.destroyAllWindows()

