# Potentiometer demo
# Kevin McAleer
# May 2021

from machine import Pin, ADC, PWM

pot = ADC(26)# the middle pin on the Potentiometer
led = PWM(Pin(15))
led.freq(1000)

def map(x, in_min, in_max, out_min, out_max):
    """ Maps two ranges together """
    return int((x-in_min) * (out_max-out_min) / (in_max - in_min) + out_min)

while True:
    # print("Value is:",pot.read_u16())
    led.duty_u16(pot.read_u16())

    pot_value = pot.read_u16()
    percentage = map(pot_value,288, 65535,0,100)
    print("Percentage:", percentage, "Raw, ", pot_value)
