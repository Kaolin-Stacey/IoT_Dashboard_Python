import RPi.GPIO as GPIO
import config
from config import ledPin, fanEnablePin, fanInput1Pin, fanInput2Pin

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(fanEnablePin, GPIO.OUT)
GPIO.setup(fanInput1Pin, GPIO.OUT)
GPIO.setup(fanInput2Pin, GPIO.OUT)
GPIO.output(fanInput1Pin, 0)
GPIO.output(fanEnablePin, 1)