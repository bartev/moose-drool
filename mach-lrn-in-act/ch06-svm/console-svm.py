dataMat, labelMat = loadDataSet('testSet.txt')
labelMat = np.mat(labelMat).transpose()
dataMatrix = np.mat(dataMat)


dataArr, labelArr = loadDataSet('testSet.txt')
b,alphas = smoSimple(dataArr, labelArr, 0.6, 0.001, 40)

# to do full Platt

dataArr,labelArr = loadDataSet('testSet.txt')
b, alphas = smoP(dataArr, labelArr, 0.6, 0.001, 40)