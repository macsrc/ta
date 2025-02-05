import sys

import pandas as pd

sys.path.append("..") # Adds higher directory to python modules path.

# Load data
df = pd.read_csv('../data/datas.csv', sep=',')
# df = pd.read_csv('prueba.csv', sep=',')

# Clean nan values
df = utils.dropna(df)

print(df.columns)

# Add adx indicator filling Nans values
df['adx'] = adx(df['High'], df['Low'], df['Close'], n=14, fillna=True)

print(df['adx'])

df['adx_neg'] = adx_neg(df['High'], df['Low'], df['Close'], n=14, fillna=True)
df['adx_pos'] = adx_pos(df['High'], df['Low'], df['Close'], n=14, fillna=True)

print(df.columns)
print(df.tail())
