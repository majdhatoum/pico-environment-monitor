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

## ✅ Step 3: Hardware

### 🧰 Required Components

To build the Raspberry Pi Pico W - Environment Monitor, the following hardware components are used:

| Component               | Description                                                        |
|-------------------------|--------------------------------------------------------------------|
| Raspberry Pi Pico W     | Main microcontroller board with Wi-Fi support                     |
| DHT11 Temperature Sensor| Measures temperature and humidity                                  |
| Tilt Sensor (e.g., SW-520D or similar) | Detects tilt or vibration                                   |
| Breadboard              | For quick and solderless circuit prototyping                      |
| Jumper Wires (Male-Male)| To connect components on the breadboard                           |
| LED (x2)                | Visual indicators: one for tilt status and another for overheat   |
| 330Ω Resistors (x2)     | Current limiting resistors for the LEDs                           |
| Micro USB cable         | For powering and programming the Raspberry Pi Pico W              |

---

### ⚡ Wiring Diagram

The following table summarizes the wiring configuration used in this project:

| Pico W Pin | Connected To          | Description                  |
|------------|-----------------------|------------------------------|
| GP0        | DHT11 Data Pin        | Temperature & humidity input |
| GP2        | Tilt Sensor Signal Pin| Detects tilt                 |
| GP4        | LED 1 (status)        | Turns on if tilt is detected |
| GP6        | LED 2 (alert)         | Turns on if temperature > 35°C |

> 📌 **Note**: The DHT11 sensor requires a 10kΩ pull-up resistor between VCC and Data for reliable communication. Some modules already have this onboard.

---

### 🔌 Power Supply

- The Raspberry Pi Pico W is powered via Micro USB.
- All sensors and LEDs are powered through the Pico W’s 3.3V and GND pins.

---

### 📷 Hardware Assembly Image

![hardware](assets/hardware.png)

