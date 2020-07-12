import pandas as pd
import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, savefig
import time
import csv
import sys
# import seaborn as sns

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

def marketPriceGraphGenerator():
    df = pd.read_csv("/Users/hamin/bithumb_analysis/data/marketPrice.csv")
    # 전체 시세
    priceGraph = df.plot(title="marketPrice May", legend=True)
    priceGraph.set_xlabel('Day')     # x축 정보 표시
    priceGraph.set_ylabel('Price(10 million krw)')     # y축 정보 표시
    plt.savefig('/Users/hamin/bithumb_analysis/graph/marketPriceMay.png', dpi=300)

    # 전체 시세
    # x = ["{}월".format(i + 1) for i in range(12)]
    priceGraph = df.plot(title="market price May", legend=True)
    priceGraph.set_xlabel('Day(End of Day)')     # x축 정보 표시
    priceGraph.set_ylabel('Price(1 million krw)')     # y축 정보 표시
    # priceGraph.legend('price may')     # 범례 표시
    # plt.xscale('linear')
    # priceGraph.set_xticks([np.1,np.2,np.3,np.4,np.5,np.6,np.7,np.8,np.9,np.10,np.11,np.12,np.13,np.14,np.15,np.16,np.17,np.18,np.19,np.20,np.21,np.22,np.23,np.24,np.25,np.26,np.27,np.28,np.29,np.30,np.31])
    priceGraph.set_xticklabels(['$0$','$0$','$4$','$8$','$12$','$16$','$20$','$24$','$28$','$31$'])
    priceGraph.set_yticklabels(['$0$','$8.0$','$8.5$','$9.0$','$9.5$','$10.0$','$10.5$'])
    plt.savefig('/Users/hamin/bithumb_analysis/graph/marketPriceMay.png', dpi=300)

    ## converting timestamp column type 'object' to 'datetime'
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
    df.dtypes

    df['Timestamp_date'] = df['Timestamp'].dt.day          # 일(숫자)
    df['Timestamp_hour'] = df['Timestamp'].dt.hour         # 시(숫자)
    df['Timestamp_minute'] = df['Timestamp'].dt.minute       # 분(숫자)
    df['Timestamp_second'] = df['Timestamp'].dt.second       # 초(숫자)

    ## creating 'hour - amount' connection
    group_date_Price = df['Price'].groupby(df['Timestamp_date'])
    group_hour_Price = df['Price'].groupby(df['Timestamp_hour'])
    group_minute_Price = df['Price'].groupby(df['Timestamp_minute'])

    # date 별 시세 평균
    datePriceGraph = group_date_Price.mean().plot(title="Daily marketPrice", marker='o')
    datePriceGraph.set_xlabel('Day(End of Day)')     # x축 정보 표시
    datePriceGraph.set_ylabel('Price(1 million krw)')     # y축 정보 표시
    datePriceGraph.set_yticklabels(['$0$','$8.0$','$8.5$','$9.0$','$9.5$','$10.0$','$10.5$'])
    plt.savefig('/Users/hamin/bithumb_analysis/graph/dailyMarketPrice.png', dpi=300)

    # hour 별 시세 평균
    hourPriceGraph = group_hour_Price.mean().plot(title="Hourly marketPrice", marker='o')
    hourPriceGraph.set_xlabel('Hour')
    hourPriceGraph.set_ylabel('Price (1 thousand krw)')
    hourPriceGraph.set_yticklabels(['$0$','$9,025$','$9,050$','$9,075$','$9,100$','$9,125$','$9,150$','$9,175$','$9,200$'])
    plt.savefig('/Users/hamin/bithumb_analysis/graph/hourlyMarketPrice.png', dpi=300)

    # min 별 시세 평균
    minutePriceGraph = group_minute_Price.mean().plot(title="Minute marketPrice", marker='o')
    minutePriceGraph.set_xlabel('Minute')
    minutePriceGraph.set_ylabel('Price (1 thousand krw)')
    minutePriceGraph.set_yticklabels(['$0$','$9,095$','$9,100$','$9,105$','$9,110$','$9,115$'])
    plt.savefig('/Users/hamin/bithumb_analysis/graph/minuteMarketPrice.png', dpi=300)

