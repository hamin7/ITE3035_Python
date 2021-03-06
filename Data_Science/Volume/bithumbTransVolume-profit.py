# 거래소 거래량 - 수익
import numpy as np
import matplotlib.pyplot as plt

x = ['Feb','Mar','Apr','May','Jun','Jul']
y1 = [6129825220000,4028287160000,3816150800000,1903469920000,869387920000,897958000000]
y2 = [20057445,8951034,23967448,11999306,4513842,494149]
# y3 = data_set['data3']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# plot with properties

line1 = ax1.plot(np.arange(len(x)), y1, color='b', linestyle='--', marker='o', label='Bithumb Volume')
line2 = ax2.plot(np.arange(len(x)), y2, color='g', linestyle='--', marker='^', label='Profit')
# line3 = ax2.plot(np.arange(len(x)), y3, color='r', linestyle='--', marker='s', label=title[3])

# plot without x sorting
ax1.set_xticklabels(['$Jan$','$Feb$','$Mar$','$Apr$','$May$','$Jun$','$Jul$','$Aug$'])
ax1.set_xlabel('Month')
ax1.set_ylabel('Bithumb Trans Volume(1,000,000,000,000KRW)')
ax2.set_ylabel('Profit(10,000,000KRW)')

# set y limit
ax1.set_ylim(0, 10000000000000)
ax2.set_ylim(0, 25000000)

# plot legend for all y axis
lines = line1 + line2
labels = [l.get_label() for l in lines]
plt.legend(lines, labels, loc=2)

plt.grid(True)

# fig.grid(False)

fig.tight_layout()
fig.savefig('Bithumb-BTC2018-bithumbVolume-profit.png', dpi=1000)
fig.savefig('Bithumb-BTC2018-bithumbVolume-profit.eps', format='eps', dpi=1000)
plt.show()
