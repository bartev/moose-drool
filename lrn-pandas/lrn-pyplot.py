import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn


fig = plt.figure()

# Axes subplot objects
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

plt.plot([1.5, 3.5, -2, 1.6])


plt.plot(rand(50).cumsum(), 'k--')
_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))


# Simple plot
x = range(0, 100)
y = [i * i for i in x]

plt(x, y, '-')
plt.plot(x, y, '-')
plt.title('Plotting x * x')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('simple.png')

 # Plotting dates/times
from matplotlib.dates import date2num
from datetime import datetime, timedelta
 
 # Generate a series of timestamps from today to today + 100 years
 x = [date2num(datetime.today() + timedelta(days=365 * x)) for x in range(0, 100)]
 y = [i * i for i in range(0, 100)]
 
plt(x, y, '-')
plt.plot_date(x, y, '-')
plt.title('Plotting x * x')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('SimpleDates.png')
plt.show()



# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

def f(t):
	return np.exp(-t) * np.cos(2 * np.pi * t)

t1 = np.arange(0., 5., 0.1)
t2 = np.arange(0., 5., 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(212)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')



