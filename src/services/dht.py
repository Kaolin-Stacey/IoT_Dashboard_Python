import services.Freenove_DHT as DHT
from time import sleep

import config

DHTPin = 21

dht = DHT.DHT(DHTPin)

def getData():
    while(True):
        config.temperatureVal, config.humidityVal = getDHT()
        # print(config.temperatureVal, config.humidityVal)
        sleep(0.1)

def getDHT():
    for i in range (1,15):
        chk = dht.readDHT11()
        if (chk == dht.DHTLIB_OK):
            break
        sleep(0.1)
    return dht.temperature, dht.humidity