#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import matplotlib
import math

#from mpl_toolkits.basemap import Basemap

#from pyspark import SparkContext, SparkConf
#from pyspark.sql import SQLContext

#######################################
def csv_file (fn):
    return os.path.join (csv_dir, fn+'.csv')

def fig_file (fn):
    #return os.path.join (fig_dir, fn+'.png')
    return os.path.join (fig_dir, fn+'.pdf')

def pickle_file (fn):
    #return os.path.join (csv_dir, fn+'.fi.pickle')
    return os.path.join (csv_dir, fn+'.slim.pk')
#######################################

def groupby_dates(df):

    _list = ['DOWNLOAD_BANDWIDTH', 'UPLOAD_BANDWIDTH', 'UDP_JITTER', 'UDP_LOSS']
    
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'], format='%Y-%m-%d %H:%M:%S')
    group_dates = df.set_index('TIMESTAMP').groupby(pd.TimeGrouper(freq='D'))
    
    for fi in _list:
        fn = '%s/dates_%s.csv' % (csv_dir, fi)
        _df = group_dates[fi].agg([min, max, np.mean, np.std, len]) 
        _df.to_csv( fn, columns=['min', 'max','mean','std','len'] )
        print fn

def dump_stats_network_id (df,category,period):
	
    ''' '3': LTE, '2': WiFi, '1': 3G, '0': 2G
    '''
    frame = []
    fn = category + ('_%s.csv' % period)
    fn = os.path.join (csv_dir, fn)
    for _id in network.keys():
        
        group = df[(df['NETWORK_ID']== _id) & (df[category]>0)].set_index('TIMESTAMP').groupby(pd.TimeGrouper(freq=period))
        id_df = group[category].agg([min, max, np.mean, np.std, 'count']).round(2)
        id_df['quant95'] = group[category].quantile(.95).round(2)
        id_df['quant05'] = group[category].quantile(.05).round(2)
        
        col_name = [(network[_id]+'-'+row) for row in id_df.columns]
        id_df.columns = col_name
        
        frame.append (id_df)

    result = pd.concat(frame, axis=1)
    result.to_csv(fn)
    
    return '+ '+fn

'''
def plot_week_dist (df,net_id,category):
	
    group = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').groupby(pd.TimeGrouper(freq="W"))
    #group = group[(group['TIMESTAMP'] > '2015-3-16') & (df['TIMESTAMP'] <= '2015-3-22')]
    
    for gr in group:
        
        week_cnt = len((gr[1])[category].index)
    	
        if (not week_cnt): continue

    	week_date = str((gr[0])).split(' ')[0]
    	week_title = 'Week of %s,  %s cnt: %s' % (week_date, network[net_id], week_cnt)
	
    	fn = fig_file ('%s-%s-week-dist' % (week_date, network[net_id]))

    	fig, ax = plt.subplots()
    	bin_size = 2
    	_label = '%dMB bin' % bin_size
    	bin_df = return_throughput_bin_dist (gr[1], category, week_cnt, bin_size)
    	bin_df.plot(linestyle=('solid'), color=('black'), label=_label, ylim=(0,0.1), xlim=(0,400), ax=ax)
    	
    	plt.title(week_title)
    	plt.legend()
    	plt.xlabel('Throughput (Mbps)')
    	plt.ylabel('Frequency (Ratio)')
    	plt.savefig (fn, bbox_inches='tight')
    	plt.gcf().clear()
    
    	print '+ '+fn

def plot_month_dist (df,net_id,category):
	
    group = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').groupby(pd.TimeGrouper(freq="M"))
    
    for gr in group:
        month_cnt = len((gr[1])[category].index)
        if (not month_cnt): continue
        
        month = '%d-%02d' % (gr[0].year, gr[0].month)
        total_cnt = len(gr[1].index)
        month_title = '%s,  %s cnt: %s' % (month, network[net_id], total_cnt)
        
        fn = fig_file ('%s-%s-month-dist' % (month, network[net_id]))
        
        fig, ax = plt.subplots()
        bin_size = 2
        _label = '%dMB bin' % bin_size
        bin_df = return_throughput_bin_dist (gr[1], category, total_cnt, bin_size)
        bin_df.plot(linestyle=('solid'), color=('black'), label=_label, ylim=(0,0.1), xlim=(0,400), ax=ax)
        
        plt.title(month_title)
    	plt.legend()
    	plt.xlabel('Throughput (Mbps)')
    	plt.ylabel('Frequency (Ratio)')
    	plt.savefig (fn, bbox_inches='tight')
        plt.gcf().clear()

    	print '+ '+fn
'''

def return_month_hour_bin_dist (df, category, total_cnt, bin_size):
    
    bin_values = range (0,302,bin_size) 
    return (df[category].value_counts(bins=bin_values).sort_index()).div(total_cnt)

    #df.plot.hist(bins=200, normed=True, cumulative=True, histtype='step', linestyle=('solid'),  title=_title, xlim=(0,400))
    
    #bins = (1, 10, 20, 30, 40, 50, 60)
    #binned_data = df1.groupby(pd.cut(df1.DOWNLOAD_BANDWIDTH, bins)).count()
    #print binned_data.values

def plot_month_dist_hours (df,net_id,category):
	
    group_busy = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').between_time('09:00','18:00').groupby(pd.TimeGrouper(freq="M"))
    group_non_busy = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').between_time('00:00','07:00').groupby(pd.TimeGrouper(freq="M"))

    if len(group_busy) != len(group_non_busy): exit(-1)
    
    for busy, non_busy in zip (group_busy, group_non_busy):
    	busy_month_cnt = len((busy[1])[category].index)
    	non_busy_month_cnt = len((non_busy[1])[category].index)
    
    	if (not busy_month_cnt): continue
    	if (not non_busy_month_cnt): continue
    
    	month = '%d-%02d' % (busy[0].year, busy[0].month)
    	total_cnt = len(busy[1].index) + len(non_busy[1].index)
    	month_title = '%s,  %s cnt: %s' % (month, network[net_id], total_cnt)
    	
    	fn = fig_file ('%s-%s-month-hour-dist' % (month, network[net_id]))
    	fig, ax = plt.subplots()
    	
    	plt.subplot(2,1,1)
    	bin_size = 2
    	_label = '%dMB bin, 00:00-07:00, cnt: %d' % (bin_size, len(busy[1].index))
    	bin_df = return_month_hour_bin_dist (busy[1], category, total_cnt, bin_size)
    	bin_df.plot(linestyle=('solid'), color=('black'), ylim=(0,0.1), xlim=(0,400), label=_label)
    	plt.legend()
    	plt.title(month_title)
    
    	plt.subplot(2,1,2)
    	bin_size = 10 
    	_label = '%dMB bin, 09:00-18:00, cnt: %d' % (bin_size, len(non_busy[1].index))
    	bin_df = return_month_hour_bin_dist (non_busy[1], category, total_cnt, bin_size)
    	bin_df.plot(linestyle=('solid'), color=('red'), ylim=(0,0.05), xlim=(0,400), label=_label)
    	
    	plt.legend()
    	plt.xlabel('Throughput (Mbps)')
    	plt.ylabel('Frequency (Ratio)')
    	plt.savefig (fn, bbox_inches='tight')
     	plt.gcf().clear()

    	print '+ '+fn

