# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Create an I2C bus, read 4 bytes from slave device, write "12" to slave device
# Create a buffer with 10 bytes, write the given buffer to the slave

from machine import Pin, I2C

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

i2c.readfrom(0x3a, 4)
i2c.writeto(0x3a, "12")

buf = bytearray(10)
i2c.writeto(0x3a, buf)
