import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(26, gp.OUT)
gp.setup(16, gp.IN)


gp.output(26,0)