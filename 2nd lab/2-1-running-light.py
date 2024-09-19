import RPi.GPIO as gp
import time

def blink(led):
    gp.output(led, 1)
    time.sleep(0.2)
    gp.output(led, 0)


gp.cleanup()
gp.setmode(gp.BCM)
leds = [2,3,4,17,27,22,10,9]

for led in leds:
    gp.setup(led, gp.OUT)


for i in range(4):
    for led in leds:
        blink(led)

for led in leds:
    gp.output(led, 0)