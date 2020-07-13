import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

df = pd.read_csv("/Users/hamin/Documents/bithumb_analysis/include/2018-05-btc-krw.csv")

# identifying column type 
df.dtypes

# creating 'price - quantity' connection - price가 같은것 끼리 묶는다.
quantity_price = df['quantity'].groupby(df['price'])

# price 별 quantity의 평균
quantity_price.mean()

# price-quantity 그래프 인데 왜 이런지 모르겠다,,,,
quantity_price.plot()

# 시간 별 모든 요소 그래프 (amount가 변동폭이 커서 나머지는 잘 안보인다)
df.plot()

# price-quantity 간 그래프
df.plot(x='price', y='quantity')

# price-amount 간 그래프 ()
df.plot(x='price', y='amount')

df.plot(x='price', y='side')
