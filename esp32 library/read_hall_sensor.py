# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Read the internal hall sensor.

# Notes: the temperature sensor in the ESP32 will typically read higher than ambient due to the IC
# getting warm while it runs.

import esp32

esp32.hall_sensor()
esp32.raw_temperature()
