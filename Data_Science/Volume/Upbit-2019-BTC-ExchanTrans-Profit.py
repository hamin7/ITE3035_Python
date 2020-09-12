# Upbit 2019 BTC 거래소 거래량 - 수익
import numpy as np
import matplotlib.pyplot as plt

x = ['Feb','May','Jun','Jul']
y1 = [607511668110,3152608439400,4490686502000,6224665445580]
y2 = [-135473,1728400,1513153,-2666093]
# y3 = data_set['data3']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# plot with properties

line1 = ax1.plot(np.arange(len(x)), y1, color='b', linestyle='--', marker='o', label='Upbit Volume')
line2 = ax2.plot(np.arange(len(x)), y2, color='g', linestyle='--', marker='^', label='Profit')
# line3 = ax2.plot(np.arange(len(x)), y3, color='r', linestyle='--', marker='s', label=title[3])

# plot without x sorting
ax1.set_xticklabels(['$Jan$','$Feb$','','$May$','','$Jun$','','$Jul$'])
ax1.set_xlabel('Month')
ax1.set_ylabel('Upbit Exchange Trans Volume(1,000,000,000,000KRW)')
ax2.set_ylabel('Profit(1,000,000KRW)')

# set y limit
ax1.set_ylim(0, 7000000000000)
ax2.set_ylim(-3000000, 5000000)

# plot legend for all y axis
lines = line1 + line2
labels = [l.get_label() for l in lines]
plt.legend(lines, labels, loc=2)

plt.grid(True)

# fig.grid(False)

fig.tight_layout()
fig.savefig('Upbit-2019-BTC-UppitVolume-profit.png', dpi=1000)
# fig.savefig('Upbit-BTC2018-UpbutVolume-profit.eps', format='eps', dpi=1000)
plt.show()
