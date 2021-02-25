import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

PIR_PIN = 26

GPIO.setup(PIR_PIN, GPIO.IN)


def readPir():
    state = GPIO.input(PIR_PIN)
    if state == 1:
        return True
    else:
        return False
