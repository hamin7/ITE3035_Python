import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/hamin/Documents/bithumb_analysis/2018-05-btc-krw.csv")

df.dtypes
# identifying column type

## converting timestamp column type 'object' to 'datetime'
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='raise')
df.dtypes

df.head()

# creating 'price - quantity' connection
group_quantity_price = df['quantity'].groupby(df['price'])

# price 별 거래량
group_quantity_price.size()

# price 별 quantity의 평균
group_quantity_price.mean()
