# Integrated OFI

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload() 

df = pd.read_csv("first_25000_rows.csv")
df.head()

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

ofi_matrix = df[ofi_levels].fillna(0).values  # Shape: (rows, 8)

scaler = StandardScaler()
ofi_scaled = scaler.fit_transform(ofi_matrix)

pca = PCA(n_components=1)
integrated_ofi = pca.fit_transform(ofi_scaled)

df['integrated_ofi'] = integrated_ofi

df[['ts_event', 'symbol', 'integrated_ofi']].head(10)
