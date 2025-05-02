# Cross-Asset OFI

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload() 

df = pd.read_csv("first_25000_rows.csv")
df.head()

df['ts_event'] = pd.to_datetime(df['ts_event'])

df['mid_price'] = (df['bid_price'] + df['ask_price']) / 2
df.set_index('ts_event', inplace=True)

symbol_ofi = []
symbol_returns = []

for symbol, group in df.groupby('symbol'):
    resampled = group.resample('1min').agg({
        'mid_price': 'last',
        'integrated_ofi': 'sum'
    }).dropna()

    resampled['log_ret'] = np.log(resampled['mid_price']).diff().shift(-1)

    resampled['symbol'] = symbol
    symbol_ofi.append(resampled[['integrated_ofi', 'symbol']])
    symbol_returns.append(resampled[['log_ret', 'symbol']])

ofi_df = pd.concat(symbol_ofi).reset_index()
ret_df = pd.concat(symbol_returns).reset_index()

ofi_wide = ofi_df.pivot(index='ts_event', columns='symbol', values='integrated_ofi').add_prefix('ofi_')

ret_aapl = ret_df[ret_df['symbol'] == 'AAPL'][['ts_event', 'log_ret']]
Xy = pd.merge(ofi_wide, ret_aapl, on='ts_event', how='inner').dropna()

X = Xy.drop(columns=['ts_event', 'log_ret'])
y = Xy['log_ret']


from sklearn.linear_model import LassoCV

lasso = LassoCV(cv=5).fit(X, y)

coef_df = pd.Series(lasso.coef_, index=X.columns)
print(coef_df[coef_df != 0].sort_values(ascending=False)) 
