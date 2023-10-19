import RPi.GPIO as GPIO

import config

def toggleFan():
    from config import fanOn
    GPIO.output(config.fanEnablePin,fanOn)