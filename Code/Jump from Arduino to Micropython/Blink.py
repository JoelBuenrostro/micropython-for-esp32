# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA
# Firmware: Micropython v1.11
# Board: NodeMCU-32s

# Purpose: Turns an LED on for one second, then off for one second, repeatedly.

from machine import Pin
import utime

led = Pin(2, Pin.OUT)

while True:
    led.on()
    utime.sleep(1)
    led.off()
    utime.sleep(1)
