from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# get one column of data
#idex_vol = data.DataReader("AAPL", data_source='yahoo')['Volume']

# get full data data
idex_data = data.DataReader("IDEX", data_source='yahoo')

# break data up by column
idex_vol = idex_data['Volume']
idex_close = idex_data['Close']
#idex_adjclose = idex_data['Adj Close']

# normalize data
idex_vol = idex_vol / max(idex_vol)
idex_close = idex_close / max(idex_close)

# Smooth Data using EMA
idex_close_smooth20 = idex_close.rolling(window=20).mean()
idex_vol_smooth20 = idex_vol.rolling(window=20).mean()

# smoothing parameter is variable...try:
#long_rolling_idex = idex_close.rolling(window=100).mean()

# shift data
#idex_vol_smooth20 = idex_vol_smooth20.shift(-50)

####################
# Plot Data
####################
fig, ax = plt.subplots(figsize=(16,9))

# plot close value data
ax.plot(idex_close, color='b', label='IDEX: close raw', alpha=0.2)
ax.plot(idex_close_smooth20, label='IDEX: close EMA 20')

# plot volume data
ax.plot(idex_vol.index, idex_vol, color='r', label='IDEX: volume raw', alpha=0.2)
ax.plot(idex_vol_smooth20, label='IDEX: volume EMA 20')

# add labels
ax.set_xlabel('Date')
ax.set_ylabel('Values Normalized to Unity')
ax.set_title('IDEX')
# add legend
ax.legend()

plt.savefig('figs/finance_seaborn.png')