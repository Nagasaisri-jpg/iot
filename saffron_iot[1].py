import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

# Sensor & Actuator Pins
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
LIGHT_SENSOR = 17
CO2_SENSOR = 27
TDS_SENSOR = 22
PH_SENSOR = 10
HUMIDIFIER = 5
GROW_LIGHTS = 6
PELTIER_MODULE = 13
PUMP_ACID = 19
PUMP_BASE = 26
PUMP_NUTRIENT_1 = 20
PUMP_NUTRIENT_2 = 21
PUMP_CIRCULATION = 16

# Telegram Bot Setup
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_telegram_message(message):
    bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
    bot.sendMessage(CHAT_ID, message)

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([HUMIDIFIER, GROW_LIGHTS, PELTIER_MODULE, PUMP_ACID, PUMP_BASE, PUMP_NUTRIENT_1, PUMP_NUTRIENT_2, PUMP_CIRCULATION], GPIO.OUT)
GPIO.setup([LIGHT_SENSOR, CO2_SENSOR, TDS_SENSOR, PH_SENSOR], GPIO.IN)

def read_sensors():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    light_level = GPIO.input(LIGHT_SENSOR)
    co2_level = GPIO.input(CO2_SENSOR)
    tds_value = GPIO.input(TDS_SENSOR)
    ph_value = GPIO.input(PH_SENSOR)
    
    return temperature, humidity, light_level, co2_level, tds_value, ph_value

def control_actuators(temp, humidity, light_level):
    if humidity < 50:
        GPIO.output(HUMIDIFIER, GPIO.HIGH)
    else:
        GPIO.output(HUMIDIFIER, GPIO.LOW)

    if light_level < 1:
        GPIO.output(GROW_LIGHTS, GPIO.HIGH)
    else:
        GPIO.output(GROW_LIGHTS, GPIO.LOW)

    if temp < 15:
        GPIO.output(PELTIER_MODULE, GPIO.HIGH)
    else:
        GPIO.output(PELTIER_MODULE, GPIO.LOW)

def main():
    while True:
        temp, humidity, light, co2, tds, ph = read_sensors()
        control_actuators(temp, humidity, light)

        message = f"Temp: {temp}°C, Humidity: {humidity}%, Light: {light}, CO2: {co2}, TDS: {tds}, pH: {ph}"
        print(message)
        send_telegram_message(message)

        time.sleep(60)

try:
    send_telegram_message("Raspberry Pi Saffron IoT System Started!")
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    send_telegram_message("System Shutdown!")
