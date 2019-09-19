# Chip: ESP32-WROOM-32 (ESP32-D0WDQ6)
# Microprocessor: Dual-Core Xtensa® 32-bit LX6
# Clock: 80MHz to 240Mhz
# Crystal: 40MHz
# SPÍ flash: 4 MB
# Operating voltage: 3.0V-3.6V
# Operating current: 80mA

# Purpose: Create a PWM object from a pin, set frequency and duty cycle

from machine import Pin, PWM

pwm0 = PWM(Pin(0))
pwm0.freq()
pwm0.freq(1000)
pwm0.duty()
pwm0.duty(200)
pwm0.deinit()

pwm2 = PWM(Pin(2), freq=500, duty=512)
