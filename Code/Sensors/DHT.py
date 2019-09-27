# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Read temperature and humidity from DHT sensors
# Notes: The DHT driver is implemented in software and works on all pins

import dht
import machine

d = dht.DHT11(machine.Pin(4))
d.measure()
d.temperature()
d.humidity()

d = dht.DHT22(machine.Pin(4))
d.measure()
d.temperature()
d.humidity()