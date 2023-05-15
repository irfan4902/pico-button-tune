import machine
import utime

from pitches import *

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

buzzer = machine.PWM(machine.Pin(18))

tune = # Create your own tune here!

while True:
    if button.value() == 1:
        for t in tune:
            if t == 0:
                # set volume to 0 
                buzzer.duty_u16(0)           
            else:
                buzzer.freq(t)                
                buzzer.duty_u16(3000)      
            utime.sleep(0.15)
