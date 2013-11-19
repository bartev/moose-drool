import seaborn as sns
import numpy as np
from numpy import mean
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import pandas as pd
from scipy import stats
import pylab

sns.set(palette='Purples_r')
sns.set(palette='Reds_r')
mpl.rc('figure', figsize=(5, 5))
np.random.seed(9221999)

x = randn(50)
y = x + randn(50)
sns.regplot(x, y)

df = pd.DataFrame(np.transpose([x, y]), columns=["X", "Y"])
sns.regplot("X", 'Y', df)

sns.regplot("X", 'Y', df, ci=None, color='slategray')

r2 = lambda x, y: stats.pearson(x, y)[0] ** 2
sns.regplot('X', 'Y', df, corr_func=r2, func_name='$R^2$', color='seagreen')


tips = pd.read_csv("https://raw.github.com/mwaskom/seaborn/master/examples/tips.csv")
tips["big_tip"] = tips.tip > (.2 * tips.total_bill)
tips["smoker"] = tips["smoker"] == "Yes"
tips["female"] = tips["sex"] == "Female"
mpl.rc("figure", figsize=(7, 7))
sns.corrplot(tips)
sns.corrplot(tips, sig_stars=False)
sns.corrplot(tips, sig_tail='upper', cmap='PuRd', cmap_range=(-.2, .8))

mpl.rc('figure', figsize=(5, 5))
sns.lmplot('total_bill', 'tip', tips)
sns.lmplot('total_bill', 'tip', tips, color='time')
sns.lmplot('total_bill', 'tip', tips, color='day', palette='muted', ci=None)

tips['tip_sqr'] = tips.tip ** 2
sns.lmplot('total_bill', 'tip_sqr', tips, order=2)

sns.lmplot('size', 'big_tip', tips)
sns.lmplot('size', 'big_tip', tips, x_jitter=0.3, y_jitter=0.075)
sns.lmplot('size', 'big_tip', tips, x_jitter=0.3, y_jitter=0.075, logistic=True, n_boot=1000)
sns.lmplot('total_bill', 'tip', tips, col='sex')
sns.lmplot('total_bill', 'tip', tips, col='sex', color='sex')
sns.lmplot('total_bill', 'tip', tips, col='sex', color='sex', sharey=False)


sns.lmplot('size', 'tip', tips)
sns.lmplot('size', 'tip', tips, x_jitter=0.15)
sns.lmplot('size', 'tip', tips, x_estimator=mean)

sns.lmplot('total_bill', 'tip', tips, row='sex', color='sex', col='day', size=4)
sns.lmplot('total_bill', 'tip', tips, color='sex', col='day', size=4)

sns.lmplot('total_bill', 'tip', tips, ci=None, color='day', col='day', col_wrap=4, size=4)

df = pd.DataFrame(dict(a=randn(50)))
df['b'] = df.a + randn(50) / 2
df['c'] = df.a + randn(50) / 2 + 3

sns.lmplot('b', 'c', df)
sns.lmplot('b', 'c', df, x_partial='a')

mpl.rc('figure', figsize=(8, 5))
sns.coefplot('tip ~ day + time * size', tips)
sns.coefplot('total_bill ~ day + time + smoker', tips, ci=68, palette='muted')
sns.coefplot('tip ~ time * sex', tips, 'size', intercept=True)