import RPi.GPIO as gp
import time

def dec2bin(num):
    return [int(bit) for bit in bin(int(num))[2:].zfill(8)]

def adc():
    k = 0
    for i in range(0, 255):
        k+=1
        num = dec2bin(i)
        # print('binar ', str(num))
        for j in range(len(num)):
            gp.output(dac[j], num[j])
        if gp.input(comp):
            # print('total iters '+str(k))
            return i
    return 255
    


dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
gp.cleanup()
gp.setmode(gp.BCM)

gp.setup(comp, gp.IN)
gp.setup(troyka, gp.OUT, initial=gp.HIGH)

u_max = 3.3


for led in dac:
    gp.setup(led, gp.OUT)

for led in dac:
    gp.output(led, 0)


try:
    while True:
        n = adc()
        print(n, n*3.3/255)

        for led in dac:
            gp.output(led, 0)
        # time.sleep(0.3)

        
finally:
    gp.output(troyka, 0)
    for led in dac:
        gp.output(led, 0)



