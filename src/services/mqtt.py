import paho.mqtt.client as mqtt

def on_connect_light(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("IoTProject/light_level")

def on_message_light(client, userdata, msg):
    import config
    msg.payload = msg.payload.decode("utf-8")
    config.lightVal = int(str(msg.payload))

light_client = mqtt.Client()
light_client.on_connect = on_connect_light
light_client.on_message = on_message_light

light_client.connect_async("localhost",1883,60)
light_client.loop_start()



def on_connect_rfid(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("IoTProject/rfid_tag")

def on_message_rfid(client, userdata, msg):
    import db
    msg.payload = msg.payload.decode("utf-8")
    db.getUserByRFID(str(msg.payload))

rfid_client = mqtt.Client()
rfid_client.on_connect = on_connect_light
rfid_client.on_message = on_message_light

rfid_client.connect_async("localhost",1883,60)
rfid_client.loop_start()

