import pandas as pd
import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, savefig
import time

def profitGraphGenerator():
    
    for i in range(1,8):
        # load csv data
        # have to change directory according to computing circumstances
        # may be we can find better way.... (using parameter)
        globals()['df{}'.format(i)] = pd.read_csv("/Users/hamin/bithumb_bot_data/include/2018-new/2018-0{}-btc-krw.csv".format(i))
        
        # converting timestamp column type 'object' to 'datetime'
        globals()['df{}'.format(i)]['timestamp'] = pd.to_datetime(globals()['df{}'.format(i)]['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')

        # quantity에 부호 붙이기
        for j, row in globals()['df{}'.format(i)].iterrows(): 
	        if row["side"]==0:
	            row["quantity"]=-row["quantity"]
	        globals()['df{}'.format(i)].at[j,'sign_quantity'] = row["quantity"]

        # timestamp (시간), quantity (거래 코인 양), price (코인 1개 당 가격), fee (??), amount (q * price), side (0:판 것, 1:산 것)
        
        # sign_quantity 더하기 - sign_quantity_cumsum은 현재 시점 보유한 coin의 quantity
        globals()['sign_quantity_cumsum{}'.format(i)]=globals()['df{}'.format(i)]["sign_quantity"].cumsum()

        # amount 더하기 - amount_cumsum이 profit임
        globals()['amount_cumsum{}'.format(i)]=globals()['df{}'.format(i)]["amount"].cumsum()

        # float16 type으로 타입 변경
        globals()['sign_quantity_cumsum{}'.format(i)] = globals()['sign_quantity_cumsum{}'.format(i)].astype('float16')

        # 데이터프레임 df1, sign_quantity_cumsum, amount_cumsum 결합
        globals()['cumsum_df{}'.format(i)] = pd.concat([globals()['df{}'.format(i)],globals()['sign_quantity_cumsum{}'.format(i)],globals()['amount_cumsum{}'.format(i)]],axis=1)\

        # 칼럼 지정
        globals()['cumsum_df{}'.format(i)].columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum']

        # 소숫점 다섯째 자리에서 자르기
        globals()['cumsum_df_zero_point{}'.format(i)]=globals()['cumsum_df{}'.format(i)][ (globals()['cumsum_df{}'.format(i)]['sign_quantity_cumsum(coin)'] < 0.00001) & (globals()['cumsum_df{}'.format(i)]['sign_quantity_cumsum(coin)'] > -0.00001)]

        # 데이터 한 칸씩 미루기
        globals()['compare{}'.format(i)]=globals()['cumsum_df_zero_point{}'.format(i)]['amount_cumsum']
        # 인덱스는 그대로 두고 데이터 한 칸씩 이동
        globals()['compare{}'.format(i)]=globals()['compare{}'.format(i)].shift(1)[:]       

        # 데이터 프레임 cumsum_df_zero_point()와 compare 결합
        globals()['cumsum_df_zero_point{}'.format(i)] = pd.concat([globals()['cumsum_df_zero_point{}'.format(i)],globals()['compare{}'.format(i)]],axis=1)

        # 결측값은 0으로 채우기
        globals()['cumsum_df_zero_point{}'.format(i)] = globals()['cumsum_df_zero_point{}'.format(i)].fillna(0)

        # 칼럼 지정
        globals()['cumsum_df_zero_point{}'.format(i)].columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum', 'compare']

        # 구간 별 profit 구하기 (point_amount_cumsum)
        globals()['cumsum_df_zero_point{}'.format(i)]['point_amount_cumsum'] = globals()['cumsum_df_zero_point{}'.format(i)]['amount_cumsum'] - globals()['cumsum_df_zero_point{}'.format(i)]['compare']
        
        # 결측값은 0으로 채우기
        globals()['cumsum_df_zero_point{}'.format(i)]=globals()['cumsum_df_zero_point{}'.format(i)].fillna(0)

        # 달 별 profit(cumulative) 그래프 생성 및 저장
        # 데이터가 없는 경우 패스
        if globals()['cumsum_df_zero_point{}'.format(i)].empty:
    	    continue
        else:
	        globals()['profit_graph{}'.format(i)]=globals()['cumsum_df_zero_point{}'.format(i)][['amount_cumsum']].plot(title='bithumb-2018-0{}-profit_graph'.format(i))
	        globals()['profit_graph{}'.format(i)].set_xlabel('date')
	        globals()['profit_graph{}'.format(i)].set_ylabel('Profit_price(1 thousand krw)')
	        globals()['profit_graph{}'.format(i)].set_yticklabels(['$0$', '$0$','$2,000$','$4,000$','$6,000$','$8,000$','$10,000$', '$12,000$', '$14,000$', '$16,000$'])
	        globals()['profit_graph{}'.format(i)].set_xticklabels(['$0{}/1$', '$0{}/07$', '$0{}/13$', '$0{}/20$', '$0{}/26$'.format(i, i, i, i, i)])
	        plt.savefig('/Users/hamin/bithumb_bot/graph/bithumb-2018-0{}-profit_graph.png'.format(i), dpi=300)
        
        # 달별 구간 profit 그래프 생성 및 저장 
        if globals()['cumsum_df_zero_point{}'.format(i)].empty:
    	    continue
        else:
	        globals()['profit_point_graph{}'.format(i)]=globals()['cumsum_df_zero_point{}'.format(i)][['point_amount_cumsum']].plot(title='bithumb-2018-0{}-profit_point_graph'.format(i))
	        globals()['profit_point_graph{}'.format(i)].set_xlabel('date')
	        globals()['profit_point_graph{}'.format(i)].set_ylabel('Profit_price(1 thousand krw)')
	        globals()['profit_point_graph{}'.format(i)].set_yticklabels(['$0$', '$-500$', '$-250$','$0$','$250$','$500$','$750$','$1,000$', '$1,250$', '$1,500$'])
	        globals()['profit_point_graph{}'.format(i)].set_xticklabels(['$0{}/1$', '$0{}/07$', '$0{}/13$', '$0{}/20$', '$0{}/26$'.format(i, i, i, i, i)])
	        plt.savefig('/Users/hamin/bithumb_bot/graph/bithumb-2018-0{}-profit_point_graph.png'.format(i), dpi=300)

        # 테이블 저장
        if globals()['profit_graph_table{}'.format(i)].empty:
            continue
        else:
	        globals()['profit_graph_table{}'.format(i)].to_csv("/Users/hamin/bithumb_bot/table/bithumb-2018-0{}-profit_graph_table.csv".format(i), header=True, index=True, encoding = 'utf-8')

        # 시간 - profit 누적 테이블 생성
        globals()['profit_point_graph_table{}'.format(i)]=globals()['cumsum_df_zero_point{}'.format(i)][['timestamp', 'point_amount_cumsum']]
        
        # time - profit 누적 테이블 저장
        if globals()['profit_point_graph_table{}'.format(i)].empty:
    	    continue
        else:
            globals()['profit_point_graph_table{}'.format(i)].to_csv("/Users/hamin/bithumb_bot/table/bithumb-2018-0{}-profit_point_graph_table.csv".format(i), header=True, index=True, encoding = 'utf-8')

        time.sleep(2)

        if globals()['profit_graph_table{}'.format(i)].empty:
            continue
        else:
            print("bithumb-2018-0{}-profit_graph_table".format(i))
            print(globals()['profit_graph_table{}'.format(i)])    
        
        time.sleep(2)
        if globals()['profit_point_graph_table{}'.format(i)].empty:
            continue
        else:
            print("bithumb-2018-0{}-profit_point_graph_table".format(i))
            print(globals()['profit_point_graph_table{}'.format(i)])

# time - profit 그래프 생성
profitGraphGenerator()