def totalTransactionCount():
    df = pd.read_csv("/Users/hamin/bithumb_analysis/include/2018-05-btc-krw.csv")
    ## converting timestamp column type 'object' to 'datetime'
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
    # df.dtypes

    ## converting timestamp to detailed date column
    df['timestamp_year_month_day'] = df['timestamp'].dt.date         # YYYY-MM-DD(문자)
    df['timestamp_year'] = df['timestamp'].dt.year         # 연(4자리숫자)
    df['timestamp_month'] = df['timestamp'].dt.month        # 월(숫자)
    df['timestamp_month_name'] = df['timestamp'].dt.month_name() # 월(문자)

    df['timestamp_day'] = df['timestamp'].dt.day          # 일(숫자)
    df['timestamp_time'] = df['timestamp'].dt.time         # HH:MM:SS(문자)
    df['timestamp_hour'] = df['timestamp'].dt.hour         # 시(숫자)
    df['timestamp_minute'] = df['timestamp'].dt.minute       # 분(숫자)
    df['timestamp_second'] = df['timestamp'].dt.second       # 초(숫자)

    ## creating 'hour - amount' connection
    group_hour_amount = df['amount'].groupby(df['timestamp_hour'])

    ## creating 'hourly - buy amount' connection
    df2 = df.copy()
    df2 =df2[df2['amount'] > 0]
    group_hour_amount_positive = df2['amount'].groupby(df2['timestamp_hour'])

    ## creating 'hour - buy amount' connection
    df3 = df.copy()
    df3 = df3[df3['amount'] < 0]
    group_hour_amount_negative = df3['amount'].groupby(df3['timestamp_hour'])

    # 시간별 절대값 총합
    # negative는 buy
    # positive는 sell
    absolute_negative_sum = group_hour_amount_negative.sum()
    absolute_negative_sum = absolute_negative_sum * (-1)
    # total 은 sell - buy
    absolute_total_amount = absolute_negative_sum+group_hour_amount_positive.sum()

    ## 시간별 계산 table 생성
    dfs = [group_hour_amount.size(), group_hour_amount.sum(), group_hour_amount_positive.size(), group_hour_amount_positive.sum(), group_hour_amount_negative.size(), group_hour_amount_negative.sum(), absolute_total_amount, absolute_negative_sum]
    day_df_final = reduce(lambda left,right: pd.merge(left,right,on='timestamp_hour'), dfs)
    day_df_final.columns = [ "Hourly transaction", "Hourly sell-buy", "Hourly sell transaction", "Hourly sell", "Hourly buy transaction", "Hourly buy", "Hourly total sell", "Hourly absolute total buy"]

    day_df_final.to_csv("/Users/hamin/bithumb_analysis/table/hour_result_table.csv", header=True, index=True, encoding = 'utf-8')

    day_df_final[['Hourly transaction', 'Hourly sell transaction', 'Hourly buy transaction']].plot(title='Hourly transaction count', marker='o')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/Hourly transaction count.png', dpi=300)

    hourTransGraph = day_df_final[['Hourly sell transaction', 'Hourly buy transaction']].plot.bar(title='Hourly transaction count', stacked=True)
    hourTransGraph.set_xlabel('Hour')
    hourTransGraph.set_ylabel('Count')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/Hourly transaction count(Stacked).png', dpi=300)

    hourTransBarGraph = day_df_final[['Hourly sell transaction', 'Hourly buy transaction']].plot.bar(title='Hourly transaction count(Bar)')
    hourTransBarGraph.set_xlabel('Hour')
    hourTransBarGraph.set_ylabel('Count')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/Hourly transaction count(Bar).png', dpi=300)

    # Minute
    ## creating 'minute - amount' connection
    group_minute_amount = df['amount'].groupby(df['timestamp_minute'])

    # Date
    # Creating 'date - amount' connection
    group_date_amount = df['amount'].groupby(df['timestamp_day'])

    # creating 'minute' - buy amount' connection
    df2 = df.copy()
    df2 =df2[df2['amount'] > 0]
    group_minute_amount_positive = df2['amount'].groupby(df2['timestamp_minute'])

    # creating 'date' - buy amount' connection
    df2 = df.copy()
    df2 =df2[df2['amount'] > 0]
    group_date_amount_positive = df2['amount'].groupby(df2['timestamp_day'])

    # creating 'minute - buy amount' connection
    df3 = df.copy()
    df3 = df3[df3['amount'] < 0]
    group_minute_amount_negative = df3['amount'].groupby(df3['timestamp_minute'])

    ## creating 'date - buy amount' connection
    df3 = df.copy()
    df3 = df3[df3['amount'] < 0]
    group_date_amount_negative = df3['amount'].groupby(df3['timestamp_day'])

    # minute 별 절대값 총합
    # negative는 buy
    absolute_minute_negative_sum = group_minute_amount_negative.sum()
    absolute_minute_negative_sum = absolute_minute_negative_sum * (-1)
    # total 은 sell - buy
    absolute_minute_total_amount = absolute_minute_negative_sum+group_minute_amount_positive.sum()
    # absolute_minute_total_amount

    # date 별 절대값 총합
    # negative는 buy
    absolute_date_negative_sum = group_date_amount_negative.sum()
    absolute_date_negative_sum = absolute_date_negative_sum * (-1)
    # total 은 sell - buy
    absolute_date_total_amount = absolute_date_negative_sum+group_date_amount_positive.sum()

    # minute 별 계산 table 생성
    dfs = [group_minute_amount.size(), group_minute_amount.sum(), group_minute_amount_positive.size(), group_minute_amount_positive.sum(), group_minute_amount_negative.size(), group_minute_amount_negative.sum(), absolute_minute_total_amount, absolute_minute_negative_sum]
    day_df_minute_final = reduce(lambda left,right: pd.merge(left,right,on='timestamp_minute'), dfs)
    day_df_minute_final.columns = [ "Minute transaction", "Minute sell-buy", "Minute sell transaction", "Minute sell", "Minute buy transaction", "Minute buy", "Minute total sell", "Minute absolute total buy"]

    # date 별 계산 table 생성
    dfs = [group_date_amount.size(), group_date_amount.sum(), group_date_amount_positive.size(), group_date_amount_positive.sum(), group_date_amount_negative.size(), group_date_amount_negative.sum(), absolute_date_total_amount, absolute_date_negative_sum]
    day_df_date_final = reduce(lambda left,right: pd.merge(left,right,on='timestamp_day'), dfs)
    day_df_date_final.columns = [ "Date transaction", "Date sell-buy", "Date sell transaction", "Date sell", "Date buy transaction", "Date buy", "Date total sell", "Date absolute total buy"]

    # table 저장하기
    day_df_minute_final.to_csv("/Users/hamin/bithumb_analysis/table/minute_result_table.csv", header=True, index=True, encoding = 'utf-8')

    # table 저장하기
    day_df_date_final.to_csv("/Users/hamin/bithumb_analysis/table/date_result_table.csv", header=True, index=True, encoding = 'utf-8')

    # Minute - transaction 그래프 그리기
    day_df_minute_final[['Minute transaction', 'Minute sell transaction', 'Minute buy transaction']].plot(title='Transaction count per minute', marker='o')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/Transaction_count_per_minute.png', dpi=300)

    # Minute - transaction 그래프 그리기
    day_df_minute_final[['Minute transaction', 'Minute sell transaction', 'Minute buy transaction']].plot(title='Transaction count per minute', marker='o')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/Transaction_count_per_minute.png', dpi=300)

    minuteTransBarGraph = day_df_minute_final[['Minute sell transaction', 'Minute buy transaction']].plot.bar(title='Transaction count per minute(Bar)')
    minuteTransBarGraph.set_xlabel('Minute')
    minuteTransBarGraph.set_ylabel('Transaction')
    minuteTransBarGraph.set_xticklabels(['$0$','','','','','','','','','','$10$','','','','','','','','','','$20$','','','','','','','','','','$30$','','','','','','','','','','$40$','','','','','','','','','','$50$'])
    plt.savefig('/Users/hamin/bithumb_analysis/graph/Transaction_count_per_minute(Bar).png', dpi=300)

    # Date - transaction 그래프 그리기
    day_df_date_final[['Date transaction', 'Date sell transaction', 'Date buy transaction']].plot(title='Transaction count per day', marker='o')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/Transaction_count_per_day.png', dpi=300)
    dayTransGraph = day_df_date_final[['Date sell transaction', 'Date buy transaction']].plot.bar(title='Transaction count per day', stacked=True)
    dayTransGraph.set_xlabel('Date')
    dayTransGraph.set_ylabel('Transaction')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/Transaction_count_per_day(Stacked).png', dpi=300)

    dayTransBarGraph = day_df_date_final[['Date sell transaction', 'Date buy transaction']].plot.bar(title='Transaction count per day(Bar)')
    dayTransBarGraph.set_xlabel('Date')
    dayTransBarGraph.set_ylabel('Transaction')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/Transaction_count_per_day(Bar).png', dpi=300)

