import RPi.GPIO as gp

dac = [8,11,7,1,0,5,12,6]
num = list(bin(int(input())))[2::]
num = [0]*(8-len(num))+num
print(num)
gp.cleanup()
gp.setmode(gp.BCM)


for led in dac:
    gp.setup(led, gp.OUT)

for led in dac:
    gp.output(led, 0)


for i in range(len(dac)):
    gp.output(dac[i], int(num[i]))
