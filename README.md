# MQTT Lab: Mosquitto Broker + Paho Clients

### Student ID: **12028910**
### Course: Internet of Things

---

## 🟢 1. Mosquitto Installation (Server)
Mosquitto broker installed on Windows using the official installer:

- Path: `D:\Program Files\mosquitto`
- Running using Windows Service
- Verified listener on port **1883**

- 
Result shows Mosquitto is listening.

---

## 🟣 2. Paho MQTT (Python Clients)

Used Python 3.13 with `paho-mqtt` client library.

Install: pip install paho-mqtt


---

## 🟡 3. Publishers

Three publishers simulate real IoT sensor values:

- **Temperature** publisher (°C)
- **Humidity** publisher (%)
- **People Counter** (random counts)

Each publisher publishes messages including the **Student ID: 12028910**.

---

## 🔵 4. Subscribers

Three subscribers listen to:

- `iot/temperature`
- `iot/humidity`
- `iot/people_counter`

Each subscriber prints received messages.

---

## 📡 5. Results (Publishers & Subscribers)

Screenshots included in `/screenshots`:

- Mosquitto Broker running
- Publisher logs (sending data)
- Subscriber logs (receiving data)

---

## 📁 Project Structure

Mosquitto_paho_Lab/
publishers/
subscribers/
screenshots/
README.md


---

## ✔️ Conclusion

In this lab:
- Mosquitto MQTT broker was installed and configured.
- Three publishers sent data using Python + Paho.
- Three subscribers received data from specific topics.
- Full logs and screenshots included.
