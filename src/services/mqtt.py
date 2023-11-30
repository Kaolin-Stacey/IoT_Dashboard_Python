import paho.mqtt.client as mqtt
import services.db as db

def on_connect(client, userdata, flags, rc):
    print("Connected MQTT with result code "+str(rc))
    client.subscribe("IoT/lumens")
    client.subscribe("IoT/rfid")

def on_message(client, userdata, msg):
    # import config
    topic = msg.topic
    message = msg.payload.decode("utf-8")
    # print("Topic: " + topic)
    # print("Message: " + message)
    if (topic == "IoT/lumens"):
        # print("Received message for lumens: " + message)
        import config
        config.lightVal = int(message)
    if (topic == "IoT/rfid"):
        # print("Received message for rfid: " + message)
        import config
        user = db.getUserByRFID(message.upper())
        config.current_user = user.name
        config.temperatureThreshold = user.temp_threshold
        config.humidityThreshold = user.humidity_threshold
        config.lightThreshold = user.light_threshold

    # config.lightVal = int(str(msg.payload))

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect_async("localhost",1883,60)
mqtt_client.loop_start()