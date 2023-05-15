import machine
import utime

from pitches import *

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

buzzer = machine.PWM(machine.Pin(18))

tune = [E7, E7, 0, E7, 0, C7, E7, 0, G7, 0, 0, 0, G6, 0, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0]

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
