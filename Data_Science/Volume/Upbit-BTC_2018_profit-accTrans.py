# Upbit 2018 BTC 수익-교수님 거래량
import numpy as np
import matplotlib.pyplot as plt

x = ['Jul','Aug','Sep','Oct','Nov','Dec']
y1 = [400090,2958947,1673592,10510,5164420,-683606]
y2 = [26492904441,21375069835,13182166616,5947578714,4991206748,3699382140]
# y3 = data_set['data3']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# plot with properties

line1 = ax1.plot(np.arange(len(x)), y1, color='b', linestyle='--', marker='o', label='Profit')
line2 = ax2.plot(np.arange(len(x)), y2, color='g', linestyle='--', marker='^', label='Account Transaction')
# line3 = ax2.plot(np.arange(len(x)), y3, color='r', linestyle='--', marker='s', label=title[3])

# plot without x sorting
ax1.set_xticklabels(['$Jun$','$Jul$','$Aug$','$Sep$','$Oct$','$Nov$','$Dec$'])
ax1.set_xlabel('Month')
ax1.set_ylabel('Profit(1,000,000KRW)')
ax2.set_ylabel('Account Transaction(10,000,000,000KRW)')

# set y limit
ax1.set_ylim(-10000000, 10000000)
ax2.set_ylim(0, 35000000000)

# plot legend for all y axis
lines = line1 + line2
labels = [l.get_label() for l in lines]
plt.legend(lines, labels, loc=2)

plt.grid(True)

# fig.grid(False)

fig.tight_layout()
fig.savefig('Upbit-2018-BTC-profit-accountTrans.png', dpi=1000)
#fig.savefig('Bithumb-BTC2018-volume-profit.eps', format='eps', dpi=1000)
plt.show()
