import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(
    client_id = "people_pub_12028910", 
    callback_api_version=1)
client.connect("localhost", 1883, 60)

while True:
    count = random.randint(0, 15)
    message = f"StudentID:12028910 | PeopleCount: {count}"
    client.publish("sensors/people", message)
    print("Published:", message)
    time.sleep(5)
