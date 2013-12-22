import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
import datetime

from pandas import Series, DataFrame

import statsmodels.api as sm 


def regress(data, yvar, xvars):
	Y = data[yvar]
	X = data[xvars] 
	X['intercept'] = 1.
	result = sm.OLS(Y, X).fit() 
	return result.params
	
# Stock Example
close_px = pd.read_csv('pydata-book/ch09/stock_px.csv', parse_dates=True, index_col=0)
# get return percentags
rets = close_px.pct_change().dropna()
spx_corr = lambda x: x.corrwith(x['SPX'])
# Group by year of index
by_year = rets.groupby(lambda x: x.year)
by_year.apply(spx_corr)
