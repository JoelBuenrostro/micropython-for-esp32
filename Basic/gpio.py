# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: 2 Cores low-power Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Create output pin on GPIO32 and a input pin on GPIO33 and enable internal pull.up resistor 
# on GPIO25.

# Notes: For mapping between board logical pins and physical chip pins consult your board 
# documentation.

from machine import Pin

p7 = Pin(32, Pin.OUT)
p7.on()
p7.off()
p7.value(1)

p8 = Pin(33, Pin.IN)
print(p8.value())

p9 = Pin(25, Pin.IN, Pin.PULL_UP)