import numpy as np

def loadDataSet():
	""" create sample data """
	postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
		['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
		['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
		['stop', 'posting', 'stupid', 'worthless', 'garbage'],
		['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
		['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
	classVec = [0, 1, 0, 1, 0, 1]	# 1 is abusive, 0 not
	return postingList, classVec

def createVocabList(dataSet):
	# create empty set
	vocabSet = set()
	for document in dataSet:
		# Create the union of 2 sets
		vocabSet = vocabSet | set(document)
	return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
	""" Take a vocab list and an input document, and return a
		vector in vocab list space indicating whether or not 
		the words are present in the document.
	"""
	# Create a vector of all 0's
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else:
			print "the word: %s is not in my vocabulary!" % word
	return returnVec

def trainNBO(trainMatrix, trainCategory):
	""" trainMatrix is a matrix of documents
		trainCategory is a vector of class labels for each document
	"""
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	# Calculate probability the doc is an abusive doc (class = 1)
	# P(0) = 1 - P(1)
	# Modify this if more than 2 classes
	pAbusive = sum(trainCategory) / float(numTrainDocs)
	# Initialize probabilities
	# Bad initialization values - better to set counts to 1 and denom to 2 as below
	# p0Num = np.zeros(numWords)		# numpy array
	# p1Num = np.zeros(numWords)
	# p0Denom = 0.0
	# p1Denom = 0.0
	# Use thes initializations for real-world problems so we don't have 0 probabilities
	p0Num = np.ones(numWords)		# numpy array
	p1Num = np.ones(numWords)
	p0Denom = 2.0
	p1Denom = 2.0
	for i in range(numTrainDocs):
		# Vector addition
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	# Element-wise division (dividing array by float)
	# Divide every element by total number of words for that class
	p1Vect = np.log(p1Num / p1Denom)		# changed to log() to avoid underflow
	p0Vect = np.log(p0Num / p0Denom)		# changed to log() to avoid underflow
	# Return 2 vectors and 1 probability
	return p0Vect, p1Vect, pAbusive

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
	p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)
	p0 = sum(vec2Classify * p0Vec) + np.log(1.0 - pClass1)
	if p1 > p0:
		return 1
	else:
		return 0

def testingNB():
	listOfPosts, listClasses = loadDataSet()
	myVocabList = createVocabList(listOfPosts)
	trainMat = []
	for postinDoc in listOfPosts:
		trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
	p0V, p1V, pAb = trainNBO(np.array(trainMat), np.array(listClasses))
	testEntry = ['love', 'my', 'dalmation']
	thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
	print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)
	testEntry = ['stupid', 'garbage']
	thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
	print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)

def bagOfWords2VecMN(vocabList, inputSet):
	""" Take a vocab list and an input document, and return a
		vector in vocab list space indicating how often each 
		word is present in the document.
	"""
	# Create a vector of all 0's
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] += 1
		# else:
			# print "the word: %s is not in my vocabulary!" % word
	return returnVec

def textParse(bigString):
	import re
	listOfTokens = re.split(r'\W*', bigString)
	result = [tok.lower() for tok in listOfTokens if len(tok) > 2]
	return result

def spamTest():
	docList = []
	classList = []
	fullText = []
	for i in range(1, 26):
		wordList = textParse(open('email/spam/%d.txt' % i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(1)
		wordList = textParse(open('email/ham/%d.txt' % i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
	# Create vocabulary
	vocabList = createVocabList(docList)
	trainingSet = range(50)
	# Create test set
	testSet = []
	for i in range(10):
		# Created random integers beetween 0 and len(trainingSet)
		randIndex = int(np.random.uniform(0, len(trainingSet)))
		testSet.append(trainingSet[randIndex])
		del(trainingSet[randIndex])
	# Can I do this all at once? - probably really easy with Pandas
	# randIndex = np.random.choice(len(trainingSet), 10, replace=False)
	# testSet.append(trainingSet[randIndex])
	# This step doesn't work
	# del(trainingSet[randIndex])
	
	trainMat = []
	trainClasses = []
	# iterate through all items in trainingSet, and create word vectors of each email and vocabulary
	for docIndex in trainingSet:
		trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
		trainClasses.append(classList[docIndex])
	# Use the training data to calculate probability vectors
	p0V, p1V, pSpam = trainNBO(np.array(trainMat), np.array(trainClasses))
	errorCount = 0
	# iterate through all items in testSet
	# create word vectors of each email and vocabulary
	# Classify each wordVector
	for docIndex in testSet:
		wordVector = setOfWords2Vec(vocabList, docList[docIndex])
		if classifyNB(np.array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
			# Increment errorCount if not classified correctly
			errorCount += 1
			print "classification error", docList[docIndex]
	print 'the error rate is: ', float(errorCount) / len(testSet)
	

def calcMostFreq(vocabList, fullText):
	# Calculate frequency of occurence
	# import operator
	freqDict = {}
	for token in vocabList:
		freqDict[token] = fullText.count(token)
	sortedFreq = sorted(freqDict.iteritems(), key=lambda (k, v): v, reverse=True)
	return sortedFreq[:30]

def localWords(feed1, feed0):
	import feedparser
	docList = []
	classList = []
	fullText = []
	minLen = min(len(feed1['entries']), len(feed0['entries']))
	for i in range(minLen):
		# access 1 feed at a time
		wordList = textParse(feed1['entries'][i]['summary'])
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(1)
		wordList = textParse(feed0['entries'][i]['summary'])
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
	vocabList = createVocabList(docList)
	# remove most frequently occurring words
	top30Words = calcMostFreq(vocabList, fullText)
	for pairW in top30Words:
		if pairW[0] in vocabList:
			vocabList.remove(pairW[0])
	trainingSet = range(2 * minLen)
	testSet = []
	for i in range(20):
		randIndex = int(np.random.uniform(0,  len(trainingSet)))
		testSet.append(trainingSet[randIndex])
		del(trainingSet[randIndex])
	trainMat = []
	trainClasses = []
	for docIndex in trainingSet:
		trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
		trainClasses.append(classList[docIndex])
	p0V, p1V, pSpam = trainNBO(np.array(trainMat), np.array(trainClasses))
	errorCount = 0
	for docIndex in testSet:
		wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
		if classifyNB(np.array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
			errorCount += 1
	print 'the error rate is: ', float(errorCount)/len(testSet)
	return vocabList, p0V, p1V
	
def getTopWords(ny, sf):
	import operator
	vocabList , p0V, p1V = localWords(ny, sf)
	topNY = []
	topSF = []
	for i in range(len(p0V)):
			if p0V[i] > -6.0: topSF.append((vocabList[i], p0V[i]))
			if p1V[i] > -6.0: topNY.append((vocabList[i], p1V[i]))	
	sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)
	for item in sortedSF:
		print item[0]
	sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
	print " NY **" * 10, "NY"
	for item in sortedNY:
		print item[0]
		
		