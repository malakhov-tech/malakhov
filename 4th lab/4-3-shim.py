import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(24, gp.OUT)

try:
    pmw = gp.PWM(24, 1000)
    while True:
        duty = int(input())
        pmw.start(duty)
finally:
    gp.cleanup()