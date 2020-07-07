# Seaborn
Seaborn gives figures made by matplotlib a more modern/professional look.

Here are a few examples of plots made with seaborn.<br>
The script [`yahoo_finance.py`](./yahoo_finance.py) was used to make the following plot

![](./figs/finance_seaborn.png)

Seaborn also offers features that matplotlib lacks, such as `sns.distplot()`.  This code snippet can be found in [`seaborn_example.py`.](./seaborn_example.py)
```py
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
idex_vol = data.DataReader("IDEX", data_source='yahoo')['Volume']
sns.distplot(idex_vol)
```
![](./figs/seaborn_example.png)
