import RPi.GPIO as gp
import time

gp.cleanup()
gp.setmode(gp.BCM)
leds = [2,3,4,17,27,22,10,9]
aux = [21,20,26,16,19,25,23,24]

for led in leds:
    gp.setup(led, gp.OUT)
    gp.output(led, 0)

for au in aux:
    gp.setup(au, gp.IN)

while True:
    for i in range(len(aux)):
        if gp.input(aux[i]):
            gp.output(leds[i],1)
        else:
            gp.output(leds[i],0)
    time.sleep(0.05)
