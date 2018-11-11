import cv2
import numpy as np
from collections import deque
import time
import imutils

video = cv2.VideoCapture(0)
lower_blue = np.array([38, 86, 0])
upper_blue = np.array([121, 255, 255])

#Life time of painting
pts = deque(maxlen=10)
while (True):
	# grab the current frame
	_,initImage = video.read()
	# resize the frame, blur it, and convert it to the HSV
	# color space
	initImage = imutils.resize(initImage, width=600)
	blurred = cv2.GaussianBlur(initImage, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the object
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(initImage, (int(x), int(y)), int(radius),
				(255, 0, 0), 3)
			cv2.circle(initImage, center, 5, (0, 0, 255), -1)

	# update the points queue
	pts.appendleft(center)

	# loop over the set of tracked points
	for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue

		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		thickness = int(np.sqrt(30 / float(i + 1)))
		cv2.line(initImage, pts[i - 1], pts[i], (0, 0, 255), thickness)

	# show the frame to our screen
	cv2.imshow("Tracking Object", initImage)
	 

	# if the 'q' key is pressed, stop the loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
        
        




# close all windows
cv2.destroyAllWindows()