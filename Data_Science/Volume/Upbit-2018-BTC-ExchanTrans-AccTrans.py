# Upbit 2018 BTC 교수님 거래량 - 교수님거래량/거래소 거래량
import numpy as np
import matplotlib.pyplot as plt

x = ['Jul','Aug','Sep','Oct','Nov','Dec']
y1 = [2069650043279,1149059584200,740095260000,528729908927,1247680784000,1062559403080]
y2 = [1.280066866,1.860222927,1.781144581,1.124880324,0.400038761,0.348157678]
# y3 = data_set['data3']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# plot with properties

line1 = ax1.plot(np.arange(len(x)), y1, color='b', linestyle='--', marker='o', label='Upbit Exchange Volume')
line2 = ax2.plot(np.arange(len(x)), y2, color='g', linestyle='--', marker='^', label='Transaction Percentage')
# line3 = ax2.plot(np.arange(len(x)), y3, color='r', linestyle='--', marker='s', label=title[3])

# plot without x sorting
ax1.set_xticklabels(['$Jun$','$Jul$','$Aug$','$Sep$','$Oct$','$Nov$','$Dec$'])
ax1.set_xlabel('Month')
ax1.set_ylabel('Upbit Exchange Trans Volume(1,000,000,000,000KRW)')
ax2.set_ylabel('Transaction Percentage(%)')

# set y limit
ax1.set_ylim(0, 3000000000000)
ax2.set_ylim(0, 2.5)

# plot legend for all y axis
lines = line1 + line2
labels = [l.get_label() for l in lines]
plt.legend(lines, labels, loc=2)

plt.grid(True)

# fig.grid(False)

fig.tight_layout()
fig.savefig('Upbit-2018-BTC-UpbitVolume-accountTrans.png', dpi=1000)
# fig.savefig('Bithumb-BTC2018-volume-trans.eps', format='eps', dpi=1000)
plt.show()
