import numpy as np

# convenience loader function
def loadDataSet():
	dataMat = []
	labelMat = []
	fr = open('testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()
		# load data set in for form (x1, x2, class) for each line
		# set x0 = 1.0
		dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat, labelMat

def sigmoid(inX):
	return 1.0 / (1 + np.exp(-inX))

def gradAscent(dataMatIn, classLabels):
	# convert to numpy matrix data type
	# 100 x 3 (m x n)
	dataMatrix = np.mat(dataMatIn)
	# 100 x 1 (m x 1)
	labelMat = np.mat(classLabels).transpose()
	m, n = dataMatrix.shape
	alpha = 0.001
	maxCycles = 500
	# 3 x 1 (n x 1)
	weights = np.ones((n, 1))
	for k in range(maxCycles):
		# matrix multiplication
		# 100 x 1 (m x 1)
		h = sigmoid(dataMatrix * weights)
		# 100 x 1 (m x 1)
		error = (labelMat - h)
		# 3 x 1 (n x 1)
		#       = 3 x 1 +           (3 x 100) * (100 x 1)
		weights = weights + alpha * dataMatrix.transpose() * error
	return weights

def plotBestFit(weights):
	import matplotlib.pyplot as plt
	# Convert weights matrix to array
	# weights = wei.getA()
	dataMat , labelMat = loadDataSet()
	dataArr = np.array(dataMat)
	n = dataArr.shape[0]
	xcoord1 = []
	ycoord1 = []
	xcoord2 = []
	ycoord2 = []
	# break up data based on label
	for i in range(n):
		if int(labelMat[i]) == 1:
			xcoord1.append(dataArr[i, 1])
			ycoord1.append(dataArr[i, 2])
		else:
			xcoord2.append(dataArr[i, 1])
			ycoord2.append(dataArr[i, 2])
	fig = plt.figure()
	ax = fig.add_subplot(111)
	# plot different classes different colors
	ax.scatter(xcoord1, ycoord1, s=30, c='red', marker='s')
	ax.scatter(xcoord2, ycoord2, s=30, c='green')
	x = np.arange(-3.0, 3.0, 0.1)
	# best line fit
	# set x0 = 1, solve for x2 - don't get confused. plotting x2 ~ x1
	y = (- weights[0] - weights[1] * x) / weights[2]
	ax.plot(x, y)
	plt.xlabel('X1')
	plt.ylabel('X2')
	plt.show()

def stochGradAscent0(dataMatrix, classLabels):
	m, n = dataMatrix.shape
	alpha = 0.01
	weights = np.ones(n)
	for i in range(m):
		# h and error are single values, not vectors
		h = sigmoid(sum(dataMatrix[i] * weights))
		error = classLabels[i] - h
		weights = weights + alpha * error * dataMatrix[i]
	return weights

def stochGradAscent1(dataMatrix, classLabels,numIter = 150):
	m, n = dataMatrix.shape
	# alpha = 0.01
	weights = np.ones(n)
	for j in range(numIter):
		dataIndex = range(m)
		for i in range(m):
			# alpha changes with each iteration
			alpha = 4/(1.0 + j + i) + 0.01
			randIndex = int(np.random.uniform(0, len(dataIndex)))
			# h and error are single values, not vectors
			h = sigmoid(sum(dataMatrix[randIndex] * weights))
			error = classLabels[randIndex] - h
			weights = weights + alpha * error * dataMatrix[randIndex]
			del(dataIndex[randIndex])
	return weights

def classifyVector(inX, weights):
	prob = sigmoid(sum(inX * weights))
	if prob > 0.5: 
		return 1.0
	else: 
		return 0.0

def colicTest():
	frTrain = open('horseColicTraining.txt'); frTest = open('horseColicTest.txt')
	trainingSet = []
	trainingLabels = []
	for line in frTrain.readlines():
		currLine = line.strip().split('\t')
		lineArr = []
		for i in range(21):
			lineArr.append(float(currLine[i]))
		trainingSet.append(lineArr)
		trainingLabels.append(float(currLine[21]))
	trainWeights = stochGradAscent1(np.array(trainingSet), trainingLabels, 1000)
	errorCount = 0; numTestVec = 0.0
	for line in frTest.readlines():
		numTestVec += 1.0
		currLine = line.strip().split('\t')
		lineArr = []
		for i in range(21):
			lineArr.append(float(currLine[i]))
		if int(classifyVector(np.array(lineArr), trainWeights))!= int(currLine[21]):
			errorCount += 1
	errorRate = (float(errorCount)/numTestVec)
	print "the error rate of this test is: %f" % errorRate
	return errorRate

def multiTest():
	numTests = 10
	errorSum = 0.0
	for k in range(numTests):
		errorSum += colicTest()
	print "after %d iterations the average error rate is: %f" % (numTests, errorSum/float(numTests))
        