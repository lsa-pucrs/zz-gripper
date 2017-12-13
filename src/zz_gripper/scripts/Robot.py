#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, TwistStamped
from modules.Raspberry import raspberry

class robot(object):
	def __init__(self):
		
		""" ROS SUBSCRIPTIONS """
		self.cmd_vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size=5)

		""" VARIABLES """
		self.stop = 0
		self.slow_down = 0.8
		self.move_cmd = Twist()
		self.robot = raspberry()


	def callback(self, cmd_velocity):
		self.baseVelocity.twist = cmd_velocity

	def turn(self):
		self.move_cmd.angular.z *= self.slow_down
		self.cmd_vel_pub.publish(self.move_cmd)
		rospy.loginfo("Gripper is turnning ...")
						
		rospy.Duration(75)

		self.move_cmd.angular.z = self.stop
		self.cmd_vel_pub.publish(self.move_cmd)


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
			self.move_cmd.linear.x *= self.slow_down
			self.cmd_vel_pub.publish(self.move_cmd)
			rospy.loginfo("Gripper is moving forward ...")

			rospy.Duration(75)
			
			self.move_cmd.linear.x *= self.slow_down
			self.cmd_vel_pub.publish(self.move_cmd)
			