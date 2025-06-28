#!/bin/bash
echo "Stopping Mosquitto, Node-RED, InfluxDB, and Grafana containers..."
docker stop mosquitto   
docker stop nodered
docker stop influxdb
docker stop grafana
echo "All services stopped safely."