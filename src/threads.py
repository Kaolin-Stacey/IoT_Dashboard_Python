from threading import Thread, Timer

import services.dht as tempService
thread_dht = Thread(target=tempService.getData, name="dht")
thread_dht.start()

import services.email as emailService
thread_email = Thread(target=emailService.checkTemperatureSendEmail, name="emailService")
thread_email.start()