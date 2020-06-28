
# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins 
GPIO.setup(11, GPIO.OUT) # I/O Pin for servo motor1
GPIO.setup(12, GPIO.OUT) # I/O Pin for servo motor2

GPIO.setup(12, GPIO.OUT)

s1 = GPIO.PWM(11, 50) # Connected to PWMB
s2 = GPIO.PWM(12, 50) # Connected to PWMA

s1.start(0)
s2.start(0)

 
def deliver(pincode):
    try:
        while True:
            if(pincode == 1):
                s1.ChangeDutyCycle(7.5) #TURN SERVO MOTOR BY 180 i.e push the package in cart 1  
                s2.ChangeDutyCycle(2.5)

            elif (pincode == 2):
                s2.ChangeDutyCycle(7.5) #TURN BOTH SERVO MOTOR BY 180 i.e push the package in cart 2 
                s1.ChangeDutyCycle(7.5)
                
            elif (pincode == 3):
                s2.ChangeDutyCycle(7.5) #TURN SERVO MOTOR BY 90 i.e push the package in cart 3 
                s1.ChangeDutyCycle(2.5)
        
            GPIO.cleanup()
    except KeyboardInterrupt:
        s1.stop(0)
        s2.stop(0)
        GPIO.cleanup()









