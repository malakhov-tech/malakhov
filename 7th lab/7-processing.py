import matplotlib.pyplot as plt

with open('7th lab/data.txt') as f:
    a = [float(x) for x in f.readlines()]

with open('7th lab/settings.txt') as f:
    dt, disFreq, quantStep = [float(x) for x in f.readlines()]

plt.plot(a)
print('dt: ' + str(dt) + ' s')
print('T of one probe: ' + str(1/disFreq) + ' s')
print('Discretization frequency: ' + str(disFreq) + ' 1/s')
print('Quant step: ' + str(quantStep) + ' V')
plt.show()