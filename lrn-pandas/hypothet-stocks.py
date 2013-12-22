import random; random.seed(0) 
import string
N = 1000
def rands(n):
	choices = string.ascii_uppercase
	return ''.join([random.choice(choices) for _ in xrange(n)]) 
tickers = np.array([rands(5) for _ in xrange(N)])

# I then create a DataFrame containing 3 columns representing hypothetical, but random portfolios for a subset of tickers:
M = 500
df = DataFrame({'Momentum' : np.random.randn(M) / 200 + 0.03,
	'Value' : np.random.randn(M) / 200 + 0.08, 
	'ShortInterest' : np.random.randn(M) / 200 - 0.02}, 
	index=tickers[:M])
	
# Next, let’s create a random industry classification for the tickers. To keep things simple, I’ll just keep it to 2 industries, storing the mapping in a Series:
ind_names = np.array(['FINANCIAL', 'TECH'])
sampler = np.random.randint(0, len(ind_names), N) 
industries = Series(ind_names[sampler], index=tickers,
	name='industry')

by_industry = df.groupby(industries)
by_industry.mean()
by_industry.describe()
def zscore(group):
	return (group - group.mean()) / group.std()
	
df_stand = by_industry.apply(zscore)
df_stand.groupby(industries).agg(['mean', 'std'])

# Within-industry rank descending
ind_rank = by_industry.rank(ascending=False)
ind_rank.groupby(industries).agg(['min', 'max'])

# Industry rank and standardize
by_industry.apply(lambda x: zscore(x.rank()))

#-------
# Group Factor Exposures
from numpy.random import rand
fac1, fac2, fac3 = np.random.rand(3, 1000)
ticker_subset = tickers.take(np.random.permutation(N)[:1000])
# Weighted sum of factors plus noise
port = Series(0.7 * fac1 - 1.2 * fac2 + 0.3 * fac3 + rand(1000),
	index=ticker_subset)
factors = DataFrame({'f1': fac1, 'f2': fac2, 'f3': fac3},
	index=ticker_subset)


# Do ordinary least squares to get factor weights on port
pd.ols(y=port, x=factors).beta


def beta_exposure(chunk, factors=None): 
	return pd.ols(y=chunk, x=factors).beta
	
by_ind = port.groupby(industries)
exposures = by_ind.apply(beta_exposure, factors=factors)
exposures.unstack()

#-------
# Decile and Quartile Analysis
import pandas.io.data as web
data = web.get_data_yahoo('SPY', '2006-01-01')
px = data['Adj Close'] 
returns = px.pct_change()

def to_index(rets):
	index = (1 + rets).cumprod()
	first_loc = max(index.notnull().argmax() - 1, 0) 
	index.values[first_loc] = 1
	return index

def trend_signal(rets, lookback, lag):
	signal = pd.rolling_sum(rets, lookback, min_periods=lookback - 5) 
	return signal.shift(lag)

#-------
# Signal Frontier Analysis
import pandas.io.data as web

names = ['AAPL', 'GOOG', 'MSFT', 'DELL', 'GS', 'MS', 'BAC', 'C'] 
def get_px(stock, start, end):
	return web.get_data_yahoo(stock, start, end)['Adj Close']

px = DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

def calc_mom(price, lookback, lag):
	mom_ret = price.shift(lag).pct_change(lookback) 
	ranks = mom_ret.rank(axis=1, ascending=False) 
	demeaned = ranks - ranks.mean(axis=1)
	return demeaned / demeaned.std(axis=1)


compound = lambda x : (1 + x).prod() - 1 
daily_sr = lambda x: x.mean() / x.std()

def strat_sr(prices, lb, hold):
	# Compute portfolio weights
	freq = '%dB' % hold
	port = calc_mom(prices, lb, lag=1)
	daily_rets = prices.pct_change()
	# Compute portfolio returns
	port = port.shift(1).resample(freq, how='first') 
	returns = daily_rets.resample(freq, how=compound) 
	port_rets = (port * returns).sum(axis=1)
	return daily_sr(port_rets) * np.sqrt(252 / hold)
	

strat_sr(px, 70, 30)
from collections import defaultdict

lookbacks = range(20, 90, 5)
holdings = range(20, 90, 5)

dd = defaultdict(dict)

for lb in lookbacks:
    for hold in holdings:
        dd[lb][hold] = strat_sr(px, lb, hold)

ddf = DataFrame(dd)
ddf.index.name = 'Holding Period'
ddf.columns.name = 'Lookback Period'

import matplotlib.pyplot as plt
def heatmap(df, cmap=plt.cm.gray_r):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    axim = ax.imshow(df.values, cmap=cmap, interpolation='nearest')
    ax.set_xlabel(df.columns.name)
    ax.set_xticks(np.arange(len(df.columns)))
    ax.set_xticklabels(list(df.columns))
    ax.set_yticks(np.arange(len(df.index)))
    ax.set_yticklabels(list(df.index))
    plt.colorbar(axim)

heatmap(ddf)

