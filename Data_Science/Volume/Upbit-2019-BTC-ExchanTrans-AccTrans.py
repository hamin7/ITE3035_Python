# Upbit 2019 BTC 거래소 거래량 - 교수님거래량/거래소 거래량
import numpy as np
import matplotlib.pyplot as plt

x = ['Feb','May','Jun','Jul']
y1 = [607511668110,3152608439400,4490686502000,6224665445580]
y2 = [0.795355188,1.041418229,1.466439247,0.815025034]
# y3 = data_set['data3']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# plot with properties

line1 = ax1.plot(np.arange(len(x)), y1, color='b', linestyle='--', marker='o', label='Upbit Exchange Volume')
line2 = ax2.plot(np.arange(len(x)), y2, color='g', linestyle='--', marker='^', label='Transaction Percentage')
# line3 = ax2.plot(np.arange(len(x)), y3, color='r', linestyle='--', marker='s', label=title[3])

# plot without x sorting
ax1.set_xticklabels(['$Jan$','$Feb$','','$May$','','$Jun$','','$Jul$'])
ax1.set_xlabel('Month')
ax1.set_ylabel('Upbit Exchange Trans Volume(1,000,000,000,000KRW)')
ax2.set_ylabel('Transaction Percentage(%)')

# set y limit
ax1.set_ylim(0, 7000000000000)
ax2.set_ylim(0, 2.0)

# plot legend for all y axis
lines = line1 + line2
labels = [l.get_label() for l in lines]
plt.legend(lines, labels, loc=2)

plt.grid(True)

# fig.grid(False)

fig.tight_layout()
fig.savefig('Upbit-2019-BTC-UpbitVolume-accountTrans.png', dpi=1000)
# fig.savefig('Bithumb-BTC2018-volume-trans.eps', format='eps', dpi=1000)
plt.show()