def plot_month_dist_hours_selected (df,net_id,category):
	
    group_busy = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').between_time('09:00','18:00').groupby(pd.TimeGrouper(freq="M"))
    group_non_busy = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').between_time('00:00','07:00').groupby(pd.TimeGrouper(freq="M"))

    if len(group_busy) != len(group_non_busy): exit(-1)
    
    selected_month = ['2013-03', '2014-01', '2014-06', '2015-01', '2016-06']

    fn = fig_file ('%s-month-hour-dist' % (network[net_id]))
    plt.figure()
    fig, ax = plt.subplots(figsize=(20,30))
    
    _index=1
    for busy, non_busy in zip (group_busy, group_non_busy):
    	busy_month_cnt = len((busy[1])[category].index)
    	non_busy_month_cnt = len((non_busy[1])[category].index)
    
    	if (not busy_month_cnt): continue
    	if (not non_busy_month_cnt): continue
    
    	month = '%d-%02d' % (busy[0].year, busy[0].month)
        month_title = '%s %2d' % (month_index[busy[0].month], busy[0].year)
        if month not in selected_month: continue

        total_cnt = len(busy[1].index) + len(non_busy[1].index)
    	#month_title = '%s,  %s cnt: %s' % (month, network[net_id], total_cnt)
    	#fn = fig_file ('%s-%s-month-hour-dist' % (month, network[net_id]))
        #fig, ax = plt.subplots()
    	plt.subplot (5,1,_index); _index+=1
        #fig.set_size_inches (10,2)
        
        bin_size = 2 
        busy_label = '%dMB bin, Day: %d tests' % (bin_size, len(busy[1].index))
    	#df_busy = return_month_hour_bin_dist (busy[1], category, total_cnt, bin_size)
    	df_busy = return_month_hour_bin_dist (busy[1], category, len(busy[1].index), bin_size)
        
        bin_size = 2 
        non_busy_label = '%dMB bin, Night: %d tests' % (bin_size, len(non_busy[1].index))
    	#df_non_busy = return_month_hour_bin_dist (non_busy[1], category, total_cnt, bin_size)
    	df_non_busy = return_month_hour_bin_dist (non_busy[1], category, len(non_busy[1].index), bin_size)
    	
        P = df_busy.plot(style=['k-'], label=busy_label)
        df_non_busy.plot(style=['r--'], ylim=(0,0.065), xlim=(0,300), ax=P)
        P.set_axis_bgcolor('white')
        P.spines['left'].set_color('black')
        P.spines['bottom'].set_color('black')
        P.text(.9,.3,month_title, horizontalalignment='right', verticalalignment='bottom', transform=P.transAxes, fontsize=35, color='blue')
        leg = P.legend([busy_label, non_busy_label], loc='upper right', fontsize=35, frameon = True)
        leg.get_frame().set_facecolor('w')
        leg.get_frame().set_edgecolor('k')

        
        #P.spines['top'].set_color('black')
        #P.spines['right'].set_color('black')
        P.xaxis.set_ticks_position('bottom')
        P.yaxis.set_ticks_position('left')
        plt.yticks(color='black', fontsize=30)
        plt.xticks(color='black', fontsize=30)
        if _index == 4:
    	    plt.ylabel('Frequency (normalized)', fontsize=45, color='black')
        if _index == 6:
    	    plt.xlabel('Throughput (Mbps)', fontsize=45, color='black')
        
    plt.savefig (fn, bbox_inches='tight')
    plt.clf()
        
    print '+ '+fn

#gps graphs
#loss measurement dist

def return_bin_dist (df, category, total_cnt, bin_size, x_max):

    bin_values = range (0, x_max+bin_size, bin_size)
    return (df[category].value_counts(bins=bin_values).sort_index()).div(total_cnt)

def plot_week_dist (df,net_id,category):
	
    ''' '3': LTE, '2': WiFi, '1': 3G, '0': 2G
    '''
    group = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').groupby(pd.TimeGrouper(freq="W"))
    #group = group[(group['TIMESTAMP'] > '2015-3-16') & (df['TIMESTAMP'] <= '2015-3-22')]
    
    for gr in group:
        
        week_cnt = len((gr[1])[category].index)
    	
        if (not week_cnt): continue

    	week_date = str((gr[0])).split(' ')[0]
    	week_title = 'Week of %s,  %s cnt: %s' % (week_date, network[net_id], week_cnt)
	
    	fn = fig_file ('%s-%s-week-dist-%s' % (week_date, network[net_id], schema[category]))

    	fig, ax = plt.subplots()
    	bin_size = 2
        _label = '%dMB bin' % bin_size
        y_max = 0.1
        x_max = 400
        
        if schema[category] == 'loss':
            bin_size = 10
            _label = '%dms bin' % bin_size
            y_max = 0.8
            x_max = 200

        bin_df = return_bin_dist (gr[1], category, week_cnt, bin_size, x_max)
    	bin_df.plot(linestyle=('solid'), color=('black'), label=_label, ylim=(0,y_max), xlim=(0,x_max), ax=ax)
    	
    	plt.title(week_title)
    	plt.legend()

        plt.ylabel('Frequency (Ratio)')
        if schema[category] == 'loss':
            plt.xlabel('Loss (ms)')
        else:
            plt.xlabel('Throughput (Mbps)')

    	plt.savefig (fn, bbox_inches='tight')
    	plt.gcf().clear()
    
    	print '+ '+fn

