import numpy as np
from math import log
import operator as op

def createDataSet():
	dataSet = [[1, 1, 'yes'],
				[1, 1, 'yes'],
				[1, 0, 'no'],
				[0, 1, 'no'],
				[0, 1, 'no']]
	labels = ['no surfacing','flippers']
	return dataSet, labels

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	# Create dictionary of all possible classes
	for featVec in dataSet:
		currentLabel = featVec[-1]
		# if currentLabel not in labelCounts.keys():
		# 	labelCounts[currentLabel] = 0
		# labelCounts[currentLabel] += 1
		labelCounts[currentLabel] = labelCounts.get(currentLabel, 0) + 1
	shanonEnt = 0.0
	# Get probabilities from key counts
	for key in labelCounts:
		prob = float(labelCounts[key]) / numEntries
		# log base 2
		shanonEnt -= prob * log(prob, 2)
	return shanonEnt

def splitDataSet(dataSet, axis, value):
	""" dataSet to split,
		axis = feature to split on
		value = value of feature to return
		
		pulls out all feature vectors that match dataSet[axis] == value
		filtering out the element dataSet[axis].
	"""
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			# Cut out the feature to split on
			# This would be easier using a pandas DataFrame?
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis + 1: ])
			retDataSet.append(reducedFeatVec)
	return retDataSet

def chooseBestFeatureToSplit(dataSet):
	# Assume data is a list of lists, each the same length
	# class label is in the last column
	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeature = -1
	for i in range(numFeatures):
		# Create unique list of class labels
		# For every row in dataSet, get list of ith entry
		# Easier with pandas data frame?
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		# Calculate entropy for each split
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet) / float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		# find the best information gain
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature


def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		# if vote not in classCount.keys(): classCount[vote] = 0
		# classCount[vote] += 1
		# This is cleaner (don't know about speed) than the code in MLIA
		classCount[vote] = classCount.get(vote, 0) + 1
	sortedClassCount = sorted(classCount.iteritems(), 
							# key=operator.itemgetter(1),  # code from MLIA
							key=lambda(k, v): v, 	# My version not using operator
							reverse=True)
	return sortedClassCount[0][0]

def createTree(dataSet, labels):
	""" labels contains a label for each feature in dataSet
	
		The result is a lot of nested dictionaries
		representing the tree.
	"""
	# Create list of all class labels in the data set
	classList = [example[-1] for example in dataSet]
	# Stop when all classes are equal
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	# Stop when there are no more features (return majority)
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)
	# Choose best feature if did not meet stopping conditions
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	# Create the tree! (store in a python dictionary)
	myTree = {bestFeatLabel : {}}
	# Get a list of unique values for chosen feature (bestFeat)
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	# Iterate over unique values and recursively call createTree()
	for value in uniqueVals:
		subLabels = labels[:]		# Creates copy of labels
		# Recursive step
		myTree[bestFeatLabel][value] = createTree( splitDataSet(dataSet, bestFeat, value), subLabels)
	return myTree


def classify(inputTree, featLabels, testVec):
	firstStr = inputTree.keys()[0]
	secondDict = inputTree[firstStr]
	# Translate label string to index
	featIndex = featLabels.index(firstStr)
	for key in secondDict.keys():
		if testVec[featIndex] == key:
			if isinstance(secondDict[key], dict):
				classLabel = classify(secondDict[key], featLabels, testVec)
			else:
				classLabel = secondDict[key]
	return classLabel

def storeTree(inputTree, filename):
	import pickle
	fw = open(filename, 'w')
	pickle.dump(inputTree, fw)
	fw.close()

def grabTree(filename):
	import pickle
	fr = open(filename)
	return pickle.load(fr)


