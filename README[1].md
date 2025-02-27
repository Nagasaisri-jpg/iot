# Saffron IoT System

This project automates saffron cultivation using Raspberry Pi 4 with Mycodo for real-time monitoring and control.

## Features
- **Sensor Monitoring**: Temperature, Humidity, CO₂, TDS, pH, Light
- **Actuator Control**: Humidifier, Grow Lights, Peltier Module, Pumps
- **Automation with Mycodo**: Scheduled nutrient dosing, climate control
- **Live Monitoring**: Raspberry Pi Camera integration
- **Alerts**: Telegram notifications for critical values

## Setup Instructions
1. Install Mycodo on Raspberry Pi.
2. Connect sensors and actuators as per the circuit diagram.
3. Upload and run the Python scripts.
4. Configure Mycodo automation for saffron's growth cycles.

## Dependencies
Install required packages using:
```
pip install -r requirements.txt
```
