#importing the libraries

#from picamera import PiCamera
import RPi.GPIO as GPIO
import numpy as np
import time,os
import scanner


#setup the GPIO pin for the servo

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)    # for platform


m1=GPIO.PMW(33,50)   #50 Hz (20ms PMW period)


m1.start(0)

# Pins for Motor Driver Inputs 
Motor1A = 24
Motor1B = 16
Motor1E = 25
 
def setup():
	GPIO.setmode(GPIO.BCM)				 # GPIO Numbering
	GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)
 
def loop():
	# Going forwards
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
 
	sleep(5)
 	# Going backwards
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
 
	sleep(5)
	# Stop
	GPIO.output(Motor1E,GPIO.LOW)

"""def SetAngle(angle):

	duty = angle / 18 + 2

	GPIO.output(22, True)

	m2.ChangeDutyCycle(duty)

	time.sleep(1)

	GPIO.output(22, False)

	m2.ChangeDutyCycle(0)"""
def get_pincode():
	try:
	setup()
	while True:
		p = scanner.scan_video()
		if not (p):
			return p
		loop()				
	
		m1.ChangeDutyCycle(7.0)       # rotate the platform by 90 degrees
		time.sleep(2)


	
