#
#	kNN.py
#	/Users/bartev/Development/full-sail/mach-lrn-in-act/ch02-knn/kNN.py
#
#	Bartev Vartanian on  12/26/13
#



import numpy as np
# from numpy import *
import operator
from os import listdir

def createDataSet():
	""" Create a data set - convenience function """
	group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['a', 'a', 'b', 'b']
	return group, labels

group, labels = createDataSet()


def classify0(inX, dataSet, labels, k):
	""" inX = input vector to classify
		dataSet = Full matrix of training examples
		labels = vector of labels
		k = number of nearest neighbors in vote """
	dataSetSize = dataSet.shape[0]
	# Distance calculation
	# why use tile? subtracting vector from matrix is easier.
	# diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	diffMat = dataSet - inX
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5
	sortedDistIndices = distances.argsort()
	classCount = {}
	# Vote with lowest k distances
	for i in range(k):
		voteIlabel = labels[sortedDistIndices[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	# Sort dictionary
	# sortedClassCount = sorted(classCount.iteritems(),
	# 	key=operator.itemgetter(1),
	# 	reverse=True)
	sortedClassCount = sorted(classCount.items(),
		key=lambda(k, v): v,
		reverse=True)
	return sortedClassCount[0][0]

def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)
	# Create NumPy matrix to return
	returnMat = np.zeros((numberOfLines, 3))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index, :] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat, classLabelVector

def autoNorm(dataSet):
	# Get min/max for each column (if used (1), then would be each row)
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = np.zeros(np.shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - np.tile(minVals, (m, 1))
	# Element-wise division
	normDataSet = normDataSet/np.tile(ranges, (m, 1))
	return normDataSet, ranges, minVals

def datingClassTest():
	hoRatio = 0.1
	datingDatMat, datingLabels = file2matrix('datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDatMat)
	# num rows in normalized matrix
	m = normMat.shape[0]
	numTestVecs = int(m * hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
		print "The classifier came back with %d, the real answer is: %d" % (classifierResult, datingLabels[i])
		if (classifierResult != datingLabels[i]): 
			errorCount += 1.0
	print "The total error rate is: %f" % (errorCount/float(numTestVecs))


def classifyPerson():
	resultList = ['not at all', 'in small doses', 'in large doses']
	percentTats = float(raw_input("percentage of time spent playing video games? "))
	ffMiles = float(raw_input("frequent flier miles earned per year? "))
	iceCream = float(raw_input("liters of ice cream consumed per year? "))
	datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDataMat)
	inArr = np.array([ffMiles, percentTats, iceCream])
	classifierResult = classify0((inArr - minVals) / ranges, 
									normMat, 
									datingLabels, 
									3)
	print "You will probably like this person: ", resultList[classifierResult - 1]

def img2vector(filename):
	returnVect = np.zeros((1, 1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0, 32 * i + j] = int(lineStr[j])
	return returnVect

def handwritingClassTest():
	hwLabels = []
	# Get contents of directory as a list
	trainingFileList = listdir('digits/trainingDigits')
	# How many files are in the training set
	m = len(trainingFileList)
	# Create training matrix
	# 1 row for each data point, 1 column for each pixel in the data point
	# matrix holds each image as a single row
	trainingMat = np.zeros((m, 1024))
	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		# parse class number from filename
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		# load image, convert to vector
		trainingMat[i, :] = img2vector('digits/trainingDigits/%s' %fileNameStr)
	testFileList = listdir('digits/testDigits')
	errorCount = 0.0
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('digits/testDigits/%s' % fileNameStr)
		classifierResult = classify0(vectorUnderTest, 
									trainingMat,
									hwLabels,
									3)
		print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
		if (classifierResult != classNumStr): errorCount += 1.0
	print "\nthe total number of errors is: %d" % errorCount
	print "\nthe total error rate is: %f" % (errorCount/float(mTest))
	


