import RPi.GPIO as gp
import time

def dec2bin(num):
    num = int(num)
    return [int(bit) for bit in bin(int(num))[2:].zfill(8)]


dac = [8,11,7,1,0,5,12,6]
gp.cleanup()
gp.setmode(gp.BCM)

u_max = 3.3


for led in dac:
    gp.setup(led, gp.OUT)

for led in dac:
    gp.output(led, 0)

try:
    usr_inp = input("Gimme your max voltaga: ")
    usr_inp = float(usr_inp)

    sampling = float(input("Enter sampling:"))
    period = float(input("Enter period: ")) # how many seconds does one sampling have
    
    # max_led = min(usr_inp / u_max * 255, 255)
    while True:
        for i in range(0, 256, int(sampling/period*255*2)):
            curr_led_out = dec2bin(i)
            for j in range(len(curr_led_out)):
                gp.output(dac[j], curr_led_out[j])
            print("current voltage: "+ str(usr_inp / 255 * i))
            time.sleep(sampling)
        
        for i in range(255, -1, -int(sampling/period*255*2)):
            curr_led_out = dec2bin(i)
            
            for j in range(len(curr_led_out)):
                gp.output(dac[j], curr_led_out[j])
            print("current voltage: "+ str(usr_inp / 255 * i))
            time.sleep(sampling)


        
finally:
    for led in dac:
        gp.output(led, 0)