import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(
    client_id = "humidity_pub_12028910", 
    callback_api_version=1)
client.connect("localhost", 1883, 60)

while True:
    hum = random.randint(30, 70)
    message = f"StudentID:12028910 | Humidity: {hum}%"
    client.publish("sensors/humidity", message)
    print("Published:", message)
    time.sleep(3)
