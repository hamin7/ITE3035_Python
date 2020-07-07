import pandas as pd
import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, savefig
import time
import csv
import sys

def marketPriceSource():
    input_file = "orderBookSample.csv"
    output_file = "marketPriceSource.csv"

    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'w', newline='') as csv_out_file:
            freader = csv.reader(csv_in_file)
            fwriter = csv.writer(csv_out_file)
            next(freader)
            prevType = 0
            prevPrice = 0
            prev_row_list = []
            filtered_list = []
            for row_list in freader:
                price = row_list[0].strip() # 0번째는 가격, strip으로 문자열 양끝 공백, 탭, 개행문자 제거
                type = row_list[2].strip()  # 2번째는 type (0이면 파는, 1이면 사는)
                if prevType == '0' and type == '1':
                    timeStamp = row_list[3].strip() # 현재 시간
                    fwriter.writerow(prev_row_list) # 시세를 계산할 판매 희망 최소 가격
                    fwriter.writerow(row_list) # 시세를 계산할 구매 희망 최대 가격
                    marketPrice = (int(prevPrice)+int(price))/2     # 시세
                    print (marketPrice)
                    filtered_list.append('marketPrice')
                    filtered_list.append(timeStamp)
                    filtered_list.append(marketPrice)
                    print(filtered_list)
                    fwriter.writerow(filtered_list)
                    filtered_list = []  # filtered_list 초기화
                prevType = type # 현재 type을 prevType에 저장
                prevPrice = price   # 현재 price를 prevPrice에 저장
                prev_row_list = row_list # 현재 row_list를 prev_row_list에 저장

def marketPrice():
    input_file = "marketPriceSource.csv"
    output_file = "marketPrice.csv"

    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'w', newline='') as csv_out_file:
            freader = csv.reader(csv_in_file)
            fwriter = csv.writer(csv_out_file)
            next(freader)
            marketPriceList = []

            for row_list in freader:
                tag = str(row_list[0]).strip()  # marketPrice인 row를 찾기 위해 tag 붙임.
                if tag == 'marketPrice':
                    marketPriceList.append(row_list[1].strip())
                    marketPriceList.append(row_list[2].strip())
                    fwriter.writerow(marketPriceList)
                    marketPriceList = []    # marketPriceList 초기화

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

