# Potentiometer demo 1
# Kevin McAleer
# May 2021

from machine import ADC

pot = ADC(26)# the middle pin on the Potentiometer

while True:
    print("Value is:",pot.read_u16())
    