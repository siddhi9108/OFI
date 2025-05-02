import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload() 

df = pd.read_csv("first_25000_rows.csv")
df.head()


# Best-Level OFI
df = df.rename(columns={
    'bid_px_01': 'bid_price',
    'ask_px_01': 'ask_price',
    'bid_sz_01': 'bid_size',
    'ask_sz_01': 'ask_size'
})

df['prev_bid_price'] = df['bid_price'].shift(1)
df['prev_ask_price'] = df['ask_price'].shift(1)
df['prev_bid_size'] = df['bid_size'].shift(1)
df['prev_ask_size'] = df['ask_size'].shift(1)

def delta_bid(row):
    if row['bid_price'] > row['prev_bid_price']:
        return row['bid_size']  
    elif row['bid_price'] == row['prev_bid_price']:
        return row['bid_size'] - row['prev_bid_size'] 
    else:
        return -row['prev_bid_size'] 

def delta_ask(row):
    if row['ask_price'] < row['prev_ask_price']:
        return row['ask_size']  
    elif row['ask_price'] == row['prev_ask_price']:
        return row['ask_size'] - row['prev_ask_size'] 
    else:
        return -row['prev_ask_size'] 

df['delta_bid'] = df.apply(delta_bid, axis=1)
df['delta_ask'] = df.apply(delta_ask, axis=1)

df['best_level_ofi'] = df['delta_bid'] - df['delta_ask']

df[['ts_event', 'symbol', 'bid_price', 'ask_price', 'bid_size', 'ask_size', 'best_level_ofi']].head(10)
