import RPi.GPIO as GPIO

import config
from time import sleep

def toggleFan():
    import config
    GPIO.output(config.fanInput2Pin,config.fanOn)

def checkFan():
    import services.email as em
    while(True):
        em.checkTemperatureSendEmail()
                