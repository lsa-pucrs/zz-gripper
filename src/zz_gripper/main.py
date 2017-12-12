#!/usr/bin/env python
import rospy, cv2, time

from modules.Camera import camera_calibration
from modules.Image import raspicam_image
from modules.Control_twist import  cmd_vel_node

# --------------------------------------------
# This is the main executable for the robot
#---------------------------------------------

class Gripper(object):
	def __init__(self):
		cc = camera_calibration()
		img = raspicam_image()
		gripper = cmd_vel_node()	

		#  wait camera
		time.sleep(3.0)

		while(1):			
			cv2.imshow("Video", cc.showImage)
			cv2.imshow("Mask Target", img.mask_img(cc.showImage))
			
			if img.find_object:
				gripper.forward()
			else:
				gripper.turn()

			cv2.waitKey(1) & 0xFF
			
		cv2.destroyAllWindows()
def main():

	rospy.init_node('gripper', anonymous=True)
	robot = Gripper()
	rospy.spin()
	
if __name__ == "__main__" :
	main()
