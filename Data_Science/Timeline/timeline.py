import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.collections import PolyCollection

data = [    (dt.datetime(2018, 1, 1, 0, 0), dt.datetime(2018, 1, 18, 23, 59), 'sleep'),
            (dt.datetime(2018, 1, 19, 0, 0), dt.datetime(2018, 1, 25, 23, 59), 'trade'),
            (dt.datetime(2018, 1, 26, 0, 0), dt.datetime(2018, 1, 30, 23, 59), 'sleep'),
            (dt.datetime(2018, 1, 31, 0, 0), dt.datetime(2018, 1, 31, 23, 59), 'trade'), 
        ]

cats = {"sleep" : 1, "trade" : 2}
colormapping = {"sleep" : "C0", "trade" : "C1"}

verts = []
colors = []
for d in data:
    v =  [(mdates.date2num(d[0]), cats[d[2]]-.4),
          (mdates.date2num(d[0]), cats[d[2]]+.4),
          (mdates.date2num(d[1]), cats[d[2]]+.4),
          (mdates.date2num(d[1]), cats[d[2]]-.4),
          (mdates.date2num(d[0]), cats[d[2]]-.4)]
    verts.append(v)
    colors.append(colormapping[d[2]])

bars = PolyCollection(verts, facecolors=colors)

fig, ax = plt.subplots()
ax.add_collection(bars)
ax.autoscale()
loc = mdates.MinuteLocator(byminute=[0,15,30,45])
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(loc))

ax.set_yticks([1,2])
ax.set_yticklabels(["sleep", "trade"])
plt.show()
fig.savefig('timeline.png', dpi = 1000)
