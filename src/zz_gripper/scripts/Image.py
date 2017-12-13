#!/usr/bin/env python
import cv2
import numpy as np
from modules.Color import Color
from cv_bridge import CvBridge, CvBridgeError

class image():

	""" ROS SUBSCRIPTIONS """
	self.cmd_vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size=5)

	
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


	def find_object(self):
		# TODO: Refactoring
		# From mask data, find the center point 
		h, w, d = self._latestMaskedImage.shape
    search_top = 3*h/4
    search_bot = 3*h/4 + 20
    mask[0:search_top, 0:w] = 0	
    mask[search_top:h, 0:w] = 0
    M = cv2.moments(mask)

    if M['m00'] > 0:
 			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			cv2.circle(image,(cx,cy),20,(0,0,255),-1)
			err = cx - w/2

      self.twist.linear.x = 0.5
      self.twist.angular.z = -float(err) / 100
      self.cmd_vel_pub.publish(self.twist)

     # Find yellow circle 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		img = cv2.medianBlur(gray,5)
		circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)    
	
		return  True if len(circle) >= 1 else False 	
		
