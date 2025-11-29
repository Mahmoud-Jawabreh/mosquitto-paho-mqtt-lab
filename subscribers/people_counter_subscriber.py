import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"[PEOPLE SUB] Received: {msg.payload.decode()}")

client = mqtt.Client(
    client_id = "people_sub_12028910", 
    callback_api_version=1)
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("sensors/people")

print("People Counter subscriber running...")
client.loop_forever()
