# 🌡️ Pico Environment Monitor
*By Majd Fares Al Hatoum*

Monitor your surroundings in style!  
Ever wondered what’s happening in your room, lab, greenhouse, or secret basement lair when you’re not looking?

**Pico Environment Monitor** is a lightweight and extensible IoT system built with a Raspberry Pi Pico W, designed to measure environmental conditions (temperature, humidity, tilt) and visualize them in real-time using modern open-source tools like **MQTT**, **Node-RED**, **InfluxDB**, and **Grafana** all wrapped up in Docker for smooth sailing.

---

## What Does It Do?

This project continuously collects sensor data from your Raspberry Pi Pico W and sends it over Wi-Fi via MQTT to a backend stack that:

- **Processes data** in Node-RED with flow-based logic
- **Stores it** in InfluxDB (a time-series database)
- **Visualizes it** using beautiful Grafana dashboards
- Can also trigger alerts (e.g., overheating or tilting detected) -- **Only using LEDs -- Not Graphana** 

---

## Why Would You Want This?

Because real-world data is cool — and useful.

Use cases include:

- **Home plant monitoring** — See if your mini jungle is thriving or sweating.
- **Smart home logging** — Detect temperature or tilt-based anomalies (did someone shake the shelf again?!).
- **Lab data logging** — Track stable environments for sensitive experiments.
- **DIY makers & STEM education** — Learn IoT fundamentals using MicroPython and Docker.
- **Prototyping & Edge deployments** — Quickly test environment sensing for any embedded system.

---

## What Problem Does It Solve?

Setting up a full IoT pipeline often means wrestling with half-baked Python scripts, mystery dashboard tools, and fragile Wi-Fi setups. This project:

- ✅ Uses reliable, open protocols (MQTT, HTTP, JSON)
- ✅ Provides a **containerized backend** that just works with `docker compose up`
- ✅ Makes the hardware + software setup simple and reproducible
- ✅ Ships with a plug-and-play frontend (dashboard + flows pre-installed)
- ✅ Empowers **students, makers, and pros** alike to build, extend, and learn

---

## Technologies Used

- **MicroPython** on **Raspberry Pi Pico W**
- **DHT11** sensor + Tilt switch + LEDs
- **Eclipse Mosquitto** (MQTT broker)
- **Node-RED** for logic and routing
- **InfluxDB 1.8** for time-series storage
- **Grafana** for real-time dashboarding
- **Docker Compose** to make it all click together

---

Whether you’re an IoT hobbyist, a data visualization fan, or someone just trying to figure out why their room feels like a sauna 🌡️ — this project is a great place to start.

> This project follows the structure and expectations of the LNU IoT course. It aims to give hands-on experience with microcontrollers, MQTT communication, containerization, and time-series visualization.

## System Architecture

This project uses a modular IoT architecture to monitor environmental conditions such as temperature, humidity, and tilt using a Raspberry Pi Pico W and visualizes the data on a Grafana dashboard.

### Components Overview

- **Raspberry Pi Pico W**: Collects environmental data via DHT11 and tilt sensor.
- **MQTT (Mosquitto Broker)**: Transfers sensor data wirelessly to the server.
- **Node-RED**: Receives, parses, and forwards MQTT data.
- **InfluxDB**: Time-series database that stores the sensor data.
- **Grafana**: Visualizes data in an interactive dashboard.

### Data Flow

1. The Pico W reads data from sensors and publishes it to the MQTT topic `pico/data`.
2. Node-RED subscribes to this topic, formats the data, and forwards it to InfluxDB.
3. InfluxDB stores the timestamped data.
4. Grafana queries the data and presents it as time series charts.

### System Overview Diagram

![System Architecture](assets/system-architecture.png)

> This architecture ensures modularity, easy maintenance, and a real-time view of environmental metrics.

## Automation & Triggers

Even simple sensors can do cool things when you automate the response!

- **Tilt Detection**: When the device tilts (e.g. someone touches it), the tilt sensor reads `1`, and the green LED turns on.
- **Temperature Alert**: If temperature exceeds 35°C, the red alert LED switches on to visually warn the user.

> These basic triggers make it easy to prototype a smarter system. You could easily expand this to activate alarms, fans, or notifications using Node-RED.

## Why Wi-Fi?

We chose **Wi-Fi (802.11)** for a few important reasons:

- Easy to set up in a home/lab environment
- Supported natively by Raspberry Pi Pico W
- No need for a separate LoRa, Zigbee, or GSM module
- Powered continuously – so power-saving isn’t a top priority

> _Wi-Fi is great for short-range, continuous power use cases, but may not suit remote/low-power deployments (e.g., farms, forests, far-away fridges)._



## Hardware

### Required Components

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

### Wiring Diagram

The following table summarizes the wiring configuration used in this project:

