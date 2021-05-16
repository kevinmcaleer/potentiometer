# Potentiometer demo
# Kevin McAleer
# May 2021

from machine import Pin, ADC, PWM

pot = ADC(26)# the middle pin on the Potentiometer
led = PWM(Pin(15))
led.freq(1000)

while True:
    print("Value is:",pot.read_u16())
    led.duty_u16(pot.read_u16())

