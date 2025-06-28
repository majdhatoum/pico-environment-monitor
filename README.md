# Raspberry Pi Pico W – Environment Monitor

This project collects temperature, humidity, and tilt data from a DHT11 sensor connected to a Raspberry Pi Pico W and visualizes it using Grafana.

## Stack

- **MicroPython** (Pico W firmware)
- **MQTT** (Mosquitto)
- **Node-RED** (for message routing & formatting)
- **InfluxDB v1.8** (for time-series storage)
- **Grafana** (for data visualization)
- **Docker Compose** (for container orchestration)

## Live Metrics

- Temperature (°C)
- Humidity (%)
- Tilt status (0 = Flat, 1 = Tilted)

## Setup

1. Flash the Pico W with MicroPython.
2. Upload the sensor script via Thonny.
3. Run `docker-compose up -d` to start services.
4. Open Node-RED at `http://localhost:1880`.
5. Open Grafana at `http://localhost:3000` and import the pre-made dashboard.

## Folder Structure