| Pico W Pin | Connected To          | Description                  |
|------------|-----------------------|------------------------------|
| GP0        | DHT11 Data Pin        | Temperature & humidity input |
| GP2        | Tilt Sensor Signal Pin| Detects tilt                 |
| GP4        | LED 1 (status)        | Turns on if tilt is detected |
| GP6        | LED 2 (alert)         | Turns on if temperature > 35°C |

> **Note**: The DHT11 sensor requires a 10kΩ pull-up resistor between VCC and Data for reliable communication. Some modules already have this onboard.

### Cost Estimation
| Item                | Purpose                          | Approx. Cost |
|---------------------|----------------------------------|--------------|
| Raspberry Pi Pico W | Main controller + WiFi           | $6.00        |
| DHT11 Sensor        | Temperature + Humidity sensor    | $2.50        |
| Tilt Sensor (Ball)  | Detects orientation changes      | $1.00        |
| LEDs + Breadboard   | Alerts and prototyping           | $2.00        |
| Jumper Wires        | Connections                      | $1.00        |

**Total Estimated Cost: ~$12.50 USD**


---

### Power Supply

- The Raspberry Pi Pico W is powered via Micro USB.
- All sensors and LEDs are powered through the Pico W’s 3.3V and GND pins.

## Electrical Considerations

This project runs fully on the 3.3V logic level provided by the Raspberry Pi Pico W, which makes things delightfully simple:

- **DHT11**: Digital sensor powered at 3.3V. No resistor needed between data and VCC since it's already internally regulated.
- **Tilt Sensor**: Acts like a switch—open or closed circuit. No current limiting needed.
- **LEDs**: Connected directly with GPIO output using short wires. Since Pico’s GPIO outputs are current-limited and we're using short durations + low current LEDs, no resistor was needed in this prototyping phase.

> _Note: For production or permanent setups, you might consider adding resistors to prolong LED life and ensure precise logic levels._


### Hardware Assembly Image

![hardware](assets/hardware.jpeg)

> Above: A real-world image of the project hardware setup. The DHT11 sensor is connected on the left, and the tilt sensor at the bottom left. The Pico W sits at the center of the breadboard with the LEDs to the right.

## Software Setup

This section walks you through setting up the MicroPython code, installing dependencies, and launching all backend services using Docker Compose. But first, I will give you a quick overview of the MicroPython code:

### Code Insight: Sending Sensor Data via MQTT

Here’s the heart of the code that makes the magic happen:

```python
sensor.measure()
temp = sensor.temperature()
hum = sensor.humidity()
tilted = tilt.value()

# LED alerts
led.value(tilted)
alert_led.value(1 if temp > 35 else 0)

data = {
    "temp": temp,
    "hum": hum,
    "tilt": tilted
}

payload = ujson.dumps(data)
client.publish(mqtt_topic, payload)
```

**This block does several important things:**

- Reads sensor values (temperature, humidity, tilt)
- Lights up LEDs if the device is tilted or overheating
- Prepares the data as a JSON string
- Publishes it via MQTT to the `pico/data` topic, where Node-RED listens and forwards the data to InfluxDB

>  _The simplicity of this loop makes it easy to extend. Want to detect gas, motion, or cosmic rays? Just plug in a sensor and add its data to the payload. Easy peasy!_


### 1. Clone the Project

Start by cloning this repository directly, which includes all the required code and configurations:

```bash
git clone https://github.com/majdhatoum/pico-environment-monitor.git
cd pico-environment-monitor
```

This will give you access to:

- **The MicroPython code** for your Raspberry Pi Pico W  
- **Dockerized backend** (MQTT, Node-RED, InfluxDB, Grafana)  
- **Preconfigured Node-RED flows** and **Grafana dashboards**  

---

### 2. Configure MicroPython on Pico W

#### Flashing MicroPython (First Time Only)

