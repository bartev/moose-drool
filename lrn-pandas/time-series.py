import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
import datetime

from pandas import Series, DataFrame
from datetime import datetime
from datetime import timedelta

now = datetime.now()
now.year, now.month, now.day
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
delta
delta.days
delta.seconds


stamp = datetime(2011, 1, 3)
str(stamp)
stamp.strftime('%Y-%m-%d')
value = '2011-01-03'
datetime.strptime(value, '%Y-%m-%d')

datestrs = ['7/6/2011', '8/6/2011']
[datetime.strptime(x, '%m/%d/%Y') for x in datestrs]

#-------
# Time series Basics
# Series indexed by timestamps
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7), datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = Series(np.random.randn(6), index=dates)

type(ts.index)
ts.index
ts + ts[::2]
ts.index.dtype
stamp = ts.index[0]

#-------
# Indexing, Selection, Subsetting
# Create a longer series with a date_range
longer_ts = Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts.truncate(after='1/9/11')
dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')

long_df = DataFrame(np.random.randn(100, 4), index=dates, columns=['Colorado', 'Texas', 'New York', 'Ohio'])
# Select rows with index in 5/2011
long_df.ix['5-2001']

#-------
# Time series with duplicate indices
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
dup_ts = Series(np.arange(5), index=dates)
dup_ts.index.is_unique
grouped = dup_ts.groupby(level=0)
grouped.mean()
grouped.count()

#-------
# Generating Date Ranges
index = pd.date_range('4/1/2012', '6/1/2012')
pd.date_range(start='4/1/2012', periods=20)
pd.date_range(end='4/1/2012', periods=20)

# Generate index containing last business day of each month
# 'BM' freq
pd.date_range('1/1/2000', '12/1/2000', freq='BM')

pd.date_range('5/2/2012 12:56:31', periods=5, normalize=True)


#-------
# Frequencies and Date Offsets
from pandas.tseries.offsets import Hour, Minute
hour = Hour()
# Create range of times, every 4 hours ('4H')
pd.date_range('1/1/2000', '1/3/2000 23:59', freq='4h')
Hour(2) + Minute(30)
pd.date_range('1/1/2000', periods=10, freq='1h30min')
rng = pd.date_range('1/1/2012', '9/1/2012', freq='WOM-3FRI')

# 'BM' 	last business/weekday of month
# 'M' 	calendar month end
# 'H'	hour
# 'WOM'	week of month

#-------
# Shifting (Leading and lagging) DataFrame
ts = Series(np.random.randn(4), index=pd.date_range('1/1/2000', periods=4, freq='M'))
# Get pct change
ts/ts.shift(1) - 1
# Advance timestamp instead of data
ts.shift(3, freq='D')
ts.shift(1)
ts.shift(1, freq='D')

#-------
# Shifting dates with offsets
from pandas.tseries.offsets import Day, MonthEnd
now
now  + 3 * Day()
# Anchored to month end
now + MonthEnd()		# goes to month end
now + MonthEnd(2)		# goes to now + 2 month ends
offset = MonthEnd()
offset.rollforward(now)
offset.rollback(now)

# Get mean, grouped by an offset (in this case, month end)
ts = Series(np.random.randn(20), index=pd.date_range('1/15/2000', periods=20, freq='4d'))
ts.groupby(offset.rollforward).mean()


#--------
# Periods and Period Arithmetic
p = pd.Period(2007, freq='A-DEC')


#--------
# Resampling and Frequency Conversion
rng = pd.date_range('1/1/2000', periods=100, freq='D')
ts = Series(randn(len(rng)), index=rng)

#--------
# Downsampling
rng = pd.date_range('1/1/2000', periods=12, freq='T')
ts = Series(np.arange(12), index=rng)
ts.resample('5min', how='sum')
ts.resample('5min', how='sum', closed='left')
ts.resample('5min', how='sum', closed='right')

ts.resample('5min', how='sum', label='left')
ts.resample('5min', how='sum', loffset='-1s')
ts.resample('5min', how='sum', loffset='-1s', closed='left')
ts.resample('5min', how='sum', loffset='-1s', closed='right')

ts.resample('5min', how='sum', loffset='1s')
ts.resample('5min', how='sum', loffset='1s', label='right')
ts.resample('5min', how='sum', loffset='-1s', label='right')
ts.resample('5min', how='ohlc', loffset='-1s', label='right')

#--------
# Resampling with groupby
rng = pd.date_range('1/1/2000', periods=100, freq='D')
ts = Series(np.arange(100), index=rng)
ts.groupby(lambda x: x.month).mean()
ts.groupby(lambda x: x.weekday).mean()


#--------
# Time Series Plotting
close_px_all = pd.read_csv('pyda ch09/stock_px.csv', parse_dates=True, index_col=0)

close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px.resample('B', fill_method='ffill')
close_px['AAPL'].plot()
close_px['AAPL'].ix['01-2011':'03-2011'].plot()
appl_q = close_px['AAPL'].resample('Q-DEC', fill_method='ffill')
appl_q.ix['2009':].plot()

# Moving window functions (Rolling mean, e.g.)


















