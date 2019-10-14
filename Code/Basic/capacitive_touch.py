# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Use the capacitive touch-enabled pins on the ESP32

# Notes: t.read() returns a smaller number when touched

from machine import TouchPad, Pin

t = TouchPad(Pin(2))
t.read()