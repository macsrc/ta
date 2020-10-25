import datetime
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr

stocks = ["^IXIC"] # If you want to grab multiple stocks add more labels to this list# Set start and end dates
start = datetime.datetime(2018, 11, 1)
end   = datetime.datetime(2019, 1, 1)# Grab data
data = pdr.get_data_yahoo(stocks, start = start, end = end)

rsi_period = 14
chg = data['Close'].diff(1)
gain = chg.mask(chg<0,0)
data['gain'] = gain
loss = chg.mask(chg>0,0)
data['loss'] = loss
avg_gain = gain.ewm(com = rsi_period - 1, min_periods = rsi_period).mean()
avg_loss = loss.ewm(com = rsi_period - 1, min_periods = rsi_period).mean()
data['avg_gain'] = avg_gain
data['avg_loss'] = avg_loss
rs = abs(avg_gain/avg_loss)
rsi = 100-(100/(1+rs))
print(rsi)