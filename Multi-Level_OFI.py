# Multi Level OFI

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload() 

df = pd.read_csv("first_25000_rows.csv")
df.head()

ofi_levels = []

for level in range(2, 10): 
    bp_col = f'bid_px_0{level}'
    ap_col = f'ask_px_0{level}'
    bs_col = f'bid_sz_0{level}'
    as_col = f'ask_sz_0{level}'

    df[f'prev_{bp_col}'] = df[bp_col].shift(1)
    df[f'prev_{ap_col}'] = df[ap_col].shift(1)
    df[f'prev_{bs_col}'] = df[bs_col].shift(1)
    df[f'prev_{as_col}'] = df[as_col].shift(1)

    def delta_bid(row):
        if row[bp_col] > row[f'prev_{bp_col}']:
            return row[bs_col]
        elif row[bp_col] == row[f'prev_{bp_col}']:
            return row[bs_col] - row[f'prev_{bs_col}']
        else:
            return -row[f'prev_{bs_col}']

    def delta_ask(row):
        if row[ap_col] < row[f'prev_{ap_col}']:
            return row[as_col]
        elif row[ap_col] == row[f'prev_{ap_col}']:
            return row[as_col] - row[f'prev_{as_col}']
        else:
            return -row[f'prev_{as_col}']

    bid_delta = df.apply(delta_bid, axis=1)
    ask_delta = df.apply(delta_ask, axis=1)

    ofi = bid_delta - ask_delta
    ofi_col = f'ofi_level_{level}'
    df[ofi_col] = ofi
    ofi_levels.append(ofi_col)
ofi_levels

[col for col in df.columns if 'bid' in col or 'ask' in col]
