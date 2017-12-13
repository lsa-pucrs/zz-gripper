#!/usr/bin/env python
import cv2
import numpy as np
from modules.Color import Color
from cv_bridge import CvBridge, CvBridgeError

class image():
	
	""" VARIABLES """
	def __init__(self):
		self.bridge = CvBridge()
		self._latestImage = None
		self._latestMaskedImage = None
		self._flagFindObject = 0

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

		self._latestMaskedImage = cv2.inRange(hsv, lower, upper) 
		return self._latestMaskedImage 

	def find_object():
		
		return 	
		
