import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

LabelDateA='2018-01-23'
LabelDateB='2018-02-04'
LabelDateC='2018-02-22'
LabelDateD='2018-03-05'
LabelDateE='2018-03-17'
LabelDateF='2018-04-12'
LabelDateG='2018-05-15'
LabelDateH='2018-06-12'
LabelDateI='2018-07-02'

df = pd.DataFrame([
    dict(Task="Trade", Start='2018-01-19', Finish='2018-01-25', Color="Trade(159 days)"),
    dict(Task="No Trans", Start='2018-01-26', Finish='2018-02-13', Color="No Trans(21 days)"),
    dict(Task="Trade", Start='2018-02-14', Finish='2018-03-04', Color="Trade(159 days)"),
    dict(Task="No Trans", Start='2018-03-05', Finish='2018-03-06', Color="No Trans(21 days)"),
    dict(Task="Trade", Start='2018-03-07', Finish='2018-07-17', Color="Trade(159 days)")
    # dict(Task="No Trans", Start='2018-07-17', Finish='2018-07-31', Color="No Trans(91days)")
])

annots =  [dict(x=LabelDateA,y=0,text="7 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateB,y=1,text="19 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateC,y=0,text="19 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateD,y=1,text="2 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateG,y=0,text="133 Days", showarrow=False, font=dict(color='black')),
           ]

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Color", width=1400, height=300)
fig.update_layout(title_text='When we trade in Bithumb BTC 2018.01.19 ~ 2018.07.17 (180 Day)', title_x = 0.5)
fig.update_yaxes(autorange="reversed")
fig['layout']['annotations'] = annots
# fig.savefig('Bithumb-BTC2018-timeline.png', dpi=1000)
fig.show()
