# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Create station interface, scan for acces points and connect to an AP

import Code.Basic.network
wlan = network.WLAN(network.STA_IF)
wlan.activate(True)
wlan.scan()
wlan.isconnected()
wlan.connect("essid", password)
wlan.config("mac")
wlan.ifconfig()

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ESP-AP")
