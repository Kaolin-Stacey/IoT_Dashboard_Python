from threading import Thread, Timer

import services.dht as tempService
thread_dht = Thread(target=tempService.getData, name="dht")
thread_dht.start()

import services.email as emailService
thread_email = Thread(target=emailService.checkTemperatureSendEmail, name="emailService")
thread_email.start()

import services.fan as fanService
thread_fan = Thread(target=fanService.checkFan,name="fanService")
thread_fan.start()

import services.threshold as thresholdService
thread_threshold = Thread(target=thresholdService.checkLightThreshold, name="thresholdService")
thread_threshold.start()

import services.mqtt as mqttService