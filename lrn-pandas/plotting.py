import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

# make simple line plot
plt.plot(np.arange(10))
plt.show()

# Close the plot
# plt.close()


fig = plt.figure()
plt.gcf()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

plt.plot(randn(50).cumsum(), 'k--')

_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))

fig, axes = plt.subplots(2, 2)
subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)

for i in range(2):
	for j in range(2):
		axes[i, j].hist(randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)