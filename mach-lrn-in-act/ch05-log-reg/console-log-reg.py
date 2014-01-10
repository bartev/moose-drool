run logRegres.py

dataArr, labelMat = loadDataSet()

gradAscent(dataArr, labelMat)

# output
# matrix([[ 4.12414349],
#         [ 0.48007329],
#         [-0.6168482 ]])


# matrix.getA() returns self as an ndarray
weights = gradAscent(dataArr, labelMat)
plotBestFit(weights)


# Stochastic gradient gradAscent
dataArr, labelMat = loadDataSet()
weights = stochGradAscent0(np.array(dataArr), labelMat)
plotBestFit(weights)


dataArr, labelMat = loadDataSet()
weights = stochGradAscent1(np.array(dataArr), labelMat)
plotBestFit(weights)