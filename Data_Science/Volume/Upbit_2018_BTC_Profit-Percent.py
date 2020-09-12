# Upbit 2018 BTC 수익 - 거래량 비율
import numpy as np
import matplotlib.pyplot as plt

x = ['Jul','Aug','Sep','Oct','Nov','Dec']
y1 = [400090,2958947,1673592,10510,5164420,-683606]
y2 = [1.280066866,1.860222927,1.781144581,1.124880324,0.400038761,0.348157678]
# y3 = data_set['data3']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# plot with properties

line1 = ax1.plot(np.arange(len(x)), y1, color='b', linestyle='--', marker='o', label='Profit')
line2 = ax2.plot(np.arange(len(x)), y2, color='g', linestyle='--', marker='^', label='Trans Percentage')
# line3 = ax2.plot(np.arange(len(x)), y3, color='r', linestyle='--', marker='s', label=title[3])

# plot without x sorting
ax1.set_xticklabels(['$Jun$','$Jul$','$Aug$','$Sep$','$Oct$','$Nov$','$Dec$'])
ax1.set_xlabel('Month')
ax1.set_ylabel('Profit(1,000,000KRW)')
ax2.set_ylabel('Transaction Percentage(%)')

# set y limit
ax1.set_ylim(-10000000, 10000000)
ax2.set_ylim(0, 2.5)

# plot legend for all y axis
lines = line1 + line2
labels = [l.get_label() for l in lines]
plt.legend(lines, labels, loc=2)

plt.grid(True)

# fig.grid(False)

fig.tight_layout()
fig.savefig('Upbit-BTC2018-profit-percent.png', dpi=1000)
# fig.savefig('Bithumb-BTC2018-trans-profit.eps', format='eps', dpi=1000)
plt.show()
