#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CompressedImage

class Gripper:
	def __init__(self):
		rospy.loginfo("Starting pick and place robot ...")
		self.camera = rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.callback, queue_size=1)
		
	def callback(self, image):
		print(image.data)

if __name__ == '__main__':
	try:
		Gripper()
		rospy.init_node('gripper', anonymous=True)
	except rospy.ROSInterruptException:
		print("Error")
