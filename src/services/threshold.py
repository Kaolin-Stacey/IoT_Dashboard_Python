from time import sleep

def checkLightThreshold():
    while(True):
        import config
        if config.lightVal < config.lightThreshold:
            from services.email import sendEmail
            sendEmail(f"The light level was lower than the threshold: {config.lightThreshold}. Turning on LED.")
            sleep(900)