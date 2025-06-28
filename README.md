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

## System Architecture

This project uses a modular IoT architecture to monitor environmental conditions such as temperature, humidity, and tilt using a Raspberry Pi Pico W and visualizes the data on a Grafana dashboard.

### 📦 Components Overview

- **Raspberry Pi Pico W**: Collects environmental data via DHT11 and tilt sensor.
- **MQTT (Mosquitto Broker)**: Transfers sensor data wirelessly to the server.
- **Node-RED**: Receives, parses, and forwards MQTT data.
- **InfluxDB**: Time-series database that stores the sensor data.
- **Grafana**: Visualizes data in an interactive dashboard.

### 🔁 Data Flow

1. The Pico W reads data from sensors and publishes it to the MQTT topic `pico/data`.
2. Node-RED subscribes to this topic, formats the data, and forwards it to InfluxDB.
3. InfluxDB stores the timestamped data.
4. Grafana queries the data and presents it as time series charts.

### 🗂 Diagram

![System Architecture](assets/system-architecture.png)

> This architecture ensures modularity, easy maintenance, and a real-time view of environmental metrics.
