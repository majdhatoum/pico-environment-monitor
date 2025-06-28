#!/bin/bash
echo "Starting Mosquitto, InfluxDB, Grafana, and Node-RED containers..."
docker start mosquitto 
docker start influxdb
docker start grafana
docker start nodered
echo "All services started. Access via:"
echo "Node-RED  → http://localhost:1880"
echo "Grafana   → http://localhost:3000"
