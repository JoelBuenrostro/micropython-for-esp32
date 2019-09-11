# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: 2 Cores low-power Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: It puts a pin in high state for a second and in low state for a second in each iteration

from machine import Pin
import time

p0 = Pin(0, Pin.OUT)

for i in range(10):
    p0.on()
    time.sleep(1)
    p0.off()
    time.sleep(1)
