import paho.mqtt.client as mqtt
from time import sleep

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("IoTProject/light_level")

def on_message(client, userdata, msg):
    import config
    msg.payload = msg.payload.decode("utf-8")
    config.lightVal = int(str(msg.payload))

light_client = mqtt.Client()
light_client.on_connect = on_connect
light_client.on_message = on_message

light_client.connect_async("localhost",1883,60)
light_client.loop_start()