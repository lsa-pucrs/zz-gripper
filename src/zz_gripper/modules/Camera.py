#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from modules.Image import raspicam_image


class camera_calibration():
	
	def __init__(self):

		""" ROS SUBSCRIPTIONS """
		self.img_sub = rospy.Subscriber("/raspicam_node/image/image_raw", Image, self.cvt_image)

		""" VARIABLES """
		self.showImage = None

	def cvt_image(self, data):
		self.showImage =  raspicam_image().lastest_img(data)

	
