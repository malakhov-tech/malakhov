import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

data = np.loadtxt('data.txt')
with open('settings.txt') as f:
    dt = float(f.readline())
    dU = float(f.readline())

t_ax = np.arange(0, dt*(len(data)), dt)
data = data * dU

t_charge = t_ax[np.argmax(data)]
t_discharge = t_ax[-1] - t_charge

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(16,10))
ax.plot(t_ax, data, label='V(t)', color='g', marker='.', markevery=10)
ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке', loc='left', wrap=True)

plt.ylabel('Напряжение, В')
plt.xlabel('Время, с')

plt.annotate('Время зарядки: ' + str(t_charge) + 'c \nВремя разрядки: ' + str(t_discharge), [8,2])

plt.xlim(0,12)
plt.ylim(0,2.9)

ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.grid(which='minor', axis='both', linestyle='--')
ax.grid(which='major', axis='both', linestyle='-')
ax.legend()
plt.show()
fig.savefig('graph.svg', dpi=400)