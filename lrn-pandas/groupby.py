import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
import datetime

from pandas import Series, DataFrame

df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
	'key2' : ['one', 'two', 'one', 'two', 'one'],
	'data1' : np.random.randn(5), 
	'data2' : np.random.randn(5)})

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
df['data1'].groupby([states, years]).mean()

for name, group in df.groupby('key1'): 
	print name
	print group

# compute a dict of the data pieces
pieces = dict(list(df.groupby('key1')))

grouped = df.groupby(df.dtypes, axis=1)
dict(list(grouped))

people = DataFrame(np.random.randn(5, 5), columns=['a', 'b', 'c', 'd', 'e'], index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.ix[2:3, ['b', 'c']] = np.nan # Add a few NA values

mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f' : 'orange'}


# apply function to groups
def peak_to_peak(arr):
	return arr.max() - arr.min()


# Load tips data
tips = pd.read_csv('pydata-book/ch08/tips.csv')
# Add tip percentage of total bill
tips['tip_pct'] = tips['tip'] / tips['total_bill']

grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'], 'size' : 'sum'})

def top(df, n=5, column='tip_pct'): 
	return df.sort_index(by=column)[-n:]


# Apply a custom function to quantiles of a df
frame = DataFrame({'data1': np.random.randn(1000), 'data2': np.random.randn(1000)})
def get_stats(group):
	return {'min': group.min(), 'max': group.max(), 'count': group.count(), 'mean': group.mean()}
grouping = pd.qcut(frame.data1, 10, labels=False)
grouped = frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()


# Example: Group Weighted Average and Correlation
df = DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'], 'data': np.random.randn(8),'weights': np.random.rand(8)})
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
grouped.apply(get_wavg)


# Stock Example
close_px = pd.read_csv('pydata-book/ch09/stock_px.csv', parse_dates=True, index_col=0)
# get return percentags
rets = close_px.pct_change().dropna()
spx_corr = lambda x: x.corrwith(x['SPX'])
# Group by year of index
by_year = rets.groupby(lambda x: x.year)
by_year.apply(spx_corr)


# Pivot table
# Implemented using groupby and reshape
# These 2 are equivalent ways of getting group means.
tips.pivot_table(rows=['sex', 'smoker'])
tips.groupby(['sex', 'smoker']).mean()

tips.pivot_table(['tip_pct', 'size'], rows=['sex', 'day'], cols='smoker')
tips.groupby(['sex', 'day', 'smoker'])['tip_pct', 'size'].mean().unstack('smoker')
