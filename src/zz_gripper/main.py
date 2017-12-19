#!/usr/bin/env python
import rospy, cv2, time

from modules.Image import image
from modules.Camera import camera
from modules.Robot import robot

# --------------------------------------------
# This is the main executable for the robot
#---------------------------------------------

class Gripper(object):
	def __init__(self):

		cam = camera()
		img = image()
		gripper = robot()
		
		#  wait camera
		time.sleep(3.0)

		while(1):		
			cv2.imshow("Video", cam.showImage)
			cv2.imshow("Masked Video", img.masked(cam.showImage))
			
			if img.find_object(cam.showImage):
				if gripper.centralized(img.masked(cam.showImage),cam.showImage):
					gripper.forward()
				else:
					gripper.turn()
			else:
				gripper.turn()
			cv2.waitKey(1) & 0xFF
			
		cv2.destroyAllWindows()
def main():

	rospy.init_node('gripper', anonymous=False)
	robot = Gripper()
	rospy.spin()
	
if __name__ == "__main__" :
	main()
