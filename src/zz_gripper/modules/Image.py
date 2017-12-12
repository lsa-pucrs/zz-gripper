#!/usr/bin/env python
import cv2
import numpy as np
from modules.Color import Color
from cv_bridge import CvBridge, CvBridgeError

class raspicam_image():
	
	""" VARIABLES """
	def __init__(self):
		self.bridge = CvBridge()
		self._latestImage = None
		
	def lastest_img(self, data):
		try:
			self._latestImage = self.bridge.imgmsg_to_cv2(data, "bgr8")
			return self._latestImage

		except CvBridgeError as e:
			print(e)

		
	def mask_img(self, data):
		mask, result = self.hsv_mask_res_images(data)
		return mask
	
	def find_object():
		return True


	def hsv_mask_res_images(self, data):

		hsv = cv2.cvtColor(data, cv2.COLOR_BGR2HSV)
		lower = np.array(Color.LOW_GREEN)
		upper = np.array(Color.UPPER_GREEN)

		mask = cv2.inRange(hsv, lower, upper)
		res = cv2.bitwise_and(data, data, mask= mask)
			
		return mask,res

		
