#!/bin/bash

# Script: scripts/reset-stack.sh
# Description: Safely tears down and brings up the full IoT monitoring stack

echo "🚧 Stopping existing containers (if running)..."
docker-compose down

echo "🧹 Cleaning up dangling volumes (optional)..."
# docker volume prune -f  # Uncomment only if you want to clear unused volumes

echo "🚀 Starting up the IoT monitoring stack..."
docker-compose up -d

echo "✅ Stack is now running. Access the services:"
echo "  - Node-RED:   http://localhost:1880"
echo "  - Mosquitto:  mqtt://localhost:1883"
echo "  - InfluxDB:   http://localhost:8086"
echo "  - Grafana:    http://localhost:3000"
