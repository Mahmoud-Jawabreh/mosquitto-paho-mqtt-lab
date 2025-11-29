import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(
    client_id = "temp_pub_12028910", 
    callback_api_version=1)
client.connect("localhost", 1883, 60)

while True:
    temp = round(random.uniform(20.0, 32.0), 2)  # realistic room temps
    message = f"StudentID:12028910 | Temperature: {temp}°C"
    client.publish("sensors/temperature", message)
    print("Published:", message)
    time.sleep(2)
