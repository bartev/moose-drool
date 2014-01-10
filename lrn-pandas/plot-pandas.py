import numpy as np
import matplotlib.pyplot as plt
import pylab
import pandas as pd
from pandas import DataFrame, Series


df = DataFrame(np.random.randn(10, 4).cumsum(0),
	columns=['A', 'B', 'C', 'D'],
	index=np.arange(0, 100, 10))

df.plot(subplots=True, sharey=True, title='random data', kind='kde')
df.plot(subplots=True, sharey=True, title='random data', kind='barh')
df.plot(subplots=True, sharey=True, title='random data', kind='bar')
df.plot(subplots=True, sharey=True, title='random data', kind='line')


# 2 plots - vertical bar plot over horizontal bar plot
data = Series(np.random.rand(16), index=list('abcdefghijklmnop'))

fig, axes = plt.subplots(2, 1)
data.plot(kind='bar', ax=axes[0], color='b', alpha=0.3)
data.plot(kind='barh', ax=axes[1], color='r', alpha=0.3)


# Plot from tips data
tips = pd.read_csv('../../pydata-book/ch08/tips.csv')
# Crosstab
party_counts = pd.crosstab(tips.day, tips.size)
# get percentages
party_pcts = party_counts.div(party_counts.sum(1).astype(float), axis=0)

# plot percentages
party_pcts.plot(kind='bar', stacked=True, alpha=0.3)

tips['tip_pct'] = tips['tip'] / tips['total_bill']

# Plot histogram of tip_pct
tips['tip_pct'].hist(bins=50, alpha=0.3, color='r')

# plot density plot (KDE = kernel density estimation)
tips['tip_pct'].plot(kind='kde')



# Bimodal example
fig = plt.figure()
comp1 = np.random.normal(0, 1, size=200)  # N(0, 1)
comp2 = np.random.normal(10, 2, size=200)  # N(10, 4)
values = Series(np.concatenate([comp1, comp2]))

values.hist(bins=100, alpha=0.3, color='g', normed=True)
values.plot(kind='kde', style='r-')
draw()

# Scatterplot
plt.figure()
macro = pd.read_csv('../../pydata-book/ch08/macrodata.csv')
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna()

plt.scatter(trans_data['m1'], trans_data['unemp'])
plt.title('Changes in log %s vs log %s' % ('m1', 'unemp'))

# scatter matrix
pd.scatter_matrix(trans_data, diagonal='kde', color='b', alpha=0.3)

