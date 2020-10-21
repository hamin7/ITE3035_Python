# 종가 - 수익
import numpy as np
import matplotlib.pyplot as plt

x = ['Feb','Mar','Apr','May','Jun','Jul','Aug']
y1 = [76615774359,121327294696,91245444410,73256553726,25829874334,23244686413,11979435513]
y2 = [1.25,3.01,2.39,3.85,2.97,2.59,0.64]
# y3 = data_set['data3']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# plot with properties

line1 = ax1.plot(np.arange(len(x)), y1, color='b', linestyle='--', marker='o', label='Bithumb Exchange Volume')
line2 = ax2.plot(np.arange(len(x)), y2, color='g', linestyle='--', marker='^', label='Transaction Percentage')
# line3 = ax2.plot(np.arange(len(x)), y3, color='r', linestyle='--', marker='s', label=title[3])

# plot without x sorting
ax1.set_xticklabels(['$Jan$','$Feb$','$Mar$','$Apr$','$May$','$Jun$','$Jul$','$Aug$'])
ax1.set_xlabel('Month')
ax1.set_ylabel('Volume(100,000,000,000KRW)')
ax2.set_ylabel('Transaction Percentage(%)')

# set y limit
ax1.set_ylim(0, 130000000000)
ax2.set_ylim(0, 5.0)

# plot legend for all y axis
lines = line1 + line2
labels = [l.get_label() for l in lines]
plt.legend(lines, labels, loc=2)

plt.grid(True)

# fig.grid(False)

fig.tight_layout()
fig.savefig('Bithumb-BTC2018-volume-trans.png', dpi=1000)
fig.savefig('Bithumb-BTC2018-volume-trans.eps', format='eps', dpi=1000)
plt.show()
