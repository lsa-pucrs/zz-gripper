#!/usr/bin/env python
import cv2
import numpy as np
from modules.Color import Color
from cv_bridge import CvBridge, CvBridgeError

class image():
	
	
	def __init__(self):
		""" VARIABLES """
		self.bridge = CvBridge()
		self._latestImage = None
		self.latestMaskedImage = None
		self.circle_x = 0
		self.circle_y = 0

	def lastest_img(self, data):
		try:
			self._latestImage = self.bridge.imgmsg_to_cv2(data, "bgr8")
			return self._latestImage
		except CvBridgeError as e:
			print(e)
		
	def masked(self, data):
		hsv = cv2.cvtColor(data, cv2.COLOR_BGR2HSV)
		lower = np.array(Color.LOW_YELLOW)
		upper = np.array(Color.UPPER_YELLOW)

		self.latestMaskedImage = cv2.inRange(hsv, lower, upper) 
		return self.latestMaskedImage

	def find_object(self, data):
		result = False
		if self.circles(data) is not None:				
			result = True

		return result

	def circleXY(self, data):
		circles = self.circles(data)
		circle = 0
		if self.circles(data) is not None:				
			circle = np.round(circles[0,:]).astype("int")[0]

		return circle[0], circle[1]
        
	def circles(self, data):

		gray_img = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
		gray_img = cv2.medianBlur(gray_img,5)
		circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT,1,20,param1=50, param2=30, minRadius=0, maxRadius=0)

		return circles	
	
		
