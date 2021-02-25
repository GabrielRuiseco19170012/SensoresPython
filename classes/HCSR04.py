import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TRIG = 23
ECHO = 24
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)


def readHC():
    GPIO.output(TRIG, False)
    print("Waiting for sensor")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulseStart = time.time()

    while GPIO.input(ECHO) == 1:
        pulseEnd = time.time()

    distance = round((pulseStart - pulseEnd) * 17150, 2)
    return distance
