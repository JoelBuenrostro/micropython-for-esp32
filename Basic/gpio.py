# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: 2 Cores low-power Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Create output pin on GPIO0 and a input pin on GPIO2 and enable internal pull.up resistor 
# on GPIO4.

# Notes: For mapping between board logical pins and physical chip pins consult your board 
# documentation.

from machine import Pin

p0 = Pin(0, Pin.OUT)
p0.on()
p0.off()
p0.value(1)

p2 = Pin(2, Pin.IN)
print(p2.value())

p4 = Pin(4, Pin.IN, Pin.PULL_UP)