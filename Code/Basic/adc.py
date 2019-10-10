# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA
# Firmware: Micropython v1.11
# Board: NodeMCU-32s

# Purpose: Create ADC object on ADC pin and read a value between 0-1024

from machine import ADC

adc = ADC(0)
adc.read()