def plot_month_dist (df,net_id,category):
    
    #group = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').groupby(pd.TimeGrouper(freq="M"))
    group = df[(df[category]>0)].set_index('date').groupby(pd.TimeGrouper(freq="M"))
    
    for gr in group:
        
        month_cnt = len((gr[1])[category].index)
        
        if (not month_cnt): continue
        
        month = '%d-%02d' % (gr[0].year, gr[0].month)
        total_cnt = len(gr[1].index)
        month_title = '%s, cnt: %s' % (month, total_cnt)
        fn = fig_file ('%s-month-dist-%s' % (month, schema[category]))
        
        
        fig, ax = plt.subplots()
        bin_size = 2
        _label = '%dMB bin' % bin_size
        y_max = 0.1
        x_max = 400
        
        if schema[category] == 'loss':
            bin_size = 10
            _label = '%dms bin' % bin_size
            y_max = 0.8
            x_max = 200
 
        bin_df = return_bin_dist (gr[1], category, total_cnt, bin_size, x_max)
        bin_df.plot(linestyle=('solid'), color=('black'), label=_label, ylim=(0,y_max), xlim=(0,x_max), ax=ax)
        
        plt.title(month_title)
        plt.legend()
        
        plt.ylabel('Frequency (Ratio)')
        if schema[category] == 'loss':
            plt.xlabel('Loss (ms)')
        else:
            plt.xlabel('Throughput (Mbps)')
        
        plt.savefig (fn, bbox_inches='tight')
    	plt.gcf().clear()
        print '+ '+fn

def return_throughput_bin_dist (df, category):

    bin_values = [0, 15, 75, 150, 300, 500]
    return df[category].value_counts(bins=bin_values).sort_index()

def plot_throughput_month_dist (df,net_id,category): #distribution: 15, 75, 150, 300, 300+ mbps
    # x-axis: time (month), y-axis: count, line-1: 0-15 bint count, line-2, etc.
    # circle size, line-1: 0-15 bint count, line-2, etc.

    #group = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').groupby(pd.TimeGrouper(freq="M"))
    group = df[(df[category]>0)].set_index('date').groupby(pd.TimeGrouper(freq="M"))

    frame = []
    for gr in group:
        
        month_cnt = len((gr[1])[category].index)
        if (not month_cnt): continue
        
        _df = return_throughput_bin_dist (gr[1], category).tolist()
        month = '%d-%02d' % (gr[0].year, gr[0].month)
        _df.insert(0, month)
        frame.append (_df)

    bin_df = pd.DataFrame (frame, columns=['date', 0, 15, 75, 150, 300]).set_index('date')
    
    month = '%d-%02d' % (gr[0].year, gr[0].month)
    month_title = 'dist'
    fn = fig_file ('device-dist-%s' % (schema[category]))
        
    fig, ax = plt.subplots()
    
    bin_df.plot()
    
    plt.title(month_title)
    plt.ylabel('Count')
    
    plt.savefig (fn, bbox_inches='tight')
    plt.gcf().clear()

    print bin_df.to_csv()

    print '+ '+fn
 
def plot_throughput_dist_table (df,net_id,category): #distribution: 15, 75, 150, 300, 300+ mbps
    # x-axis: time (year), y-axis: count, line-1: 0-15 bint count, line-2, etc.
    # circle size, line-1: 0-15 bint count, line-2, etc.

    newdf = df[(df['NETWORK_ID']== net_id) & (df[category]>300)]
    print newdf['TIMESTAMP'].values
    print len(newdf[category].index)

    group = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').groupby(pd.TimeGrouper(freq="12M"))
    
    frame = []
    for gr in group:
        
        yr_cnt = len((gr[1])[category].index)
        if (not yr_cnt): continue
        
        total_cnt = len(gr[1].index)
        _df = return_throughput_bin_dist (gr[1], category)
        
        print total_cnt
        print _df

        _df_percent = _df.div(total_cnt)*100
        _df = _df.tolist()

        yr = '%d' % (gr[0].year)
        _df.insert(0, yr)
        frame.append (_df)
        #print _df_percent

    bin_df = pd.DataFrame (frame, columns=['date', 0, 15, 75, 150, 300]).set_index('date')
    print bin_df.to_csv()

month_index = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',7:'Jan',8:'Aug',9:'Oct',10:'Oct',11:'Nov',12:'Dec'}

import seaborn as sns
 
def plot_test (df,net_id,category): #
    # x-axis:  y-axis:
    group = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').groupby(pd.TimeGrouper(freq="M"))
    
    frame = []
    all_frame = []
    for gr in group:
        
        yr_cnt = len((gr[1])[category].index)
        if (not yr_cnt): continue
        
        month = '%s-%2d' % (month_index[gr[0].month], gr[0].year-2000)
        total_cnt = len(gr[1].index)
 
        _mean = (gr[1])[category].mean().round(2)
        _quant5 = (gr[1])[category].quantile(.05).round(2)
        _quant95 = (gr[1])[category].quantile(.95).round(2)

        frame.append ([month, _mean, _quant5, _quant95])
        all_frame.append (gr[1][category].values)

    bin_df = pd.DataFrame (frame, columns=['date', 'Mean', '5th Percentile', '95th Percentile']).set_index('date')
    all_df = pd.DataFrame (all_frame).reset_index().T
    all_df.columns = bin_df.index.tolist()
    
    fn = fig_file ('%s-mean-5-95-dist-%s' % (network[net_id], schema[category]))
    fig, ax = plt.subplots()
    P = bin_df.plot(rot=65, style=['k-','k--','k:'])

    leg = P.legend(loc='upper right', fontsize=12, frameon = True)
    leg.get_frame().set_facecolor('w')
    leg.get_frame().set_edgecolor('k')
 
    P.set_axis_bgcolor('white')
    P.spines['left'].set_color('black')
    P.spines['bottom'].set_color('black')
    P.xaxis.set_ticks_position('bottom')
    P.yaxis.set_ticks_position('left')
    P.xaxis.label.set_color('black')
    P.yaxis.label.set_color('black')
    P.set_ylabel('Download Throughput (Mbps)', fontsize=14)
    P.set_xlabel ('')
    #plt.xticks(range(0,len(bin_df.index),1), bin_df.index.tolist(), color='black')
    plt.xticks(color='black', fontsize=11)
    plt.yticks(color='black', fontsize=13)
 
    for xc in [14,25]:
        plt.axvline(x=xc, color='grey', linestyle='-')
    #ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05),)
    P.annotate('Period 1', xy=(2, 1), xytext=(5, 230), fontsize=13, color='black')
    P.annotate('Period 2', xy=(2, 1), xytext=(17, 230), fontsize=13, color='black')
    P.annotate('Period 3', xy=(2, 1), xytext=(26, 230), fontsize=13, color='black')
    plt.savefig (fn, bbox_inches='tight')
    plt.gcf().clear()
    
    '''
    all_df.plot.box(rot=90, ylim=(0, 300))
    bin_df.plot.area(rot=90, stacked=False)
    
    ax = sns.heatmap(bin_df.T)
    for item in ax.get_yticklabels():
        item.set_rotation(0)
    for item in ax.get_xticklabels():
        item.set_rotation(90)
    '''
    #print bin_df.to_csv()
    print '+ '+fn

