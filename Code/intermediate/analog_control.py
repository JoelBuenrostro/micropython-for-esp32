# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Control a LED with potentiometer

import machine
import utime
import sys

Led = machine.Pin(2, machine.Pin.OUT)
Button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
ADCpin = machine.ADC(0)
PWM = PWM(Pin(2))

while True:
    if Button.value() == 0:
        sys.exit()

AnalogValue = adc.read()
AnalogValue = AnalogValue * (3.3 / 4095)
pwm.duty(AnalogValue)
utime.sleep_ms(2)