def priceSideMapping():
    df = pd.read_csv("/Users/hamin/bithumb_analysis/table/2018-05-btc-krw.csv")
    # creating 'price - side' connection - price가 같은것 끼리 묶는다.
    side_price = df['side'].groupby(df['price'])

    # 가격을 10 구간 으로 구간 나눔
    factor_price=pd.cut(df.price,10)

    group_side_by_priceGroup = df['side'].groupby(factor_price)

    group_side_by_priceGroup_table = [group_side_by_priceGroup.size(), group_side_by_priceGroup.mean(), group_side_by_priceGroup.sum()]
    side_by_priceGroup = reduce(lambda left, right: pd.merge(left,right, on='price'), group_side_by_priceGroup_table)
    side_by_priceGroup.columns = ["# of side", "mean of side", "sum of side"]
    
    side_by_priceGroup.to_csv("/Users/hamin/bithumb_analysis/table/side_by_price_Group.csv")

    # priceGroup-side 간 그래프
    side_by_priceGroup.plot(title='side by price Group', marker='o')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/side_by_price_Group.png', dpi=300)

    # priceGroup-mean of side 간 그래프 (0.5보다 크면 산 것이 더 많다는 것)
    side_by_priceGroup.plot(y='mean of side',title='mean of side by price Group', marker='o')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/mean_of_side_by_price_Group.png', dpi=300)