def plot_geo_month_dist(df, net_id, category):
    
    #group = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].set_index('TIMESTAMP').groupby(pd.TimeGrouper(freq="M"))
    group = df[(df['NETWORK_ID']== net_id) & (df[category]>0)].groupby(['TIMESTAMP','SUBLOCALITY']).reset_index()
    
    for gr in group:
        
        print (gr[1])[category].head(100)
        exit()

        month_cnt = len((gr[1])[category].index)
        
        if (not month_cnt): continue
        
        month = '%d-%02d' % (gr[0].year, gr[0].month)
        total_cnt = len(gr[1].index)
        month_title = '%s,  %s cnt: %s' % (month, network[net_id], total_cnt)
        fn = fig_file ('%s-%s-month-dist-%s' % (month, network[net_id], schema[category]))
        
        
        fig, ax = plt.subplots()
        bin_size = 2
        _label = '%dMB bin' % bin_size
        y_max = 0.1
        x_max = 400
        
        if schema[category] == 'loss':
            bin_size = 10
            _label = '%dms bin' % bin_size
            y_max = 0.8
            x_max = 200
 
        bin_df = return_bin_dist (gr[1], category, total_cnt, bin_size, x_max)
        bin_df.plot(linestyle=('solid'), color=('black'), label=_label, ylim=(0,y_max), xlim=(0,x_max), ax=ax)
        
        plt.title(month_title)
        plt.legend()
        
        plt.ylabel('Frequency (Ratio)')
        if schema[category] == 'loss':
            plt.xlabel('Loss (ms)')
        else:
            plt.xlabel('Throughput (Mbps)')
        
        plt.savefig (fn, bbox_inches='tight')
    	plt.gcf().clear()
        print '+ '+fn

def write_stats_network_id (df):
    
    #schema = ['DOWNLOAD_BANDWIDTH', 'UPLOAD_BANDWIDTH', 'UDP_LOSS']
    
    for cat in schema.keys():
        print dump_stats_network_id (df,cat,'3M')

def plot_trend_mobile_users():

    print 'plot_trend_mobile_users()'
    
    df = pd.read_csv(csv_file ('mobile-users-2012-2016')).set_index('date') 
    ''' 
    fn = fig_file ('mobile-users-bar') 
    plt.figure()
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, rot=90, title='2012-2016 mobile growth (stacked bar)')
    plt.xlabel('Month')
    plt.ylabel('Subscribers')
    plt.yticks(range(0,80000000,10000000),['0','10M','20M','30M','40M','50M','60M', '70M'])
    plt.savefig (fn, bbox_inches='tight')
    plt.gcf().clear()
    print '+ '+fn
    '''

    fn = fig_file('mobile-users') 
    plt.figure()
    fig, ax = plt.subplots()
   
    P = df.plot(rot=65, style=['ks-','ko--','k^:'] )
    #P = df.plot(rot=65, style=['ks-','ko-','k^-'] )
    #P = df.plot(rot=65, style=['k-','k--','k:'] )
    
    leg = P.legend(['2G', '3G', '4G LTE'], loc='upper left', fontsize=14, frameon = True)
    leg.get_frame().set_facecolor('w')
    leg.get_frame().set_edgecolor('k')
 
    P.set_axis_bgcolor('white')
    P.spines['left'].set_color('black')
    P.spines['bottom'].set_color('black')
    P.spines['top'].set_color('black')
    P.spines['right'].set_color('black')
    P.xaxis.set_ticks_position('bottom')
    P.yaxis.set_ticks_position('left')
    P.xaxis.label.set_color('black')
    P.yaxis.label.set_color('black')
    P.set_ylabel ('Number of subscribers', fontsize=15)
    P.set_xlabel ('', fontsize=15)
    plt.yticks(range(0,60000000,10000000),['0','10M','20M','30M','40M','50M'], color='black', fontsize=14)
    plt.xticks(color='black', fontsize=11)
    #plt.xticks(range(0,len(df.index),1), df.index.tolist())
    
    plt.savefig (fn, bbox_inches='tight')
    plt.clf()
    print '+ '+fn

def plot_trend_network():
    
    print 'plot_trend_network()'
    df = pd.read_csv(csv_file ('mobile-net')).set_index('year')
    
    fn = fig_file('mobile-net')
    plt.figure()
    fig, ax = plt.subplots()
   
    P = df.plot(rot='360', kind='bar', color='black', ylim=(0,1200), legend=[])
    P.set_axis_bgcolor('white')
    P.spines['left'].set_color('black')
    P.spines['bottom'].set_color('black')
    P.spines['top'].set_color('black')
    P.spines['right'].set_color('black')
    P.xaxis.set_ticks_position('bottom')
    P.yaxis.set_ticks_position('left')
    P.xaxis.label.set_color('black')
    P.yaxis.label.set_color('black')
    P.set_ylabel ('Max. download throughput (Mbps)', fontsize=15)
    P.set_xlabel ('', fontsize=15)
    P.annotate(' (384 Kbps)\n 2G CDMA', xy=(1, 1), xytext=(-0.3, 5), fontsize=11, color='black')
    P.annotate(' (14.4 Mbps)\n3G WCDMA', xy=(1, 1), xytext=(.6, 30), fontsize=11, color='black')
    P.annotate('(75 Mbps)\n4G LTE', xy=(1, 1), xytext=(1.75, 95), fontsize=11, color='black')
    P.annotate('(150 Mbps)\n4G LTE-A', xy=(1, 1), xytext=(2.7, 175), fontsize=11, color='black')
    P.annotate('    (500 Mbps)\n4G LTE-A Pro\n     Phase I', xy=(1, 1), xytext=(3.5, 520), fontsize=11, color='black')
    P.annotate('     (1 Gbps)\n4G LTE-A Pro\n     Phase II', xy=(1, 1), xytext=(4.5, 1020), fontsize=11, color='black')
    plt.yticks(color='black', fontsize=13)
    plt.xticks(color='black', fontsize=14)
    #plt.yticks(range(0,60000000,10000000),['0','10M','20M','30M','40M','50M'])
    #plt.xticks(range(0,len(df.index),1), df.index.tolist())
    
    plt.savefig (fn, bbox_inches='tight')
    plt.clf()
    print '+ '+fn

