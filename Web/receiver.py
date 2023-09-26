import paho.mqtt.client as mqtt

# MQTT broker config
broker_address = "localhost"
port = 1883
topic = "your/topic"

def on_connect(client, userdata, flags, rc):
    print("Connected with code: " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print("Received message:" + str(msg.payload))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port, 60)
client.loop_forever()
