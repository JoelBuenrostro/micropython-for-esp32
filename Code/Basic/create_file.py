# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Create a file stored in the flash

# Notes: If your devices has 1Mbyte or more of storage then it will be set up (upon first boot) to
# contain a filesystem. This filesystem uses the FAT format and is stored in the flash after the
# MicroPython firmware.

f = open("data.txt", "w")
f.write("data")
f.close()
