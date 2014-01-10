datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')

normMat, ranges, minVals = autoNorm(datingDataMat)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
# plt.show()


# fig = plt.figure()
# ax = fig.add_subplot(111)
# x = datingDataMat[:, 1]
# y = datingDataMat[:, 2]
# ax.scatter(x, y, 15.0 * array(datingLabels), 15.0 * array(datingLabels))
# plt.show()



# x = randn(10)
# y = randn(10)
# rep([1, 2], 5)
# [1, 2]
# [1, 2] * 3
# cols = [1, 2] * 5
# sizes = cols
# type(cols)
# fig = plt.figure()
# fig.add_subplot(111)
# ax = fig.add_subplot(111)
# ax.scatter(x, y)
# draw()
# ax.scatter(x, y, cols, sizes)




# """
# Simple demo of a scatter plot.
# """
# import numpy as np
# import matplotlib.pyplot as plt


# N = 10
# x = np.random.rand(N)
# y = np.random.rand(N)
# area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

# plt.scatter(x, y, s=area, alpha=0.5)
# plt.show()



















