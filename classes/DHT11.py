import RPi.GPIO as GPIO
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BOARD)
DHT_PIN = 4
GPIO.setup(DHT_PIN, GPIO.IN)


def readDht():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        data = {"Temp": temperature, "Humidity": humidity}
    return data
