
from numpy.random import randn
import numpy as np
import matplotlib.pyplot as plt


x = randn(10)
y = randn(10)
cols = [1, 2] * 5
cols = 15 * np.array(cols)
sizes = cols

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y, c = cols, s = sizes)

plt.show()



# Posted on stackoverflow
import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

plt.scatter(x, y, s=area, alpha=0.5)
plt.show()
