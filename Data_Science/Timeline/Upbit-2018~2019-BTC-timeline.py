import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

LabelDateA='2018-07-15'
LabelDateB='2018-08-04'
LabelDateC='2018-09-22'
LabelDateD='2018-11-19'
LabelDateE='2018-11-26'
LabelDateF='2018-12-07'
LabelDateG='2018-12-14'
LabelDateH='2018-12-26'
LabelDateI='2018-12-31'
LabelDateJ='2019-01-18'
LabelDateK='2019-02-24'
LabelDateL='2019-04-01'
LabelDateM='2019-06-15'
LabelDateN='2019-07-10'
LabelDateO='2019-07-12'
LabelDateP='2019-07-26'
LabelDateQ='2019-08-01'

df = pd.DataFrame([
    dict(Task="Trade", Start='2018-07-02', Finish='2018-07-31', Color="Trade(226 days)"),
    dict(Task="No Trans", Start='2018-08-01', Finish='2018-08-07', Color="No Trans(167 days)"),
    dict(Task="Trade", Start='2018-08-08', Finish='2018-11-19', Color="Trade(226 days)"),
    dict(Task="No Trans", Start='2018-11-20', Finish='2018-11-27', Color="No Trans(167 days)"),
    dict(Task="Trade", Start='2018-11-28', Finish='2018-12-03', Color="Trade(226 days)"),
    dict(Task="No Trans", Start='2018-12-04', Finish='2018-12-18', Color="No Trans(167 days)"),
    dict(Task="Trade", Start='2018-12-19', Finish='2018-12-22', Color="Trade(226 days)"),
    dict(Task="No Trans", Start='2018-12-23', Finish='2018-12-26', Color="No Trans(167 days)"),
    dict(Task="Trade", Start='2018-12-27', Finish='2018-12-28', Color="Trade(226 days)"),
    dict(Task="No Trans", Start='2018-12-29', Finish='2019-02-20', Color="No Trans(167 days)"),
    dict(Task="Trade", Start='2019-02-21', Finish='2019-02-28', Color="Trade(226 days)"),
    dict(Task="No Trans", Start='2019-03-01', Finish='2019-05-15', Color="No Trans(167 days)"),
    dict(Task="Trade", Start='2019-05-16', Finish='2019-07-14', Color="Trade(226 days)"),
    dict(Task="No Trans", Start='2019-07-15', Finish='2019-07-16', Color="No Trans(167 days)"),
    dict(Task="Trade", Start='2019-07-17', Finish='2019-07-19', Color="Trade(226 days)"),
    dict(Task="No Trans", Start='2019-07-20', Finish='2019-07-21', Color="No Trans(167 days)"),
    dict(Task="Trade", Start='2019-07-22', Finish='2019-07-29', Color="Trade(226 days)")
    # 2019 7.15, 7.16
])

annots =  [dict(x=LabelDateA,y=0,text="30 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateB,y=1,text="7 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateC,y=0,text="104 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateD,y=1,text="8 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateE,y=0,text="6 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateF,y=1,text="15 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateG,y=0,text="4 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateH,y=1,text="4 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateI,y=0,text="2 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateJ,y=1,text="54 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateK,y=0,text="8 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateL,y=1,text="76 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateM,y=0,text="60 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateN,y=1,text="1 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateO,y=0,text="4 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateP,y=1,text="2 Days", showarrow=False, font=dict(color='black')),
           dict(x=LabelDateQ,y=0,text="8 Days", showarrow=False, font=dict(color='black'))
           ]

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Color", width=1400, height=300)
fig.update_layout(title_text='When we trade in Upbit BTC 2018 ~ 2019', title_x = 0.5)
fig.update_yaxes(autorange="reversed")
fig['layout']['annotations'] = annots
# fig.savefig('Bithumb-BTC2018-timeline.png', dpi=1000)
fig.show()