import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

LabelDateA='2018-04-30'
LabelDateB='2018-05-12'
LabelDateC='2018-05-26'
LabelDateD='2018-06-13'
LabelDateE='2018-06-24'
LabelDateF='2018-06-30'
LabelDateG='2018-07-05'

df = pd.DataFrame([
    dict(Task="Trade", Start='2018-04-24', Finish='2018-05-07', Color="Trade(45 days)"),
    dict(Task="No Trans", Start='2018-05-08', Finish='2018-05-16', Color="No Trans(31 days)"),
    dict(Task="Trade", Start='2018-05-17', Finish='2018-06-04', Color="Trade(45 days)"),
    dict(Task="No Trans", Start='2018-06-05', Finish='2018-06-21', Color="No Trans(31 days)"),
    dict(Task="Trade", Start='2018-06-22', Finish='2018-06-27', Color="Trade(45 days)"),
    dict(Task="No Trans", Start='2018-06-28', Finish='2018-07-02', Color="No Trans(31 days)"),
    dict(Task="Trade", Start='2018-07-03', Finish='2018-07-08', Color="Trade(45 days)")
    #dict(Task="No Trans", Start='2018-07-09', Finish='2018-07-31', Color="No Trans(91days)")
])

annots =  [dict(x=LabelDateA,y=0,text="14 Days", showarrow=False, font=dict(color='white')),
           dict(x=LabelDateB,y=1,text="9 Days", showarrow=False, font=dict(color='White')),
           dict(x=LabelDateC,y=0,text="19 Days", showarrow=False, font=dict(color='White')),
           dict(x=LabelDateD,y=1,text="17 Days", showarrow=False, font=dict(color='White')),
           dict(x=LabelDateE,y=0,text="6 Days", showarrow=False, font=dict(color='White')),
           dict(x=LabelDateF,y=1,text="5 Days", showarrow=False, font=dict(color='White')),
           dict(x=LabelDateG,y=0,text="6 Days", showarrow=False, font=dict(color='White'))
           ]

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Color", width=1400, height=300)
fig.update_layout(title_text='When we trade in Bithumb EOS 2018.04.24 ~ 2018.07.08 (76 Days)', title_x = 0.5)
fig.update_yaxes(autorange="reversed")
fig['layout']['annotations'] = annots

# fig.savefig('Bithumb-BTC2018-timeline.png', dpi=1000)
fig.show()