# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Put the device to sleep for 10 seconds

# Notes: Calling deepsleep() without an argument will put the device to sleep indefinitely

import machine

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print("Wake up")

machine.deepsleep(10000)
