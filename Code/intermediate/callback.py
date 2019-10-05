# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA
# Firmware: Micropython v1.11
# Board: NodeMCU-32s

# Purpose: Define a simple callback function to handle the interrupt and assigning it to a type of 
# change on a specific pin.

from machine import Pin

def callback(p):
    print("Pin", p)

p0 = Pin(0, Pin.IN)
p0.irq(trigger=Pin.IRQ_FALLING, handler=callback)