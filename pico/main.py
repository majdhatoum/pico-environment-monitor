import network
import time
import ujson
from machine import Pin
import dht
from umqtt.simple import MQTTClient

# Wi-Fi credentials
ssid = 'dany'
password = 'dany2009'

# MQTT Broker settings
mqtt_server = '192.168.1.20'
mqtt_topic = b'pico/data'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while not wlan.isconnected():
    print("Connecting to Wi-Fi...")
    time.sleep(1)
print("Connected on:", wlan.ifconfig()[0])

# Initialize sensor and LEDs
sensor = dht.DHT11(Pin(0))
tilt = Pin(2, Pin.IN)
led = Pin(4, Pin.OUT)
alert_led = Pin(6, Pin.OUT)

# Setup MQTT client
client_id = "pico-sensor"
client = MQTTClient(client_id, mqtt_server)
client.connect()
client.publish(mqtt_topic, b"", retain=True)  # Clear retained
print("MQTT Connected to", mqtt_server)

# Publish loop
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        tilted = tilt.value()

        # LED alerts
        led.value(tilted)
        alert_led.value(1 if temp > 35 else 0)

        # Prepare payload
        data = {
            "temp": temp,
            "hum": hum,
            "tilt": tilted
        }

        payload = ujson.dumps(data)
        print("Publishing:", payload)
        client.publish(mqtt_topic, payload)

    except Exception as e:
        print("Error:", e)

    time.sleep(5)