1. Hold down the **BOOTSEL** button on the Raspberry Pi Pico W and connect it to your computer via USB.
2. It will appear as a **mass storage device**.
3. Download the latest `.uf2` firmware from the [official MicroPython website](https://micropython.org/download/rp2-pico-w/).
4. Drag and drop the `.uf2` file into the Pico’s USB drive.
5. The Pico will automatically reboot and is now ready for MicroPython development.

### 3. Thonny IDE Setup

1. Open **Thonny IDE**.

2. Navigate to:

```bash
Tools > Options > Interpreter
```

3. Set the interpreter to:
```bash
MicroPython (Raspberry Pi Pico W)
```

4. Open the following file from the cloned repository:
```bash
pico/main.py
```


✅ You do **not** need to write the code manually — the script is already included.

---

### 4. Edit Wi-Fi and MQTT Credentials

In `main.py`, update the following lines to match your network environment:

```python
# Replace these with your actual Wi-Fi and MQTT settings
ssid = 'your-wifi-ssid'
password = 'your-wifi-password'
mqtt_server = 'your-mqtt-broker-ip'
```

**mqtt_server** should point to the host machine’s local IP address, e.g., `192.168.1.20`.

---

### 5. Auto-Start on Boot

Once saved as `main.py`, the script will **automatically run** every time the Raspberry Pi Pico W is **powered on or reset**.


## Docker-Based Backend Setup

This project comes with a pre-configured `docker-compose.yml` file that sets up the entire backend system, including:

- **Mosquitto** (MQTT Broker)
- **Node-RED** (Logic Flow Editor)
- **InfluxDB** (Time-Series Database)
- **Grafana** (Visualization Dashboard)

---

### Requirements

Make sure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

You can verify the installation with:

```bash
docker --version
docker-compose --version
```

### Launch the Stack

Navigate to the project root directory (where `docker-compose.yml` is located), then start all services with:
```bash
docker compose up -d
```
This will:

- Start **Mosquitto** on port `1883`
- Start **Node-RED** on port `1880`
- Start **InfluxDB** on port `8086`
- Start **Grafana** on port `3000`

You can verify everything is running using:
```bash
docker ps
```

---

### Shutdown and Resume Later

To safely stop the stack, run:
```bash
docker compose down
```

To resume later:

```bash
docker compose up -d
```

Your data will be persisted in the project folder under:

- `./mosquitto/`
- `./nodered-data/`
- `./influxdb-data/`
- `./grafana-data/`

## Accessing and Using the Dashboard

Once your stack is up and running, you can start monitoring real-time sensor data.
> Do not forget to Run your Thonny code. If all is well You should be seeing something like: **Publishing: {"hum": 10, "tilt": 0, "temp": 28}** updating constantly!

### 1. Access Node-RED
- Open your browser and go to: `http://localhost:1880`
- You’ll see the Node-RED flow editor interface.
- You can view or modify the pre-configured flow that:
  - Subscribes to MQTT data on topic `pico/data`
  - Parses the incoming JSON payload
  - Sends it to InfluxDB for storage

You can also monitor incoming messages via **Debug** nodes in real-time.

> If you make changes, click **Deploy** in the top right to apply them.

---

### 2. Access Grafana Dashboard

- Navigate to: `http://localhost:3000`
- Default credentials:
  - **Username:** `admin`
  - **Password:** `admin`
- You’ll be prompted to change the password on first login.

Once logged in:

- Go to **Dashboards > Manage**
- Load the pre-imported dashboard titled: `Pico Environment Monitor`
- You will see live graphs for:
  - 🌡 Temperature
  - 💧 Humidity
  - 📦 Tilt status
 
### 3. A peak of what you should be expeting to see on the board! 



## Final Thoughts & Reflections

Building this little IoT buddy was quite the ride — a mix of blinking LEDs, flashing firmware, and some MQTT magic.

What started as a simple idea ("let’s measure room temperature") turned into a full-stack edge-to-cloud setup featuring:
- A Raspberry Pi Pico W bravely gathering environmental data
- A DHT11 and tilt sensor doing their silent jobs
- Docker spinning up powerful backend services
- Grafana dashboards making things look *way* cooler than spreadsheets ever could

### What Went Well
- The whole thing runs beautifully offline — no subscriptions, no clouds, just pure LAN-powered glory.
- I learned many new things!
- Thanks to Docker, the backend is reproducible and easy to redeploy.
- The circuit is minimal and works reliably even after unplug-replug cycles.
- Node-RED and Grafana? A dream team for automation and dashboards.

### What I’d Do Differently Next Time
- Use a better temperature/humidity sensor like the DHT22 or BME280 for improved accuracy.
- Make alerts on Graphana
- Use more sensors
- Add secure authentication to MQTT and Grafana for production-readiness.
- Maybe wrap the breadboard into a small enclosure to avoid accidental wire yanks (we’ve all been there).

### AND this leads me to the next question: 

### Future Extensions
This project is just getting warmed up (pun intended). Here are a few directions you could explore:
- **Remote access:** Add port forwarding or secure tunneling with [ngrok](https://ngrok.com/) to monitor your dashboard from anywhere in the world.
- **Weather API comparison:** Pull real-time weather data from OpenWeatherMap and compare it with your sensor readings.
- **Historical analytics:** Configure InfluxDB retention policies and build time-based comparisons like “Yesterday vs Today” trends.
- **More sensors:** Add air quality, light, or motion sensors to turn this into a full environmental monitoring station.


### However, Could This Be a Real Product?
Absolutely. Could be a thing for small offices, greenhouses, server rooms, or anyone who talks to their houseplants and wants to back it up with data.

And the best part? Once it’s configured, it just works — no fiddling, no fluff.

That’s a wrap! Hope you enjoyed building and learning with this project as much as I did. 🌿📡



