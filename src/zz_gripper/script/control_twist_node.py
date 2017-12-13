#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, TwistStamped

class cmd_vel_node(object):
	def __init__(self):
		
		""" ROS SUBSCRIPTIONS """
		self.cmd_vel_pub = rospy.Publisher("cmd_vel", Twist, queue,size=5)

		""" VARIABLES """
		self.move_cmd = Twist()
		self.slow_down_factor = 0.8


	def callback(self, cmd_velocity):
		self.baseVelocity.twist = cmd_velocity


	def turn():
		self.move_cmd.angular.z *= self.slow_down_factor
		self.cmd_vel_pub.publish(self.move_cmd)

	def forward():
		self.move_cmd.linear.x *= self.slow_down_factor
		self.cmd_vel_pub.publish(self.move_cmd)
		
