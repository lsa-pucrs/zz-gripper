#!/usr/bin/env python
import cv2
import rospy
from modules.Image import image
from geometry_msgs.msg import Twist
from modules.Control_raspberry import control_raspberry

class robot(object):
	def __init__(self):
		
		""" ROS SUBSCRIPTIONS """
		self.pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
		rospy.Rate(5)

		""" VARIABLES """
		self.stop = 0
		self.slow_down = 0.8
		self.twist = Twist()
		self.robot = control_raspberry()
		distance_x = [209,212]
		distance_y = [137,189]	


	def turn(self):
		self.twist.angular.x = 0.8
		self.twist.angular.y = 0.8
		self.twist.angular.z = 2
		self.pub.publish(self.twist)
		rospy.loginfo("Gripper is turnning ...")
						
		rospy.Duration(75)

		self.twist.angular.z = self.stop
		self.pub.publish(self.twist)


	def centralized(self, img, masked_img):
		rospy.loginfo("Centralized robot ...")
		M = cv2.moments(img)
		circleX, circleY = image().circleXY(masked_img)
		
		result = False
		if M['m10'] != 0.0 and M['m01'] != 0.0 and M['m00'] != 0.0 and M is not None:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			if circleX in range(cx, cx+10) and circleY in range(cy, cy+10):	
				result = True
		
		return result

	def forward(self):
		#  Robot identified object, so it should open arm
		if(self.robot.flagOpenArm == True):
				self.robot.openArm()		
		
		#  Robot is walking and Is there an object close?
		if(self.robot.checkObjectDistance()):

			# Object is close, just close hand and check pression
			rospy.loginfo("Object is close ...")			
			while self.robot.checkPression():
				self.robot.closeHands()			
			
		else:

			# Object is not close, let's walk
			self.twist.angular.x = 2
			#self.twist.angular.y = 2
			#self.twist.angular.z = 2
			#self.pub.publish(self.twist)
			rospy.loginfo("Gripper is moving forward ...")

			rospy.Duration(75)
			
			self.twist.linear.x *= self.slow_down
			self.pub.publish(self.twist)
			
