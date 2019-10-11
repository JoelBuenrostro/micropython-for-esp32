# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA
# Firmware: Micropython v1.11
# Board: NodeMCU-32s
# Purpose: Set SPI baudrate, polarity and phase on hardware SPI bus

# Notes: The hardware SPI is faster (up to 80Mhz), but only works on following pins: MISO is GPIO12
# MOSI is GPIO13, and SCK is GPIO14.

from machine import Pin, SPI

hspi = SPI(1, baudrate=80000000, polarity=0, phase=0)