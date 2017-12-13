#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, TwistStamped
from modules.Control_raspberry import control_raspberry

class cmd_vel_node(object):
	def __init__(self):
		
		""" ROS SUBSCRIPTIONS """
		self.cmd_vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size=5)

		""" VARIABLES """
		self.move_cmd = Twist()
		self.slow_down_factor = 0.8
		self.stop_factor = 0
		self.robot = control_raspberry()


	def callback(self, cmd_velocity):
		self.baseVelocity.twist = cmd_velocity

	def turn(self):
		self.move_cmd.angular.z *= self.slow_down_factor
		self.cmd_vel_pub.publish(self.move_cmd)
		rospy.loginfo("Gripper is turnning ...")
						
		rospy.Duration(75)

		self.move_cmd.angular.z = self.stop_factor
		self.cmd_vel_pub.publish(self.move_cmd)

	def forward(self):
		if(self.robot.needOpenArm == True):
				self.robot.openArm()		
		
		if(self.robot.isCloseToPickTarget()):

			while self.robot.hasObjectOnHand():
				self.robot.closeHands()			
			rospy.loginfo("Object is close ...")
		else:
			self.move_cmd.linear.x *= self.slow_down_factor
			self.cmd_vel_pub.publish(self.move_cmd)
			rospy.loginfo("Gripper is moving forward ...")

			rospy.Duration(75)
			
			self.move_cmd.linear.x *= self.slow_down_factor
			self.cmd_vel_pub.publish(self.move_cmd)
			
		