def agg_stats_network_id (fp):
    
    df_down_bw = pd.read_csv(csv_file ('DOWNLOAD_BANDWIDTH_3M'))
    df_up_bw = pd.read_csv(csv_file('UPLOAD_BANDWIDTH_3M'))
    
    df_bw = pd.concat([df_down_bw['TIMESTAMP'], df_down_bw['3g-mean'],df_down_bw['lte-mean'],df_down_bw['wifi-mean'],df_up_bw['3g-mean'],df_up_bw['lte-mean'],df_up_bw['wifi-mean']], axis=1, keys = ['bandwidth', '3g-mean-DOWN', 'lte-mean', 'wifi-mean', '3g-mean-UPLOAD', 'lte-mean', 'wifi-mean'])
    
    df_bw.to_string(justify='left')
    df_bw.to_csv (fp, index=False, sep='\t')
    fp.write ('\n')

    df_bw = pd.concat([df_down_bw['TIMESTAMP'], df_down_bw['3g-max'],df_down_bw['lte-max'],df_down_bw['wifi-max'],df_up_bw['3g-max'],df_up_bw['lte-max'],df_up_bw['wifi-max']], axis=1, keys = ['bandwidth', '3g-MAX-DOWN', 'lte-max', 'wifi-max', '3g-max-UPLOAD', 'lte-max', 'wifi-max'])
    df_bw.to_csv (fp, index=False, sep='\t')
    fp.write ('\n')

    df_bw = pd.concat([df_down_bw['TIMESTAMP'], df_down_bw['3g-std'],df_down_bw['lte-std'],df_down_bw['wifi-std'],df_up_bw['3g-std'],df_up_bw['lte-std'],df_up_bw['wifi-std']], axis=1, keys = ['bandwidth-STD', '3g-DOWN', 'lte', 'wifi', '3g-UPLOAD', 'lte', 'wifi'])

    df_bw.to_csv (fp, index=False, sep='\t')
    fp.write ('\n')
    
    df = pd.read_csv( csv_file('UDP_LOSS_3M'))
    df_loss = df[['TIMESTAMP', '3g-mean', '3g-max', 'lte-mean', 'lte-max', 'wifi-mean', 'wifi-max']]
    df_loss.columns = ['udp-loss','3g-mean','max', 'lte-mean','max', 'wifi-mean', 'max']
    
    df_loss.to_csv (fp, index=False, sep='\t')
    fp.write ('\n')

def write_gps_map(df):

    fn = csv_file('gps_map') 
    valid_df = df[(df['LATITUDE']>0) & (df['LONGITUDE']>0) ]
    valid_df [['LATITUDE', 'LONGITUDE']].to_csv(fn)
    print '+ '+fn

def plot_gps_map():
	
    df = pd.read_csv (csv_file('gps_map'))
    lats = df['LATITUDE'].tolist()
    lons = df['LONGITUDE'].tolist()
	
    # Korea Map
    eq_map = Basemap(projection='merc', lat_0=37, lon_0=127, resolution = 'h', area_thresh = 0.1, llcrnrlon=124.49, llcrnrlat=32.91, urcrnrlon=131.11, urcrnrlat=39.60)
	
    # World Map
    #eq_map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0, lat_0=0, lon_0=-130)

    eq_map.drawcoastlines()
    eq_map.drawcountries()
    eq_map.fillcontinents(color = 'gray')
    eq_map.drawmapboundary()
    eq_map.drawmeridians(np.arange(0, 360, 30))
    eq_map.drawparallels(np.arange(-90, 90, 30))
	 
    x,y = eq_map(lons, lats)
    eq_map.plot(x, y, 'ro', markersize=3)
    fn = fig_file('gps_map')
    plt.savefig (fn, bbox_inches='tight') 
    plt.gcf().clear()

    print '+ '+fn

def write_throughput_table():

    fn = csv_file ('table')
    if os.path.isfile (fn):
        os.remove (fn)

    fp = open (fn, 'a')
    agg_stats_network_id(fp)
    fp.close()
    print '+ '+fn

def write_wireless_csv():

	df = pd.read_pickle(nia_wireless_pk)

	write_stats_network_id(df)
	write_gps_map(df)

def dump_spark(fi):

    conf = SparkConf().setAppName("test")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    
    print csv_file(fi)
    df = sqlContext.read.format('csv').option('header', 'true').option('mode','DROPMALFORMED').csv(csv_file (fi))
    df.printSchema()
    df.registerTempTable ("speed")
    uuid = sqlContext.sql ("Select * from speed")
    uuid.toPandas().to_pickle(csv_dir+fi+".pickle")

