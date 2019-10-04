# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA
# Firmware: Micropython v1.11
# Board: NodeMCU-32s

# Purpose: Puts a pin in high state for a second and in low state for a second while the condition
# is true

# Notes: If you need to stop a program that's running on the board just connect to the REPL and
# press Ctrl-c

from machine import Pin
import time

led = Pin(2, Pin.OUT)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
