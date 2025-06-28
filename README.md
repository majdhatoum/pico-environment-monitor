# 🌡️ Pico Environment Monitor

This project demonstrates a complete IoT-based environmental monitoring system using a Raspberry Pi Pico W, DHT11 sensor, MQTT, Node-RED, InfluxDB, and Grafana — all orchestrated via Docker.

It continuously monitors:
- Temperature (°C)
- Humidity (%)
- Tilt status (shock/fall detection)

Data is:
- **Captured** by the Raspberry Pi Pico W
- **Published** to an MQTT broker (Mosquitto)
- **Processed and visualized** via Node-RED
- **Stored** in InfluxDB
- **Displayed** using Grafana dashboards

> This project follows the structure and expectations of the LNU IoT course. It aims to give hands-on experience with microcontrollers, MQTT communication, containerization, and time-series visualization.