def priceAmountMapping():
    df = pd.read_csv("/Users/hamin/bithumb_analysis/include/2018-05-btc-krw.csv")
    
    # creating 'price - amount' connection - price가 같은것 끼리 묶는다.
    amount_price = df['amount'].groupby(df['price'])

    # 가격을 10 구간 으로 구간 나눔
    factor_price=pd.cut(df.price,10)


    group_amount_by_priceGroup = df['amount'].groupby(factor_price)

    group_amount_by_priceGroup_table = [group_amount_by_priceGroup.size(), group_amount_by_priceGroup.mean(), group_amount_by_priceGroup.sum()]
    amount_by_priceGroup = reduce(lambda left, right: pd.merge(left,right, on='price'), group_amount_by_priceGroup_table)
    amount_by_priceGroup.columns = ["# of amount", "mean of amount", "sum of amount"]

    amount_by_priceGroup.to_csv("/Users/hamin/bithumb_analysis/table/amount_by_price_Group.csv")

    # priceGroup-amount 간 그래프
    amount_by_priceGroup.plot(title='amount by price Group', marker='o')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/amount_by_price_Group.png', dpi=300)

    # priceGroup-# of amount 간 그래프
    amount_by_priceGroup.plot(y='# of amount',title='# of amount by price Group', marker='o')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/#_of_amount_by_price_Group.png', dpi=300)

    # priceGroup-mean of amount 간 그래프
    amount_by_priceGroup.plot(y='mean of amount',title='mean of amount by price Group', marker='o')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/mean_of_amount_by_price_Group.png', dpi=300)

    # priceGroup-sum of amount 간 그래프
    amount_by_priceGroup.plot(y='sum of amount',title='sum of amount by price Group', marker='o')
    plt.savefig('/Users/hamin/bithumb_analysis/graph/sum_of_amount_by_price_Group.png', dpi=300)

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

# market price data로 그래프 그리기.
marketPriceGraphGenerator()

# totalTransactionCount.
totalTransactionCount()

# price-side mapping graph.
priceSideMapping()

# price-amount mapping graph.
priceAmountMapping()

# time - profit 그래프 생성.
profitGraphGenerator()

# 달 별 highlight를 summuarize.
summaryByMonth()