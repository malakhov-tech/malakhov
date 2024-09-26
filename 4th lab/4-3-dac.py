import RPi.GPIO as gp

def dec2bin(num):
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
    while True:
        usr_inp = input("Gimme your numba: ")
        if usr_inp == 'q': break
        print(usr_inp)

        # if usr_inp[:-1].isdigit():
        #     print("Error: not only numbers are present in input")
        #     continue
        if float(usr_inp) % 1 != 0:
            print("Warning: input value is not integer")

        usr_inp = int(usr_inp) * 255 / 100


        if usr_inp > 255:
            print("Error: input value is bigger than allowed!")
            continue
        if usr_inp < 0:
            print("Error: input value is lower than allowed!")
            continue
        

        print("Expected voltage: " + str(u_max / 255 * usr_inp))

        num = dec2bin(usr_inp)
        for i in range(len(num)):
            gp.output(dac[i], num[i])
finally:
    for led in dac:
        gp.output(led, 0)



