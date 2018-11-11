import cv2
import numpy as np
 
video = cv2.VideoCapture(0)
 
while True:
    res, initImage = video.read()
    init_Gauss = cv2.GaussianBlur(initImage, (5, 5), 0)
    init_hsv = cv2.cvtColor(init_Gauss, cv2.COLOR_BGR2HSV)
 
    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])
    mask = cv2.inRange(init_hsv, lower_blue, upper_blue)
 
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
 
    for contour in contours:
        area = cv2.contourArea(contour)
 
        if area > 5000:
            cv2.drawContours(initImage, contour, -1, (0, 255, 0), 3)
 
 
    cv2.imshow("Processed Stream", initImage)
    cv2.imshow("Blue Objects", mask)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()