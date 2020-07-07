from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
idex_vol = data.DataReader("IDEX", data_source='yahoo')['Volume']
sns.distplot(idex_vol)

plt.savefig('figs/seaborn_example.png')