import RPi.GPIO as gp
import time
import matplotlib.pyplot as plt

# R_res = 1 MOm
# R_dump = 100 Om
# U_max = 3.3

#1.43

# gpio setup
leds = [21,20,16,12,7,8,25,24]
dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
gp.cleanup()
gp.setmode(gp.BCM)

gp.setmode(gp.BCM)
gp.setup(leds,gp.OUT,initial=gp.LOW)
gp.setup(dac,gp.OUT,initial=gp.LOW)
gp.setup(troyka,gp.OUT)
gp.setup(comp,gp.IN)

def binary(decimal):
    return[int(bit) for bit in bin(decimal)[2:].zfill(8)]

# adc script, returns curr voltage value
def adc():
    num = [0]*8
    for i in range(8):
        # print('binary ', str(num))
        num[i] = 1
        for j in range(8):
            gp.output(dac[j], num[j])
        time.sleep(0.0005)
        if gp.input(comp):
            num[i] = 0
        
    return ''.join(str(x) for x in num)


data = []
t1 = time.time() # in seconds


try:
    gp.output(13, 1)
    ascent_flag = True
    descent_flag = True
    # charging
    print("Charging... registering data")
    while ascent_flag:
        n = adc()
        curr_u = int(n, 2) / 255 * 3.3
        data += [curr_u]
        print(curr_u)
        
        if curr_u/3.3 >= 0.97:
            ascent_flag = False

    # discharging
    gp.output(13,0)
    print("Charging completed. Discharging...")
    while descent_flag:
        n = adc()
        curr_u = int(n, 2)/255*3.3
        data += [curr_u]
        print(curr_u)

        if curr_u/3.3 <= 0.02:
            descent_flag = False

    t2 = time.time()
    dt = t2-t1
    disFreq = len(data)/dt
    quantStep = 3.3/256
    print("Experiment completed")
    print('Experiment time:', str(t2-t1), 's')
    print('Discretization frequency:', str(disFreq))

        
finally:
    gp.output(troyka, 0)
    for led in dac:
        gp.output(led, 0)

    # writing in file
    # input values saving
    with open('7th lab/data.txt', 'w') as f:
        f.write(''.join(str(x)+'\n' for x in data))

    # calculated values saving
    with open("7th lab/settings.txt", 'w') as f:
        f.write(str(str(dt)+'\n'+str(disFreq)+'\n'+str(quantStep)))

    
