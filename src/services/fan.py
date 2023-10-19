import RPi.GPIO as GPIO

import config



def toggleFan():
    from config import fanOn
    GPIO.output(config.fanInput2Pin,fanOn)

def checkFan():
    fanOnTmp = False
    while(True):
        from config import fanOn
        if config.fanOn != fanOnTmp:
            fanOnTmp = config.fanOn
            toggleFan()