def dump_filtered_df(fi):

    print csv_file(fi)
    
    if (fi=='2016'):
        df = pd.read_csv (csv_file (fi), error_bad_lines = False, low_memory = False)
    else:
        df = pd.read_csv (csv_file (fi), encoding='cp949', error_bad_lines = False)

    _df = df.copy()
    
    print 'original count: %d' % len(df.index)

    _df ['date'] = pd.to_datetime(_df['date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    _df = _df[(_df['down_speed'] > 0) | (df['up_speed'] > 0) | (df['ping_rtt'] > 0) | (df['udp_rtt'] > 0)]
    
    print 'filtered count: %d' % len(_df.index)
    
    if (fi=='2016'):
        _df[cols_2015].to_pickle(csv_out_dir+fi+'.fi.pickle')
    else:
        _df[cols_rest].to_pickle(csv_out_dir+fi+'.fi.pickle')
 
def dump_filtered_pk(fi):

    print pickle_file(fi)
    
    df = pd.read_pickle(pickle_file (fi))
    
    print 'original count: %d' % len(df.index)

    #_df = _df[(_df['down_speed'] > 0) | (df['up_speed'] > 0) | (df['ping_rtt'] > 0) | (df['udp_rtt'] > 0)]
    _df = df[(df['up_speed']>0)&(df['down_speed']>0)&(df['ping_rtt']>=0)&(df['udp_rtt']>=0)&(df['ping_loss']>=0)&(df['udp_loss']>=0)]

    print 'filtered count: %d' % len(_df.index)
    
    if (fi=='2016'):
        _df[cols_2015].to_pickle(csv_dir+fi+'.slim.pk')
    else:
        _df[cols_rest].to_pickle(csv_dir+fi+'.silm.pk')
    

def dump_filtered_cvstopk(fi):

    print csv_file(fi)
    
    #if (fi=='2016'):
    if fi in ['2015','2016','2017','2018']:
        df = pd.read_csv (csv_file (fi), error_bad_lines = False, low_memory = False)
    else:
        df = pd.read_csv (csv_file (fi), encoding='cp949', error_bad_lines = False)

    _df = df.copy()
    
    print 'original count: %d' % len(df.index)
    
    _df ['date'] = pd.to_datetime(_df['date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

    if (fi=='2012'):
        _df = _df[(_df['date'].dt.month != 1)] #2012-01 data corrupted

    if fi in ['2012','2013','2014','2015','2016','2017','2018']:
        _df['down_speed'] = _df['down_speed'].apply(lambda x: x*8)
        _df['up_speed'] = _df['up_speed'].apply(lambda x: x*8)
        print 'convert to bps'
    
    _df = _df[(_df['up_speed']>0)&(_df['down_speed']>0)&(_df['ping_rtt']>=0)&(_df['udp_rtt']>=0)&(_df['ping_loss']>=0)&(_df['udp_loss']>=0)]
   
    print 'filtered count: %d' % len(_df.index)
    
    if fi in ['2015','2016','2017','2018']:
        _df[cols_2015].to_pickle(csv_out_dir+fi+'.slim.pk')
    else:
        _df[cols_rest].to_pickle(csv_out_dir+fi+'.slim.pk')
 
def dump_all_df():
    
    for fi in wired.values():
        print fi
        dump_filtered_cvstopk(fi)
        
        ##dump_filtered_df(fi)
        ##dump_filtered_pk(fi)
        ##dump_spark(fi)

def plot_wireless_csv():
    
    print 'plot_wireless_csv()'
    
    #write_wireless_csv() #write all processed csv from df
	#write_throughput_table()
    #plot_gps_map()
    plot_trend_mobile_users(); plot_trend_network()
   

def plot_wireless_df():
    
    print 'plot_wireless_df()'
    df = pd.read_pickle(nia_wireless_pk)
    
    #plot_week_dist (df, 3, 'DOWNLOAD_BANDWIDTH') #LTE, line, density
    #plot_week_dist (df, 3, 'UDP_LOSS') #LTE, line, density
    #plot_month_dist (df, 3, 'DOWNLOAD_BANDWIDTH') #LTE, line, density
    #plot_month_dist (df, 3, 'UDP_LOSS') #LTE, line, density

	#plot_month_dist_hours (df, 3, 'DOWNLOAD_BANDWIDTH') #LTE, bar, cdf, density
    
    plot_month_dist_hours_selected (df, 3, 'DOWNLOAD_BANDWIDTH') #LTE, bar, cdf, density

    #plot_geo_month_dist (df, 3, 'DOWNLOAD_BANDWIDTH') # fixed this
    #plot_throughput_month_dist (df, 3, 'DOWNLOAD_BANDWIDTH')

    #plot_throughput_dist_table (df, 3, 'DOWNLOAD_BANDWIDTH')
    plot_test (df, 3, 'DOWNLOAD_BANDWIDTH')


def open_fig (fn):

    print '+ '+fn
    os.system ( 'open %s'%(fn) )

def plot_month_test_count():
    
    #df = pd.read_csv (csv_file('wired-month-count')).set_index('date')
    df = pd.read_csv (csv_file('wired-month-count'))

    fn = fig_file ('wired-test-count')
    plt.figure()
    fig, ax = plt.subplots()
    P = df.plot( x='date', y='test-count', style=['ks-'] )
 
    plt.savefig (fn, bbox_inches='tight')
    plt.clf()
    print '+ '+fn

def plot_month_speed():
    
    df = pd.read_csv (csv_file('wired-month-count'))

    df['down-speed-mean'] = df['down-speed-mean'].apply(lambda x: math.floor(x/1024/1024)) 
    df['down-speed-95'] = df['down-speed-95'].apply(lambda x: math.floor(x/1024/1024)) 
    df['down-speed-5'] = df['down-speed-5'].apply(lambda x: math.floor(x/1024/1024)) 
    
    df['up-speed-mean'] = df['up-speed-mean'].apply(lambda x: math.floor(x/1024/1024))
    df['up-speed-95'] = df['up-speed-95'].apply(lambda x: math.floor(x/1024/1024))
    df['up-speed-5'] = df['up-speed-5'].apply(lambda x: math.floor(x/1024/1024))
    
    fn = fig_file ('wired-down-speed')
    plt.figure(); fig, ax = plt.subplots()

    #P = df.plot( x='date', y=['up-speed-95', 'down-speed-95'], ylim=(0,200) )
    P = df.plot( x='date', y=['down-speed-mean', 'down-speed-5', 'down-speed-95'] )
 
    plt.savefig (fn, bbox_inches='tight'); plt.clf(); open_fig(fn)


    fn = fig_file ('wired-up-speed')
    plt.figure(); fig, ax = plt.subplots()

    P = df.plot( x='date', y=['up-speed-mean', 'up-speed-5', 'up-speed-95'] )
 
    plt.savefig (fn, bbox_inches='tight'); plt.clf(); open_fig(fn)

    fn = fig_file ('wired-rtt-loss')
    plt.figure(); fig, ax = plt.subplots()
    
    P = df.plot( x='date', y=['rtt-95', 'loss-95'] )
    
    plt.savefig (fn, bbox_inches='tight'); plt.clf(); open_fig(fn)


def plot_id_month_down(_id): #service, company or isp
    
    type_id = '%s-id'%_id
    df = pd.read_csv (csv_file(('%s-month')%(type_id)))

    df['down-speed-mean'] = df['down-speed-mean'].apply(lambda x: math.floor(x/1024/1024)) 
    df['down-speed-95'] = df['down-speed-95'].apply(lambda x: math.floor(x/1024/1024)) 
    df['down-speed-5'] = df['down-speed-5'].apply(lambda x: math.floor(x/1024/1024)) 
    
    df['up-speed-mean'] = df['up-speed-mean'].apply(lambda x: math.floor(x/1024/1024))
    df['up-speed-95'] = df['up-speed-95'].apply(lambda x: math.floor(x/1024/1024))
    df['up-speed-5'] = df['up-speed-5'].apply(lambda x: math.floor(x/1024/1024))
   
    list_id = df[type_id].unique()
    print len(list_id)
    
    test_count_limit = 50000

    for sid in list_id:
        _df = df[(df[type_id] == sid)]
        
        if sid not in (service_id.keys()):
            continue
        #if _df['test-count'].sum() <= test_count_limit:
        #    continue

        fn = fig_file ('wired-down-speed-%s-%d'%(type_id, sid))
        plt.figure(); fig, axes = plt.subplots(nrows=2, ncols=1)
        
        plt.title (service_id[sid])
        P1 = _df.plot( x='date', y=['down-speed-mean', 'down-speed-5', 'down-speed-95'],  ylim=(0,400), ax=axes[0] )
        #P1 = _df.plot( x='date', y=['up-speed-95', 'down-speed-95'],  ylim=(0,400), ax=axes[0] )
        P2 = _df.plot( x='date', y='test-count', kind='bar', ax=axes[1])
        plt.xticks([])
        
        plt.savefig (fn, bbox_inches='tight'); plt.clf()
        print fn

def plot_id_month_up_down(_id): #service, company or isp
    
    type_id = '%s-id'%_id
    df = pd.read_csv (csv_file(('%s-month')%(type_id)))

    df['down-speed-mean'] = df['down-speed-mean'].apply(lambda x: math.floor(x/1024/1024)) 
    df['down-speed-95'] = df['down-speed-95'].apply(lambda x: math.floor(x/1024/1024)) 
    df['down-speed-5'] = df['down-speed-5'].apply(lambda x: math.floor(x/1024/1024)) 
    
    df['up-speed-mean'] = df['up-speed-mean'].apply(lambda x: math.floor(x/1024/1024))
    df['up-speed-95'] = df['up-speed-95'].apply(lambda x: math.floor(x/1024/1024))
    df['up-speed-5'] = df['up-speed-5'].apply(lambda x: math.floor(x/1024/1024))
   
    list_id = df[type_id].unique()
    print len(list_id)
    
    for sid in list_id:
        _df = df[(df[type_id] == sid)]
        
        if sid not in (service_id.keys()):
            continue

        fn = fig_file ('wired-up-down-speed-%s-%d'%(type_id, sid))
        plt.figure(); fig, axes = plt.subplots(nrows=2, ncols=1)
        
        plt.title (service_id[sid])
        P1 = _df.plot( x='date', y=['up-speed-95', 'down-speed-95'],  ylim=(0,400), ax=axes[0] )
        P2 = _df.plot( x='date', y='test-count', kind='bar', ax=axes[1])
        plt.xticks([])
        
        plt.savefig (fn, bbox_inches='tight'); plt.clf()
        print fn


def test(df):

    df['down_speed'] = df['down_speed'].apply(lambda x: math.floor(x/1024/1024*8)) #round(x,0)
    df['up_speed'] = df['up_speed'].apply(lambda x: math.floor(x/1024/1024*8))
    print df.date.min(), df.date.max(), len(df.index)
    print df['down_speed'].min(), df['down_speed'].median(), df['down_speed'].max()

def csv_isp_id():
    
    print '+ csv_isp_id()'
    _list = []
    for fi in wired.values():
        df = pd.read_pickle(pickle_file(fi))

        group = df[(df['up_speed']>0)&(df['down_speed']>0)&(df['ping_rtt']>=0)&(df['udp_rtt']>=0)&(df['ping_loss']>=0)&(df['udp_loss']>=0)].\
                set_index('date').groupby([pd.TimeGrouper(freq="M"), 'isp_id'], sort=True)

        #print group.size()
        #print group.describe()

        for gr in group:

            #print '%d-%02d %d' % (gr[0][0].year, gr[0][0].month, gr[0][1])
            month = '%d-%02d' % (gr[0][0].year, gr[0][0].month)
            gr_r = gr[1]

            down_speed = gr_r['down_speed']
            up_speed = gr_r['up_speed']
            
            _list.append([month, gr[0][1], len(gr_r.index), \
                    round(down_speed.mean(),2), round(down_speed.quantile(.05),2), round(down_speed.quantile(.95),2), down_speed.median(), down_speed.max(), down_speed.min(), \
                    round(up_speed.mean(),2), round(up_speed.quantile(.05),2), round(up_speed.quantile(.95),2), up_speed.median(), up_speed.max(), up_speed.min(), \
                    round(gr_r['ping_rtt'].quantile(.95),2), round(gr_r['ping_loss'].quantile(.95),2)])
            
            print month, len(gr_r.index), gr[0][1]

    csv_df = pd.DataFrame (_list, columns=['date', 'isp-id', 'test-count', \
            'down-speed-mean', 'down-speed-5', 'down-speed-95', 'down-speed-median', 'down-speed-max', 'down-speed-min', \
            'up-speed-mean', 'up-speed-5', 'up-speed-95', 'up-speed-median', 'up-speed-max', 'up-speed-min', \
            'rtt-95', 'loss-95'])

    csv_df.to_csv(csv_file('isp-id-month'))

def csv_service_id():
    
    print '+ csv_service_id()'
    _list = []
    for fi in wired.values():
        df = pd.read_pickle(pickle_file(fi))

        group = df[(df['up_speed']>0)&(df['down_speed']>0)&(df['ping_rtt']>=0)&(df['udp_rtt']>=0)&(df['ping_loss']>=0)&(df['udp_loss']>=0)].\
                set_index('date').groupby([pd.TimeGrouper(freq="M"), 'service_id'], sort=True)

        for gr in group:

            month = '%d-%02d' % (gr[0][0].year, gr[0][0].month)
            gr_r = gr[1]

            down_speed = gr_r['down_speed']
            up_speed = gr_r['up_speed']
            
            _list.append([month, gr[0][1], len(gr_r.index), \
                    round(down_speed.mean(),2), round(down_speed.quantile(.05),2), round(down_speed.quantile(.95),2), down_speed.median(), down_speed.max(), down_speed.min(), \
                    round(up_speed.mean(),2), round(up_speed.quantile(.05),2), round(up_speed.quantile(.95),2), up_speed.median(), up_speed.max(), up_speed.min(), \
                    round(gr_r['ping_rtt'].quantile(.95),2), round(gr_r['ping_loss'].quantile(.95),2)])
            
            print month, len(gr_r.index), gr[0][1]

    csv_df = pd.DataFrame (_list, columns=['date', 'service-id', 'test-count', \
            'down-speed-mean', 'down-speed-5', 'down-speed-95', 'down-speed-median', 'down-speed-max', 'down-speed-min', \
            'up-speed-mean', 'up-speed-5', 'up-speed-95', 'up-speed-median', 'up-speed-max', 'up-speed-min', \
            'rtt-95', 'loss-95'])

    csv_df.to_csv(csv_file('service-id-month'))

def csv_company_id():
    
    print '+ csv_company_id()'
    _list = []
    for fi in wired.values():
        df = pd.read_pickle(pickle_file(fi))

        group = df[(df['up_speed']>0)&(df['down_speed']>0)&(df['ping_rtt']>=0)&(df['udp_rtt']>=0)&(df['ping_loss']>=0)&(df['udp_loss']>=0)].\
                set_index('date').groupby([pd.TimeGrouper(freq="M"), 'company_id'], sort=True)

        for gr in group:

            month = '%d-%02d' % (gr[0][0].year, gr[0][0].month)
            gr_r = gr[1]

            down_speed = gr_r['down_speed']
            up_speed = gr_r['up_speed']
            
            _list.append([month, gr[0][1], len(gr_r.index), \
                    round(down_speed.mean(),2), round(down_speed.quantile(.05),2), round(down_speed.quantile(.95),2), down_speed.median(), down_speed.max(), down_speed.min(), \
                    round(up_speed.mean(),2), round(up_speed.quantile(.05),2), round(up_speed.quantile(.95),2), up_speed.median(), up_speed.max(), up_speed.min(), \
                    round(gr_r['ping_rtt'].quantile(.95),2), round(gr_r['ping_loss'].quantile(.95),2)])
            
            print month, len(gr_r.index), gr[0][1]

    csv_df = pd.DataFrame (_list, columns=['date', 'company-id', 'test-count', \
            'down-speed-mean', 'down-speed-5', 'down-speed-95', 'down-speed-median', 'down-speed-max', 'down-speed-min', \
            'up-speed-mean', 'up-speed-5', 'up-speed-95', 'up-speed-median', 'up-speed-max', 'up-speed-min', \
            'rtt-95', 'loss-95'])

    csv_df.to_csv(csv_file('company-id-month'))


def csv_month_count():
    
    print '+ csv_month_count()'
    month_test_count = [] 
    for fi in wired.values():
        df = pd.read_pickle(pickle_file(fi))

        group = df[(df['up_speed']>0)&(df['down_speed']>0)&(df['ping_rtt']>=0)&(df['udp_rtt']>=0)&(df['ping_loss']>=0)&(df['udp_loss']>=0)].\
                set_index('date').groupby(pd.TimeGrouper(freq="M"))

        for gr in group:
            month = '%d-%02d' % (gr[0].year, gr[0].month)
            
            gr_r = gr[1]

            down_speed = gr_r['down_speed']
            up_speed = gr_r['up_speed']
            
            month_test_count.append([month, len(gr[1].index), \
                    round(down_speed.mean(),2), round(down_speed.quantile(.05),2), round(down_speed.quantile(.95),2), down_speed.median(), down_speed.max(), down_speed.min(), \
                    round(up_speed.mean(),2), round(up_speed.quantile(.05),2), round(up_speed.quantile(.95),2), up_speed.median(), up_speed.max(), up_speed.min(), \
                    round(gr_r['ping_rtt'].quantile(.95),2), round(gr_r['ping_loss'].quantile(.95),2)])
            
            print month, len(gr_r.index)

    csv_df = pd.DataFrame (month_test_count, columns=['date', 'test-count', \
            'down-speed-mean', 'down-speed-5', 'down-speed-95', 'down-speed-median', 'down-speed-max', 'down-speed-min', \
            'up-speed-mean', 'up-speed-5', 'up-speed-95', 'up-speed-median', 'up-speed-max', 'up-speed-min', \
            'rtt-95', 'loss-95'])

    csv_df.to_csv(csv_file('wired-month-count'))

def dump_wired_csv():

    print 'dump_wired_csv()'
    #csv_month_count()
    #csv_isp_id()
    #csv_service_id()
    #csv_company_id()

def plot_wired_csv():
   
    print 'plot_wired_csv()'
   
    #plot_month_test_count()
    #plot_month_speed()
    
    #plot_id_month_down('isp-id')
    plot_id_month_down('service')
    plot_id_month_down('company')
    plot_id_month_up_down('service')
    plot_id_month_up_down('company')

def plot_wired():

    #csv_month_count()
    
    #csv_isp_id()
    #plot_id_month_down('isp')

    #csv_company_id()
    #plot_id_month_down('company')
    
    #csv_month_count()
    plot_month_speed()


csv_dir = '../csv/'
#csv_dir = '/Users/young/Desktop/csv/'

csv_out_dir = '../csv/'

fig_dir = '../csv/'
#fig_dir = '../script/fig/'
#fig_dir = '../nia_paper/fig/new/'

nia_wireless_pk = '../csv/nia-wireless-filtered.pickle'

network = {0:'2g', 1:'3g', 2:'wifi', 3:'lte'}
schema = {'down_speed':'wired-d-throughput', 'up_speed':'wired-u-throughput', 'ping_rtt':'wired-ping-rtt'}

#wired = {1:'2001', 2:'2002', 3:'2003', 4:'2004', 5:'2005', 6:'2006', 7:'2007', 8:'2008', 9:'2009', 10:'2010', 11:'2011', 12:'2012', 13:'2013', 14:'2014', 16:'2016' } 
#wired = {12:'2012', 13:'2013', 14:'2014', 16:'2016' } 
#wired = {15:'2015', 16:'2016', 17:'2017', 18:'2018'} 
wired = {1:'2001', 2:'2002', 3:'2003', 4:'2004', 5:'2005', 6:'2006', 7:'2007', 8:'2008', 
        9:'2009', 10:'2010', 11:'2011', 12:'2012', 13:'2013', 14:'2014', 15:'2015', 16:'2016', 17:'2017', 18:'2018'} 

cols_rest = ['no','date','user_id','isp_id','company_id','service_id','sido_id','ip','down_speed','up_speed','ping_rtt','ping_jitter','ping_loss','udp_rtt','udp_jitter','udp_loss','ipaddr']
cols_2015 = ['no','date','user_id','isp_id','company_id','service_id','sido_id','ip','down_speed','up_speed','ping_rtt','ping_jitter','ping_loss','udp_rtt','udp_jitter','udp_loss','ipaddr','ifname','service_type']

service_id = {1:'KT',2:'SKB',3:'LGU+',4:'Delive',5:'CJ',6:'T-Broad',7:'HCN',8:'ETC',9:'CMB'} #service, company

matplotlib.style.use('ggplot')

#dump_all_df()
plot_wired()

#dump_wired_csv()
#plot_wired_csv()



#plot_wireless_csv()
#plot_wireless_df()
