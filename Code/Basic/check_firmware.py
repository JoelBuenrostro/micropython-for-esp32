# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Check the firmware integrity from a MicroPython REPL prompt

# Notes: If the last output value is True, the firmware is OK. Otherwise, it’s corrupted and need 
# to be reflashed correctly.

import esp

esp.check_fw()