def  summaryByMonth():
    print("output is 1 overall tables")
    print("profit's 0 range is -0.00001 < x < 0.00001 ....... ")
    print()
    print()
    
    for i in range(1,8):
        globals()['df{}'.format(i)] = pd.read_csv("/Users/hamin/bithumb_bot/data/2018-0{}-btc-krw.csv".format(i))
        globals()['df{}'.format(i)]['timestamp'] = pd.to_datetime(globals()['df{}'.format(i)]['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
        print("caclulation number of transaction")
        
        # quantity에 부호 붙이기
        for j, row in globals()['df{}'.format(i)].iterrows(): 
            if row["side"]==0:
                row["quantity"]=-row["quantity"]
                globals()['df{}'.format(i)].at[j,'sign_quantity'] = row["quantity"]
        
        globals()['sign_quantity_cumsum{}'.format(i)]=globals()['df{}'.format(i)]["sign_quantity"].cumsum()
        
        print("caclulation profit")
        
        globals()['amount_cumsum{}'.format(i)]=globals()['df{}'.format(i)]["amount"].cumsum()
        globals()['sign_quantity_cumsum{}'.format(i)] = globals()['sign_quantity_cumsum{}'.format(i)].astype('float16')
        globals()['cumsum_df{}'.format(i)] = pd.concat([globals()['df{}'.format(i)],globals()['sign_quantity_cumsum{}'.format(i)],globals()['amount_cumsum{}'.format(i)]],axis=1)
        globals()['cumsum_df{}'.format(i)].columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum']
        globals()['cumsum_df_zero_point{}'.format(i)]=globals()['cumsum_df{}'.format(i)][ (globals()['cumsum_df{}'.format(i)]['sign_quantity_cumsum(coin)'] < 0.00001) & (globals()['cumsum_df{}'.format(i)]['sign_quantity_cumsum(coin)'] > -0.00001)]
        globals()['compare{}'.format(i)]=globals()['cumsum_df_zero_point{}'.format(i)]['amount_cumsum']
        globals()['compare{}'.format(i)]=globals()['compare{}'.format(i)].shift(1)[:]
        globals()['cumsum_df_zero_point{}'.format(i)] = pd.concat([globals()['cumsum_df_zero_point{}'.format(i)],globals()['compare{}'.format(i)]],axis=1)
        globals()['cumsum_df_zero_point{}'.format(i)] = globals()['cumsum_df_zero_point{}'.format(i)].fillna(0)
        globals()['cumsum_df_zero_point{}'.format(i)].columns = ['timestamp', 'quantity', 'price', 'fee', 'amount', 'side', 'sign_quantity', 'sign_quantity_cumsum(coin)', 'amount_cumsum', 'compare']
        globals()['cumsum_df_zero_point{}'.format(i)]['point_amount_cumsum'] = globals()['cumsum_df_zero_point{}'.format(i)]['amount_cumsum'] - globals()['cumsum_df_zero_point{}'.format(i)]['compare']
        globals()['cumsum_df_zero_point{}'.format(i)]=globals()['cumsum_df_zero_point{}'.format(i)].fillna(0)

        ## converting timestamp to detailed date column
        globals()['df{}'.format(i)]['timestamp_month_name'] = globals()['df{}'.format(i)]['timestamp'].dt.month_name() # 월(문자)
        globals()['df{}'.format(i)]['timestamp_year']       = globals()['df{}'.format(i)]['timestamp'].dt.year         # 연(4자리숫자)
        globals()['df{}'.format(i)]['timestamp_month']      = globals()['df{}'.format(i)]['timestamp'].dt.month        # 월(숫자)
        globals()['df{}'.format(i)]['timestamp_month_name'] = globals()['df{}'.format(i)]['timestamp'].dt.month_name() # 월(문자)
        globals()['df{}'.format(i)]['timestamp_day']        = globals()['df{}'.format(i)]['timestamp'].dt.day          # 일(숫자)
        globals()['df{}'.format(i)]['timestamp_time']       = globals()['df{}'.format(i)]['timestamp'].dt.time         # HH:MM:SS(문자)
        globals()['df{}'.format(i)]['timestamp_hour']       = globals()['df{}'.format(i)]['timestamp'].dt.hour         # 시(숫자)
        globals()['df{}'.format(i)]['timestamp_minute']     = globals()['df{}'.format(i)]['timestamp'].dt.minute       # 분(숫자)
        globals()['df{}'.format(i)]['timestamp_second']     = globals()['df{}'.format(i)]['timestamp'].dt.second       # 초(숫자)
        globals()['df{}_1'.format(i)] = globals()['df{}'.format(i)].copy()
        globals()['df{}_1'.format(i)] = globals()['df{}_1'.format(i)][globals()['df{}_1'.format(i)]['amount'] > 0]
        globals()['group_day_amount_positive{}'.format(i)] = globals()['df{}_1'.format(i)]['amount']

        print("caclulation positive and negative amount")

        ## creating 'hour - earning amount' connection
        globals()['df{}_2'.format(i)] = globals()['df{}'.format(i)].copy()
        globals()['df{}_2'.format(i)] = globals()['df{}_2'.format(i)][globals()['df{}_2'.format(i)]['amount'] < 0]
        globals()['group_day_amount_negative{}'.format(i)] = globals()['df{}_2'.format(i)]['amount']
        globals()['df{}_1'.format(i)] = globals()['df{}'.format(i)].copy()
        globals()['df_p_amount_{}_1'.format(i)] = globals()['df{}_1'.format(i)][globals()['df{}_1'.format(i)]['amount'] > 0]
        globals()['df{}_1'.format(i)] = globals()['df{}'.format(i)].copy()
        globals()['df_n_amount_{}_1'.format(i)] = globals()['df{}_1'.format(i)][globals()['df{}_1'.format(i)]['amount'] < 0]

        table_by_month = {
            '2018-01': [len(df1), len(group_day_amount_positive1), len(group_day_amount_negative1), np.nan, np.nan, df_p_amount_1_1['amount'].sum(), df_n_amount_1_1['amount'].sum()],
            '2018-02': [len(df2), len(group_day_amount_positive2), len(group_day_amount_negative2), cumsum_df_zero_point2.iloc[-1]['amount_cumsum'], cumsum_df_zero_point2.iloc[-1]['point_amount_cumsum'], df_p_amount_2_1['amount'].sum(), df_n_amount_2_1['amount'].sum()],
            '2018-03': [len(df3), len(group_day_amount_positive3), len(group_day_amount_negative3), cumsum_df_zero_point3.iloc[-1]['amount_cumsum'], cumsum_df_zero_point3.iloc[-1]['point_amount_cumsum'], df_p_amount_3_1['amount'].sum(), df_n_amount_3_1['amount'].sum()],
            '2018-04': [len(df4), len(group_day_amount_positive4), len(group_day_amount_negative4), np.nan, np.nan, df_p_amount_4_1['amount'].sum(), df_n_amount_4_1['amount'].sum()],
            '2018-05': [len(df5), len(group_day_amount_positive5), len(group_day_amount_negative5), cumsum_df_zero_point5.iloc[-1]['amount_cumsum'], cumsum_df_zero_point5.iloc[-1]['point_amount_cumsum'], df_p_amount_5_1['amount'].sum(), df_n_amount_5_1['amount'].sum()],
            '2018-06': [len(df6), len(group_day_amount_positive6), len(group_day_amount_negative6), cumsum_df_zero_point6.iloc[-1]['amount_cumsum'], cumsum_df_zero_point6.iloc[-1]['point_amount_cumsum'], df_p_amount_6_1['amount'].sum(), df_n_amount_6_1['amount'].sum()],
            '2018-07': [len(df7), len(group_day_amount_positive7), len(group_day_amount_negative7), cumsum_df_zero_point7.iloc[-1]['amount_cumsum'], cumsum_df_zero_point7.iloc[-1]['point_amount_cumsum'], df_p_amount_7_1['amount'].sum(), df_n_amount_7_1['amount'].sum()],
        }
        table_by_month = pd.DataFrame(table_by_month, index=['# of trans.', '# of buy trans.', '# of sell trans.', 'cumsum_profit', 'point_cumsum_profit', 'positive amount', 'negative amount'])
        table_by_month.to_csv("/Users/hamin/bithumb_bot/table/bithumb-overall-SummaryByMonth.csv", header=True, index=True, encoding = 'utf-8')
        print()
        print("/Users/hamin/bithumb_bot/table/bithumb-overall-SummaryByMonth.csv generating")
        print()
        print()
        print("bithumb-overall-SummaryByMonth")
        print(table_by_month)

# orderbook에서 데이터를 추출.
marketPriceSource()

# marketPriceSource()에서 추출된 데이터 csv로 market price 테이블 생성.
marketPrice()

# time - profit 그래프 생성
profitGraphGenerator()

# 달 별 highlight를 summuarize
summaryByMonth()