import RPi.GPIO
from time import sleep

motor1 = 4
motor2 = 14

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor1, GPIO.out)
    GPIO.setup(motor2, GPIO.out)

def loop():
    GPIO.output(motor1, HIGH)
    GPIO.output(motor2, LOW)
def stop():
    GPIO.output(motor1, LOW)
    GPIO.output(motor2, LOW)

def forward():
    setup()
    loop()
    sleep(10)
    
