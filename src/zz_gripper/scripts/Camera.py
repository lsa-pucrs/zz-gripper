#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from modules.Image import image

class camera():
	
	def __init__(self):

		""" ROS SUBSCRIPTIONS """
		rospy.Subscriber("/raspicam_node/image/image_raw", Image, self.cvt_image)

		""" VARIABLES """
		self.showImage = None

	def cvt_image(self, data):
		self.showImage =  image().lastest_img(data)