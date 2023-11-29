import RPi.GPIO as GPIO

import config

def toggleLed():
    from config import ledOn
    GPIO.output(config.ledPin, not ledOn)