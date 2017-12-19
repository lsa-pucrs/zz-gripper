#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

class control_raspberry(object):

	def __init__(self):
		self.flagOpenArm = False

		self.interval = 0.1
		distance = 0
		self.anguleLeft = 2.5
		self.anguleRight = 12.5
		self.adc = Adafruit_ADS1x15.ADS1115()
		
		# Set which GPIO pins the drive outputs are connected
		HAND_LEFT = 13
		HAND_RIGHT = 16
		STBY = 22
		PWMB = 23
		BIN1 = 24
		BIN2 = 25
		self.tri = 20
		self.echo = 26	

		# GPIO SETUP
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		# MOTOR LEFT/RIGHT
		GPIO.setup(HAND_LEFT, GPIO.OUT)
		GPIO.setup(HAND_RIGHT, GPIO.OUT) 

		# MOTOR UP/DOWN
		GPIO.setup(BIN1, GPIO.OUT)
		GPIO.setup(BIN2, GPIO.OUT)
		GPIO.setup(STBY, GPIO.OUT)
		GPIO.setup(PWMB, GPIO.OUT)

		# SENSOR SONAR
		GPIO.setup(self.tri, GPIO.OUT)
		GPIO.setup(self.echo, GPIO.IN)

		GPIO.output(self.tri, False)
		time.sleep(0.5)
		GPIO.setwarnings(False)

		self.handLeft = GPIO.PWM(HAND_LEFT,50)
		self.handRight = GPIO.PWM(HAND_RIGHT,50)

		self.handLeft.start(0)
		self.handRight.start(0)
		####################################

	def openArm(self):
		if self.flagOpenArm == False:
			self.flagOpenArm = True
		self.openHands()


	def checkObjectDistance(self):	
		minTargetDistance = 0.12
		distance = self.sonarDistance()
		time.sleep(self.interval)

		return  True if distance <= minTargetDistance else False
		
	def up():
		(GPIO.output(BIN1, GPIO.HIGH))
		(GPIO.output(BIN2, GPIO.LOW))
		(GPIO.output(STBY, GPIO.HIGH))
		(GPIO.output(PWMB, GPIO.HIGH))

	def down():
		(GPIO.output(BIN1, GPIO.LOW))
		(GPIO.output(BIN2, GPIO.HIGH))
		(GPIO.output(STBY, GPIO.HIGH))
		(GPIO.output(PWMB, GPIO.HIGH))

	def closeHands(self):
		self.anguleLeft = self.anguleLeft + 1
		self.anguleRight = self.anguleRight - 1

		self.handLeft.ChangeDutyCycle(self.anguleLeft)
		self.handRight.ChangeDutyCycle(self.anguleRight)	

		self.flagOpenArm = True		
		time.sleep(1)
						
	def openHands(self):	
		self.anguleLeft = 5.5
		self.anguleRight = 9.5
		self.handLeft.ChangeDutyCycle(self.anguleLeft)
		self.handRight.ChangeDutyCycle(self.anguleRight)
		time.sleep(2)

	def sonarDistance(self):
		GPIO.output(self.tri, True)
		time.sleep(0.00001)
		GPIO.output(self.tri, False)
		start = 0
		stop = 0    

		while GPIO.input(self.echo) == 0:
			start = time.time()

		while GPIO.input(self.echo) == 1:
			stop = time.time()

	 	distance = (stop - start) * (17150 + 0.6 * 20)

		return round(distance/100,2)

	# Check pression sensor
	def checkPression(self):		
		gain = 1
		flag= False
		analog_chn = 0
		force = 20000
	
		if  self.adc.read_adc(analog_chn, gain=gain) < force:
	  		flag =True
			self.up()
	
		return flag

