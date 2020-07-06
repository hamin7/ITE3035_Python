import pandas as pd
import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, savefig


df1 = pd.read_csv("/Users/hamin/bithumb_bot_data/include/2018-new/2018-01-btc-krw.csv")   # load csv
df2 = pd.read_csv("/Users/hamin/bithumb_bot_data/include/2018-new/2018-02-btc-krw.csv")   # load csv
df3 = pd.read_csv("/Users/hamin/bithumb_bot_data/include/2018-new/2018-03-btc-krw.csv")   # load csv
df4 = pd.read_csv("/Users/hamin/bithumb_bot_data/include/2018-new/2018-04-btc-krw.csv")   # load csv
df5 = pd.read_csv("/Users/hamin/bithumb_bot_data/include/2018-new/2018-05-btc-krw.csv")   # load csv
df6 = pd.read_csv("/Users/hamin/bithumb_bot_data/include/2018-new/2018-06-btc-krw.csv")   # load csv
df7 = pd.read_csv("/Users/hamin/bithumb_bot_data/include/2018-new/2018-07-btc-krw.csv")   # load csv

## converting timestamp column type 'object' to 'datetime'
df1['timestamp'] = pd.to_datetime(df1['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
df2['timestamp'] = pd.to_datetime(df2['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
df3['timestamp'] = pd.to_datetime(df3['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
df4['timestamp'] = pd.to_datetime(df4['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
df5['timestamp'] = pd.to_datetime(df5['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
df6['timestamp'] = pd.to_datetime(df6['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
df7['timestamp'] = pd.to_datetime(df7['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')

# quantity에 부호 붙이기
for i, row in df1.iterrows(): 
    if row["side"]==0:
        row["quantity"]=-row["quantity"]
    df1.at[i,'sign_quantity'] = row["quantity"]

# quantity에 부호 붙이기
for i, row in df2.iterrows(): 
    if row["side"]==0:
        row["quantity"]=-row["quantity"]
    df2.at[i,'sign_quantity'] = row["quantity"]

# quantity에 부호 붙이기
for i, row in df3.iterrows(): 
    if row["side"]==0:
        row["quantity"]=-row["quantity"]
    df3.at[i,'sign_quantity'] = row["quantity"]

# quantity에 부호 붙이기
for i, row in df4.iterrows(): 
    if row["side"]==0:
        row["quantity"]=-row["quantity"]
    df4.at[i,'sign_quantity'] = row["quantity"]

# quantity에 부호 붙이기
for i, row in df5.iterrows(): 
    if row["side"]==0:
        row["quantity"]=-row["quantity"]
    df5.at[i,'sign_quantity'] = row["quantity"]

# quantity에 부호 붙이기
for i, row in df6.iterrows(): 
    if row["side"]==0:
        row["quantity"]=-row["quantity"]
    df6.at[i,'sign_quantity'] = row["quantity"]

# quantity에 부호 붙이기
for i, row in df7.iterrows(): 
    if row["side"]==0:
        row["quantity"]=-row["quantity"]
    df7.at[i,'sign_quantity'] = row["quantity"]

# timestamp (시간), quantity (거래 코인 양), price (코인 1개 당 가격), fee (??), amount (q * price), side (0:판 것, 1:산 것)

# sign_quantity 더하기 - sign_quantity_cumsum은 현재 시점 보유한 coin의 quantity
sign_quantity_cumsum1=df1["sign_quantity"].cumsum()
sign_quantity_cumsum2=df2["sign_quantity"].cumsum()
sign_quantity_cumsum3=df3["sign_quantity"].cumsum()
sign_quantity_cumsum4=df4["sign_quantity"].cumsum()
sign_quantity_cumsum5=df5["sign_quantity"].cumsum()
sign_quantity_cumsum6=df6["sign_quantity"].cumsum()
sign_quantity_cumsum7=df7["sign_quantity"].cumsum()

# amount 더하기 - amount_cumsum이 profit임
amount_cumsum1=df1["amount"].cumsum()
amount_cumsum2=df2["amount"].cumsum()
amount_cumsum3=df3["amount"].cumsum()
amount_cumsum4=df4["amount"].cumsum()
amount_cumsum5=df5["amount"].cumsum()
amount_cumsum6=df6["amount"].cumsum()
amount_cumsum7=df7["amount"].cumsum()

# float16 type으로 타입 변경
sign_quantity_cumsum1 = sign_quantity_cumsum1.astype('float16')
sign_quantity_cumsum2 = sign_quantity_cumsum2.astype('float16')
sign_quantity_cumsum3 = sign_quantity_cumsum3.astype('float16')
sign_quantity_cumsum4 = sign_quantity_cumsum4.astype('float16')
sign_quantity_cumsum5 = sign_quantity_cumsum5.astype('float16')
sign_quantity_cumsum6 = sign_quantity_cumsum6.astype('float16')
sign_quantity_cumsum7 = sign_quantity_cumsum7.astype('float16')

# 데이터프레임 df1, sign_quantity_cumsum, amount_cumsum 결합
cumsum_df1 = pd.concat([df1,sign_quantity_cumsum1,amount_cumsum1],axis=1)
cumsum_df2 = pd.concat([df2,sign_quantity_cumsum2,amount_cumsum2],axis=1)
cumsum_df3 = pd.concat([df3,sign_quantity_cumsum3,amount_cumsum3],axis=1)
cumsum_df4 = pd.concat([df4,sign_quantity_cumsum4,amount_cumsum4],axis=1)
cumsum_df5 = pd.concat([df5,sign_quantity_cumsum5,amount_cumsum5],axis=1)
cumsum_df6 = pd.concat([df6,sign_quantity_cumsum6,amount_cumsum6],axis=1)
cumsum_df7 = pd.concat([df7,sign_quantity_cumsum7,amount_cumsum7],axis=1)

# 칼럼 지정
cumsum_df1.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum']
cumsum_df2.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum']
cumsum_df3.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum']
cumsum_df4.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum']
cumsum_df5.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum']
cumsum_df6.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum']
cumsum_df7.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum']

# 소숫점 다섯째 자리에서 자르기
cumsum_df_zero_point1=cumsum_df1[ (cumsum_df1['sign_quantity_cumsum(coin)'] < 0.01) & (cumsum_df1['sign_quantity_cumsum(coin)'] > -0.01)]
cumsum_df_zero_point2=cumsum_df2[ (cumsum_df2['sign_quantity_cumsum(coin)'] < 0.01) & (cumsum_df2['sign_quantity_cumsum(coin)'] > -0.01)]
cumsum_df_zero_point3=cumsum_df3[ (cumsum_df3['sign_quantity_cumsum(coin)'] < 0.01) & (cumsum_df3['sign_quantity_cumsum(coin)'] > -0.01)]
cumsum_df_zero_point4=cumsum_df4[ (cumsum_df4['sign_quantity_cumsum(coin)'] < 0.01) & (cumsum_df4['sign_quantity_cumsum(coin)'] > -0.01)]
cumsum_df_zero_point5=cumsum_df5[ (cumsum_df5['sign_quantity_cumsum(coin)'] < 0.01) & (cumsum_df5['sign_quantity_cumsum(coin)'] > -0.01)]
cumsum_df_zero_point6=cumsum_df6[ (cumsum_df6['sign_quantity_cumsum(coin)'] < 0.01) & (cumsum_df6['sign_quantity_cumsum(coin)'] > -0.01)]
cumsum_df_zero_point7=cumsum_df7[ (cumsum_df7['sign_quantity_cumsum(coin)'] < 0.01) & (cumsum_df7['sign_quantity_cumsum(coin)'] > -0.01)]

# 데이터 한 칸씩 미루기
compare1=cumsum_df_zero_point1['amount_cumsum']
compare1=compare1.shift(1)[:]     # 인덱스는 그대로 두고 데이터 한 칸씩 이동

compare2=cumsum_df_zero_point2['amount_cumsum']
compare2=compare2.shift(1)[:]

compare3=cumsum_df_zero_point3['amount_cumsum']
compare3=compare3.shift(1)[:]

compare4=cumsum_df_zero_point4['amount_cumsum']
compare4=compare4.shift(1)[:]

compare5=cumsum_df_zero_point5['amount_cumsum']
compare5=compare5.shift(1)[:]

compare6=cumsum_df_zero_point6['amount_cumsum']
compare6=compare6.shift(1)[:]

compare7=cumsum_df_zero_point7['amount_cumsum']
compare7=compare7.shift(1)[:]

# 데이터 프레임 cumsum_df_zero_point()와 compare 결합
cumsum_df_zero_point1 = pd.concat([cumsum_df_zero_point1,compare1],axis=1)
cumsum_df_zero_point1 = cumsum_df_zero_point1.fillna(0)     # 결측값은 0으로 채우기

cumsum_df_zero_point2 = pd.concat([cumsum_df_zero_point2,compare2],axis=1)
cumsum_df_zero_point2 = cumsum_df_zero_point2.fillna(0)

cumsum_df_zero_point3 = pd.concat([cumsum_df_zero_point3,compare3],axis=1)
cumsum_df_zero_point3 = cumsum_df_zero_point3.fillna(0)

cumsum_df_zero_point4 = pd.concat([cumsum_df_zero_point4,compare4],axis=1)
cumsum_df_zero_point4 = cumsum_df_zero_point4.fillna(0)

cumsum_df_zero_point5 = pd.concat([cumsum_df_zero_point5,compare5],axis=1)
cumsum_df_zero_point5 = cumsum_df_zero_point5.fillna(0)

cumsum_df_zero_point6 = pd.concat([cumsum_df_zero_point6,compare6],axis=1)
cumsum_df_zero_point6 = cumsum_df_zero_point6.fillna(0)

cumsum_df_zero_point7 = pd.concat([cumsum_df_zero_point7,compare7],axis=1)
cumsum_df_zero_point7 = cumsum_df_zero_point7.fillna(0)

# 칼럼 지정
cumsum_df_zero_point1.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum', 'compare']
cumsum_df_zero_point2.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum', 'compare']
cumsum_df_zero_point3.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum', 'compare']
cumsum_df_zero_point4.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum', 'compare']
cumsum_df_zero_point5.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum', 'compare']
cumsum_df_zero_point6.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum', 'compare']
cumsum_df_zero_point7.columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum', 'compare']

# 구간 별 profit 구하기 (point_amount_cumsum)
cumsum_df_zero_point1['point_amount_cumsum'] = cumsum_df_zero_point1['amount_cumsum'] - cumsum_df_zero_point1['compare']
cumsum_df_zero_point2['point_amount_cumsum'] = cumsum_df_zero_point2['amount_cumsum'] - cumsum_df_zero_point2['compare']
cumsum_df_zero_point3['point_amount_cumsum'] = cumsum_df_zero_point3['amount_cumsum'] - cumsum_df_zero_point3['compare']
cumsum_df_zero_point4['point_amount_cumsum'] = cumsum_df_zero_point4['amount_cumsum'] - cumsum_df_zero_point4['compare']
cumsum_df_zero_point5['point_amount_cumsum'] = cumsum_df_zero_point5['amount_cumsum'] - cumsum_df_zero_point5['compare']
cumsum_df_zero_point6['point_amount_cumsum'] = cumsum_df_zero_point6['amount_cumsum'] - cumsum_df_zero_point6['compare']
cumsum_df_zero_point7['point_amount_cumsum'] = cumsum_df_zero_point7['amount_cumsum'] - cumsum_df_zero_point7['compare']

# 결측값은 0으로 채우기
cumsum_df_zero_point1=cumsum_df_zero_point1.fillna(0)
cumsum_df_zero_point2=cumsum_df_zero_point2.fillna(0)
cumsum_df_zero_point3=cumsum_df_zero_point3.fillna(0)
cumsum_df_zero_point4=cumsum_df_zero_point4.fillna(0)
cumsum_df_zero_point5=cumsum_df_zero_point5.fillna(0)
cumsum_df_zero_point6=cumsum_df_zero_point6.fillna(0)
cumsum_df_zero_point7=cumsum_df_zero_point7.fillna(0)

# 달 별 profit 그래프 생성 및 저장
profit_graph1=cumsum_df_zero_point1[['amount_cumsum']].plot(title='2018-01-profit_graph')
profit_graph1.set_xlabel('date')
profit_graph1.set_ylabel('Profit_price(1 thousand krw)')
profit_graph1.set_yticklabels(['$0$', '$0$','$2,000$','$4,000$','$6,000$','$8,000$','$10,000$', '$12,000$'])
profit_graph1.set_xticklabels(['$0$', '$05/07$', '$05/13$', '$05/20$', '$05/26$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/profit/2018-01-profit_graph.png', dpi=300)

profit_graph2=cumsum_df_zero_point2[['amount_cumsum']].plot(title='2018-02-profit_graph')
profit_graph2.set_xlabel('date')
profit_graph2.set_ylabel('Profit_price(1 thousand krw)')
profit_graph2.set_yticklabels(['$0$', '$0$','$2,000$','$4,000$','$6,000$','$8,000$','$10,000$', '$12,000$'])
profit_graph2.set_xticklabels(['$0$', '$02/14$', '$02/16$', '$02/18$', '$02/20$', '$02/22$', '$02/24$', '$02/26$', '$02/28$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/profit/2018-02-profit_graph.png', dpi=300)

profit_graph3=cumsum_df_zero_point3[['amount_cumsum']].plot(title='2018-03-profit_graph')
profit_graph3.set_xlabel('date')
profit_graph3.set_ylabel('Profit_price(1 thousand krw)')
profit_graph3.set_yticklabels(['$0$', '$0$','$2,000$','$4,000$','$6,000$','$8,000$','$10,000$', '$12,000$'])
profit_graph3.set_xticklabels(['$0$', '$03/01$', '$03/06$', '$03/11$', '$03/16$', '$03/21$', '$03/26$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/profit/2018-03-profit_graph.png', dpi=300)

profit_graph4=cumsum_df_zero_point4[['amount_cumsum']].plot(title='2018-04-profit_graph')
profit_graph4.set_xlabel('date')
profit_graph4.set_ylabel('Profit_price(1 thousand krw)')
profit_graph4.set_yticklabels(['$0$', '$0$','$2,000$','$4,000$','$6,000$','$8,000$','$10,000$', '$12,000$'])
profit_graph4.set_xticklabels(['$0$', '$04/01$', '$04/06$', '$04/11$', '$04/16$', '$04/21$', '$04/26$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/profit/2018-04-profit_graph.png', dpi=300)

profit_graph5=cumsum_df_zero_point5[['amount_cumsum']].plot(title='2018-05-profit_graph')
profit_graph5.set_xlabel('date')
profit_graph5.set_ylabel('Profit_price(1 thousand krw)')
profit_graph5.set_yticklabels(['$0$', '$0$','$2,000$','$4,000$','$6,000$','$8,000$','$10,000$', '$12,000$'])
profit_graph5.set_xticklabels(['$0$', '$05/01$', '$05/07$', '$05/13$', '$05/19$', '$05/25$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/profit/2018-05-profit_graph.png', dpi=300)

profit_graph6=cumsum_df_zero_point6[['amount_cumsum']].plot(title='2018-06-profit_graph')
profit_graph6.set_xlabel('date')
profit_graph6.set_ylabel('Profit_price(1 thousand krw)')
profit_graph6.set_yticklabels(['$0$', '$0$','$2,000$','$4,000$','$6,000$','$8,000$','$10,000$', '$12,000$'])
profit_graph6.set_xticklabels(['$0$', '$06/01$', '$06/07$', '$06/13$', '$06/19$', '06/25'])
plt.savefig('/Users/hamin/bithumb_bot/graph/profit/2018-06-profit_graph.png', dpi=300)

profit_graph7=cumsum_df_zero_point7[['amount_cumsum']].plot(title='2018-07-profit_graph')
profit_graph7.set_xlabel('date')
profit_graph7.set_ylabel('Profit_price(1 thousand krw)')
profit_graph7.set_yticklabels(['$0$', '$0$','$2,000$','$4,000$','$6,000$','$8,000$','$10,000$', '$12,000$'])
profit_graph7.set_xticklabels(['$0$', '$07/01$', '$07/07$', '$07/13$', '$07/19$', '07/25'])
plt.savefig('/Users/hamin/bithumb_bot/graph/profit/2018-07-profit_graph.png', dpi=300)











profit_point_graph1=cumsum_df_zero_point1[['point_amount_cumsum']].plot(title='2018-01-profit_point_graph')
profit_point_graph1.set_xlabel('date')
profit_point_graph1.set_ylabel('Profit_price(1 thousand krw)')
profit_point_graph1.set_yticklabels(['$0$', '$-500$', '$-250$','$0$','$250$','$500$','$750$','$1,000$', '$1,250$', '$1,500$'])
profit_point_graph1.set_xticklabels(['$0$', '$05/07$', '$05/13$', '$05/20$', '$05/26$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/2018-01-profit_point_graph.png', dpi=300)

profit_point_graph2=cumsum_df_zero_point2[['point_amount_cumsum']].plot(title='2018-02-profit_point_graph')
profit_point_graph2.set_xlabel('date')
profit_point_graph2.set_ylabel('Profit_price(1 thousand krw)')
profit_point_graph2.set_yticklabels(['$0$', '$-500$', '$-250$','$0$','$250$','$500$','$750$','$1,000$', '$1,250$', '$1,500$'])
profit_point_graph2.set_xticklabels(['$0$', '$05/07$', '$05/13$', '$05/20$', '$05/26$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/2018-02-profit_point_graph.png', dpi=300)

profit_point_graph3=cumsum_df_zero_point3[['point_amount_cumsum']].plot(title='2018-03-profit_point_graph')
profit_point_graph3.set_xlabel('date')
profit_point_graph3.set_ylabel('Profit_price(1 thousand krw)')
profit_point_graph3.set_yticklabels(['$0$', '$-500$', '$-250$','$0$','$250$','$500$','$750$','$1,000$', '$1,250$', '$1,500$'])
profit_point_graph3.set_xticklabels(['$0$', '$05/07$', '$05/13$', '$05/20$', '$05/26$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/2018-03-profit_point_graph.png', dpi=300)

profit_point_graph4=cumsum_df_zero_point4[['point_amount_cumsum']].plot(title='2018-04-profit_point_graph')
profit_point_graph4.set_xlabel('date')
profit_point_graph4.set_ylabel('Profit_price(1 thousand krw)')
profit_point_graph4.set_yticklabels(['$0$', '$-500$', '$-250$','$0$','$250$','$500$','$750$','$1,000$', '$1,250$', '$1,500$'])
profit_point_graph4.set_xticklabels(['$0$', '$05/07$', '$05/13$', '$05/20$', '$05/26$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/2018-04-profit_point_graph.png', dpi=300)

profit_point_graph5=cumsum_df_zero_point5[['point_amount_cumsum']].plot(title='2018-05-profit_point_graph')
profit_point_graph5.set_xlabel('date')
profit_point_graph5.set_ylabel('Profit_price(1 thousand krw)')
profit_point_graph5.set_yticklabels(['$0$', '$-500$', '$-250$','$0$','$250$','$500$','$750$','$1,000$', '$1,250$', '$1,500$'])
profit_point_graph5.set_xticklabels(['$0$', '$05/07$', '$05/13$', '$05/20$', '$05/26$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/2018-05-profit_point_graph.png', dpi=300)

profit_point_graph6=cumsum_df_zero_point6[['point_amount_cumsum']].plot(title='2018-06-profit_point_graph')
profit_point_graph6.set_xlabel('date')
profit_point_graph6.set_ylabel('Profit_price(1 thousand krw)')
profit_point_graph6.set_yticklabels(['$0$', '$-500$', '$-250$','$0$','$250$','$500$','$750$','$1,000$', '$1,250$', '$1,500$'])
profit_point_graph6.set_xticklabels(['$0$', '$05/07$', '$05/13$', '$05/20$', '$05/26$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/2018-06-profit_point_graph.png', dpi=300)

profit_point_graph7=cumsum_df_zero_point7[['point_amount_cumsum']].plot(title='2018-07-profit_point_graph')
profit_point_graph7.set_xlabel('date')
profit_point_graph7.set_ylabel('Profit_price(1 thousand krw)')
profit_point_graph7.set_yticklabels(['$0$', '$-500$', '$-250$','$0$','$250$','$500$','$750$','$1,000$', '$1,250$', '$1,500$'])
profit_point_graph7.set_xticklabels(['$0$', '$05/07$', '$05/13$', '$05/20$', '$05/26$'])
plt.savefig('/Users/hamin/bithumb_bot/graph/2018-07-profit_point_graph.png', dpi=300)

# 테이블 저장
cumsum_df_zero_point1.to_csv("/Users/hamin/bithumb_bot/table/2018-01-profit_table.csv", header=True, index=True, encoding = 'utf-8')
cumsum_df_zero_point2.to_csv("/Users/hamin/bithumb_bot/table/2018-02-profit_table.csv", header=True, index=True, encoding = 'utf-8')
cumsum_df_zero_point3.to_csv("/Users/hamin/bithumb_bot/table/2018-03-profit_table.csv", header=True, index=True, encoding = 'utf-8')
cumsum_df_zero_point4.to_csv("/Users/hamin/bithumb_bot/table/2018-04-profit_table.csv", header=True, index=True, encoding = 'utf-8')
cumsum_df_zero_point5.to_csv("/Users/hamin/bithumb_bot/table/2018-05-profit_table.csv", header=True, index=True, encoding = 'utf-8')
cumsum_df_zero_point6.to_csv("/Users/hamin/bithumb_bot/table/2018-06-profit_table.csv", header=True, index=True, encoding = 'utf-8')
cumsum_df_zero_point7.to_csv("/Users/hamin/bithumb_bot/table/2018-07-profit_table.csv", header=True, index=True, encoding = 'utf-8')

# 시간 - profit 누적 테이블 생성
profit_graph_table1=cumsum_df_zero_point1[['timestamp', 'amount_cumsum']]
profit_graph_table2=cumsum_df_zero_point2[['timestamp', 'amount_cumsum']]
profit_graph_table3=cumsum_df_zero_point3[['timestamp', 'amount_cumsum']]
profit_graph_table4=cumsum_df_zero_point4[['timestamp', 'amount_cumsum']]
profit_graph_table5=cumsum_df_zero_point5[['timestamp', 'amount_cumsum']]
profit_graph_table6=cumsum_df_zero_point6[['timestamp', 'amount_cumsum']]
profit_graph_table7=cumsum_df_zero_point7[['timestamp', 'amount_cumsum']]

# time - profit 누적 테이블 저장
profit_graph_table1.to_csv("/Users/hamin/bithumb_bot/table/2018-01-profit_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_graph_table2.to_csv("/Users/hamin/bithumb_bot/table/2018-02-profit_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_graph_table3.to_csv("/Users/hamin/bithumb_bot/table/2018-03-profit_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_graph_table4.to_csv("/Users/hamin/bithumb_bot/table/2018-04-profit_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_graph_table5.to_csv("/Users/hamin/bithumb_bot/table/2018-05-profit_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_graph_table6.to_csv("/Users/hamin/bithumb_bot/table/2018-06-profit_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_graph_table7.to_csv("/Users/hamin/bithumb_bot/table/2018-07-profit_graph_table.csv", header=True, index=True, encoding = 'utf-8')

# time - 구간 별 profit 테이블 생성
profit_point_graph_table1=cumsum_df_zero_point1[['timestamp', 'point_amount_cumsum']]
profit_point_graph_table2=cumsum_df_zero_point2[['timestamp', 'point_amount_cumsum']]
profit_point_graph_table3=cumsum_df_zero_point3[['timestamp', 'point_amount_cumsum']]
profit_point_graph_table4=cumsum_df_zero_point4[['timestamp', 'point_amount_cumsum']]
profit_point_graph_table5=cumsum_df_zero_point5[['timestamp', 'point_amount_cumsum']]
profit_point_graph_table6=cumsum_df_zero_point6[['timestamp', 'point_amount_cumsum']]
profit_point_graph_table7=cumsum_df_zero_point7[['timestamp', 'point_amount_cumsum']]

# time - 구간 별 profit 테이블 저장
profit_point_graph_table1.to_csv("/Users/hamin/bithumb_bot/table/2018-01-profit_point_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_point_graph_table2.to_csv("/Users/hamin/bithumb_bot/table/2018-02-profit_point_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_point_graph_table3.to_csv("/Users/hamin/bithumb_bot/table/2018-03-profit_point_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_point_graph_table4.to_csv("/Users/hamin/bithumb_bot/table/2018-04-profit_point_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_point_graph_table5.to_csv("/Users/hamin/bithumb_bot/table/2018-05-profit_point_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_point_graph_table6.to_csv("/Users/hamin/bithumb_bot/table/2018-06-profit_point_graph_table.csv", header=True, index=True, encoding = 'utf-8')
profit_point_graph_table7.to_csv("/Users/hamin/bithumb_bot/table/2018-07-profit_point_graph_table.csv", header=True, index=True, encoding = 'utf-8')

if __name__ == "__main__":
