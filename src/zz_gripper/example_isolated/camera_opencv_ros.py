# import the necessary packages
from picamera.array import PiRGBArray
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from picamera import PiCamera
import rospy, cv2, time, numpy


class Gripper:
  def __init__(self):

	camera = PiCamera()
	camera.resolution = (240, 280)
	camera.framerate = 32
	rawCapture = PiRGBArray(camera, size=(640, 480))

	# allow the camera to warmup
	time.sleep(0.1)

	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])

	
	# capture frames from the camera
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		image = frame.array

		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)	
		mask = cv2.inRange(hsv, lower_blue, upper_blue)
		res = cv2.bitwise_and(image, image, mask= mask)

    		    
		# show the frame
		cv2.imshow("Image", image)
		cv2.imshow("Mask", mask)
		cv2.imshow("Final Result", res)
		key = cv2.waitKey(1) & 0xFF

rospy.init_node('turtlebot_tracker')
robot = Gripper()
rospy.spin()
