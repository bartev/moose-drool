import numpy as np
# import pandas as pd

# from numpy import mat, zeros, random

def loadDataSet(fileName):
	dataMat = []
	labelMat = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = line.strip().split('\t')
		dataMat.append([float(lineArr[0]), float(lineArr[1])])
		labelMat.append(float(lineArr[2]))
	return dataMat, labelMat

def selectJrand(i, m):
	""" Select any J not equal to i
	"""
	j = i
	while (j == i):
		j = int(np.random.uniform(0, m))
	return j

def clipAlpha(aj, H, L):
	if aj > H:
		aj = H
	if L > aj:
		aj = L
	return aj

def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
	dataMatrix = np.mat(dataMatIn)
	labelMat = np.mat(classLabels).transpose()
	b = 0
	m, n = dataMatrix.shape
	alphas = np.mat(np.zeros((m, 1)))
	# Count number of times gone through dataset without any alphas changing
	iter = 0
	while(iter < maxIter):
		alphaPairsChanged = 0
		for i in range(m):
			# fXi = Prediction of class
			# np.multiply(alphas, labelMat) does element-wise multiplication resulting in alpha(i) * y(i) terms and a (1 x m) matrix (after the transform)
			# (dataMatrix * dataMatrix[i,:].T) is the inner product of all the rows of x with the ith row. It is a (m x 1) matrix
			# Multiplying these 2, gives the sum(i=1 to m) [ alpha(i) y(i) <x(i), x>], the main term in calculating the predicted class.
			fXi = float(np.multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T)) + b
			# Ei = error based on prediction
			Ei = fXi - float(labelMat[i])
			#  If error is large, then alpha can be optimized
			if ((labelMat[i] * Ei < -toler) and (alphas[i] < C)) or \
				((labelMat[i] * Ei > toler) and (alphas[i] > 0)):
				# Enter optimiztion if alphas can be changed
				# Randomly select 2nd alpha
				j = selectJrand(i, m)
				# fXj = prediction of class for 2nd alpha
				fXj = float(np.multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[j, :].T)) + b
				# Ej = error for 2nd alpha
				Ej = fXj - float(labelMat[j])
				alphaIold = alphas[i].copy()  # copy so we don't mess with original
				alphaJold = alphas[j].copy()
				#  Guarantee alpha stays between 0 and C
				if(labelMat[i] != labelMat[j]):
					L = max(0, alphas[j] - alphas[i])
					H = min(C, C + alphas[j] - alphas[i])
				else:
					L = max(0, alphas[j] + alphas[i] - C)
					H = min(C, alphas[j] + alphas[i])
				if L == H:
					# print "L == H"
					continue
				# eta = optimal amt to change alpha[j]
				eta = 2.0 * dataMatrix[i, :] * dataMatrix[j, :].T - \
					dataMatrix[i, :] * dataMatrix[i, :].T - \
					dataMatrix[j, :] * dataMatrix[j, :].T
				# simplification for now
				if eta >= 0:
					print "eta >= 0"
					continue
				# Calculate new alpha, and clip it
				alphas[j] -= labelMat[j] * (Ei - Ej)/eta
				alphas[j] = clipAlpha(alphas[j], H, L)
				# Quit for loop if alpha didn't change much
				if (abs(alphas[j] - alphaJold) < 0.00001):
					# print "j not moving enough"
					continue
				# update i by same amount as j in opposite directin
				# Change alpha[i] by opposite sign
				alphas[i] += labelMat[j] * labelMat[i] * (alphaJold - alphas[j])
				# Set constant term after adjusting alphas
				b1 = b - Ei - labelMat[i] * (alphas[i] - alphaIold) * \
					dataMatrix[i, :] * dataMatrix[i, :].T - \
					labelMat[j] * (alphas[j] - alphaJold) * \
					dataMatrix[i, :] * dataMatrix[j, :].T
				b2 = b - Ej - labelMat[i] * (alphas[i] - alphaIold) * \
					dataMatrix[i, :] * dataMatrix[j, :].T - \
					labelMat[j] * (alphas[j] - alphaJold) * \
					dataMatrix[j, :] * dataMatrix[j, :].T
				if (0 < alphas[i]) and (C > alphas[i]):
					b = b1
				elif (0 < alphas[j]) and (C > alphas[i]):
					b = b2
				else:
					b = (b1 + b2)/2.0
				alphaPairsChanged += 1
				# print "iter: %d i: %d, pairs changed %d" % (iter, i, alphaPairsChanged)
		#  Exit while loop if go through maxIter times without changing alphas
		if (alphaPairsChanged == 0):
			iter += 1
		else:
			iter = 0
		print "iteration number: %d" % iter
	return b, alphas

def kernelTrans(X, A, kTup):
	""" kTup is a tuple that containes information about the kernel
		kTup[0]: string describing what type of kernel
		kTup[1...]: optional argument that may be needed
	"""
	m, n = np.shape(X)
	K = np.mat(np.zeros((m, 1)))
	if kTup[0] == 'lin':
		# linear kernel
		# dot product between dataset and row of dataset
		K = X * A.T
	elif kTup[0] == 'rbf':
		# radial basis function (Gaussian)
		for j in range(m):
			deltaRow = X[j, :] - A
			K[j] = deltaRow * deltaRow.T
		# element-wise division
		K = np.exp(K / (-1 * kTup[1] ** 2))
	# add additional kernel types here
	# elif ... 
	else:
		raise NameError('Houston, we have a problem - that kernel is not recognized')
	return K

class optStruct:
	""" data structure to hold all important values """
	def __init__(self, dataMatIn, classLabels, C, toler, kTup):
		self.X = dataMatIn
		self.labelMat = classLabels
		self.C = C
		self.tol = toler
		self.m = np.shape(dataMatIn)[0]
		self.alphas = np.mat(np.zeros((self.m, 1)))
		self.b = 0
		# Error cache m x 2 matrix
		# col 1 = flag bit - is eCache valid?
		# col 2 = E value
		self.eCache = np.mat(np.zeros((self.m, 2)))
		# add for using kernel
		self.K = np.mat(np.zeros((self.m, self.m)))
		# linear in m!
		# Calculated once.
		# kTup is a tuple that containes information about the kernel
		for i in range(self.m):
			self.K[:, i] = kernelTrans(self.X, self.X[i, :], kTup)

def calcEk(oS, k):
	""" calculate an E value for a given alpha. 
		Before done inline, but in full Platt SMO, 
		calculation is done more often, so pull it out 
	"""
	"""
		fXk = Prediction of class
		np.multiply(alphas, labelMat) does element-wise 
		multiplication resulting in alpha(i) * y(i) terms and 
		a (1 x m) matrix (after the transform)
		oS.K[:, k] is the kernel (inner product 
		of all the rows of x with the ith row?). 
		It is a (m x 1) matrix
		Multiplying these 2, gives the 
		sum(i=1 to m) [ alpha(i) y(i) <x(i), x>], 
		the main term in calculating the predicted class.
	"""
	fXk = float( np.multiply(oS.alphas, oS.labelMat).T * oS.K[:, k] + oS.b)
	Ek = fXk - float(oS.labelMat[k])
	return Ek

def selectJ(i, oS, Ei):
	""" select second alpha (inner loop alpha from simple SMO)
	"""
	maxK = -1
	maxDeltaE = 0
	Ej = 0
	oS.eCache[i] = [1, Ei]
	# np.nonzero retunrs indices of nonzero values
	validEcacheList = np.nonzero(oS.eCache[:, 0].A)[0]
	if (len(validEcacheList)) > 1:
		for k in validEcacheList:
			if k == i:
				continue
			Ek = calcEk(oS, k)
			deltaE = abs(Ei - Ek)
			# Choose j for maximum step size
			if (deltaE > maxDeltaE):
				maxK = k
				maxDeltaE = deltaE
				Ej = Ek
		return maxK, Ej
	else:
		j = selectJrand(i, oS.m)
		Ej = calcEk(oS, j)
	return j, Ej

def updateEk(oS, k):
	Ek = calcEk(oS, k)
	oS.eCache[k] = [1, Ek]


def innerL(i, oS):
	Ei = calcEk(oS, i)
	if ((oS.labelMat[i]*Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or \
		((oS.labelMat[i]*Ei > oS.tol) and (oS.alphas[i] > 0)):
		j, Ej = selectJ(i, oS, Ei)
		alphaIold = oS.alphas[i].copy()
		alphaJold = oS.alphas[j].copy()
		if (oS.labelMat[i] != oS.labelMat[j]):
			L = max(0, oS.alphas[j] - oS.alphas[i])
			H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
		else:
			L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
			H = min(oS.C, oS.alphas[j] + oS.alphas[i])
		if L == H:
			print "L == H"
			return 0
		# Change to use kernel
		eta = 2.0 * oS.K[i, j] - oS.K[i, i] - oS.K[j, j]
		if eta >= 0:
			print "eta >= 0"
			return 0
		oS.alphas[j] -= oS.labelMat[j] * (Ei - Ej) / eta
		oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
		# update ecache (j)
		updateEk(oS, j)
		if (abs(oS.alphas[j] - alphaJold) < 0.00001):
			# print "j not moving enough"
			return 0
		oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (alphaJold - oS.alphas[j])
		# update ecache (i)
		updateEk(oS, i)
		# Change to use kernel
		b1 = oS.b - Ei - \
			oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.K[i, i] - \
			oS.labelMat[j] * (oS.alphas[j] - alphaJold) * oS.K[i, j]
		b2 = oS.b - Ej - \
			oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.K[i, j] - \
			oS.labelMat[j] * (oS.alphas[j] - alphaJold) * oS.K[j, j]
		if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]):
			oS.b = b1
		elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]):
			oS.b = b2
		else:
			oS.b = (b1 + b2)/2.0
		return 1
	else:
		return 0

def smoP(dataMatIn, classLabels, C, toler, maxIter, kTup=('lin', 0)):
	"""  Full Platt SMO - same inputs as simple version
	"""
	# create data structure to hold all the data
	oS = optStruct(np.mat(dataMatIn), np.mat(classLabels).transpose(), C, toler, kTup)
	# initialize variables
	iter = 0
	entireSet = True
	alphaPairsChanged = 0
	# main code - similar to smoSimple, but more exit conditions
	while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
		alphaPairsChanged = 0
		if entireSet:
			# go over all values
			for i in range(oS.m):
				# call innerL to choose 2nd alpha and do optimization if possible
				alphaPairsChanged += innerL(i, oS)
				print "fullSet, iter: %d i:%d, pairs changed %d" % (iter, i, alphaPairsChanged)
			iter += 1
		else:
			# go over non-bound values
			nonBoundIs = np.nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
			for i in nonBoundIs:
				alphaPairsChanged += innerL(i, oS)
				print "non-bound, iter: %d i:%d, pairs changed %d" % (iter, i, alphaPairsChanged)
			iter += 1
		# toggle between entire set and non-bound loop
		if entireSet: 
			entireSet = False
		elif (alphaPairsChanged == 0):
			entireSet = True
		print "iteration number: %d" % iter
	return oS.b, oS.alphas

def calcWs(alphas, dataArr, classLabels):
	X = np.mat(dataArr)
	labelMat = np.mat(classLabels).transpose()
	m, n = np.shape(X)
	w = np.zeros((n, 1))
	for i in range(m):
		# w.transpose = 
		# sum over i
		# 	alpha(i) * y(i) * X(i).transpose
		w += np.multiply(alphas[i] * labelMat[i], X[i, :].T)
	return w

def testRbf(k1 = 1.3):
	dataArr, labelArr = loadDataSet('testSetRBF.txt')
	b, alphas = smoP(dataArr, labelArr, 200, 0.0001, 10000, ('rbf', k1))
	dataMat = np.mat(dataArr)
	labelMat = np.mat(labelArr).transpose()
	svInd = np.nonzero(alphas.A > 0) [0]
	# Create matrix of support vectors
	sVs = dataMat[svInd]
	labelSV = labelMat[svInd]
	print "there are %d Support Vectors" % np.shape(sVs)[0]
	print "b = " + str(b)
	# for idx in svInd:
	# 	y = labelMat[idx]
	# 	print "idx = %d, y = %f" % (idx, y)
	m, n = np.shape(dataMat)
	errorCount = 0
	for i in range(m):
		kernelEval = kernelTrans(sVs, dataMat[i, :], ('rbf', k1))
		predict = kernelEval.T * np.multiply(labelSV, alphas[svInd]) + b
		if np.sign(predict) != np.sign(labelArr[i]):
			errorCount += 1
	print "the training error rate is: %f" % (float(errorCount)/m)
	w1 = calcWs(alphas, dataArr, labelArr)
	dataArr, labelArr = loadDataSet('testSetRBF2.txt')
	errorCount = 0
	dataMat = np.mat(dataArr)
	labelMat = np.mat(labelArr).transpose()
	m, n = np.shape(dataMat)
	for i in range(m):
		kernelEval = kernelTrans(sVs, dataMat[i, :], ('rbf', k1))
		predict = kernelEval.T * np.multiply(labelSV, alphas[svInd]) + b
		if np.sign(predict) != np.sign(labelArr[i]):
			# print "ERROR predict = %f, labelArr[%d] = %f" % (predict, i, labelArr[i])
			errorCount += 1
		# else:
			# print "predict = %f, labelArr[%d] = %f" % (predict, i, labelArr[i])
	print "the test error rate is: %f" % (float(errorCount)/m)
	print "error count = %f, m = %f" % (float(errorCount), float(m))
	return b, alphas, svInd, sVs, w1



## ----- No kernel versions
def calcEkK(oS, k):
	""" calculate an E value for a given alpha. 
		Before done inline, but in full Platt SMO, 
		calculation is done more often, so pull it out 
	"""
	"""
		fXi = Prediction of class
		np.multiply(alphas, labelMat) does element-wise 
		multiplication resulting in alpha(i) * y(i) terms and 
		a (1 x m) matrix (after the transform)
		(dataMatrix * dataMatrix[i,:].T) is the inner product 
		of all the rows of x with the ith row. 
		It is a (m x 1) matrix
		Multiplying these 2, gives the 
		sum(i=1 to m) [ alpha(i) y(i) <x(i), x>], 
		the main term in calculating the predicted class.
	"""
	fXk = float( np.multiply(oS.alphas, oS.labelMat).T * (oS.X * oS.X[k, :].T) + oS.b)
	Ek = fXk - float(oS.labelMat[k])
	return Ek

def innerLK(i, oS):
	""" original version - other version allows use of kernel
	"""
	Ei = calcEk(oS, i)
	if ((oS.labelMat[i]*Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or \
		((oS.labelMat[i]*Ei > oS.tol) and (oS.alphas[i] > 0)):
		j, Ej = selectJ(i, oS, Ei)
		alphaIold = oS.alphas[i].copy()
		alphaJold = oS.alphas[j].copy()
		if (oS.labelMat[i] != oS.labelMat[j]):
			L = max(0, oS.alphas[j] - oS.alphas[i])
			H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
		else:
			L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
			H = min(oS.C, oS.alphas[j] + oS.alphas[i])
		if L == H:
			print "L == H"
			return 0
		eta = 2.0 * oS.X[i, :] * oS.X[j, :].T \
				- oS.X[i, :] * oS.X[i, :].T \
				- oS.X[j, :] * oS.X[j, :].T
		if eta >= 0:
			print "eta >= 0"
			return 0
		oS.alphas[j] -= oS.labelMat[j] * (Ei - Ej) / eta
		oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
		# update ecache (j)
		updateEk(oS, j)
		if (abs(oS.alphas[j] - alphaJold) < 0.00001):
			print "j not moving enough"
			return 0
		oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] \
			* (alphaJold - oS.alphas[j])
		# update ecache (i)
		updateEk(oS, i)
		b1 = oS.b - Ei - \
			oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :] * oS.X[i, :].T - \
			oS.labelMat[j] * (oS.alphas[j] - alphaJold) * oS.X[i, :] * oS.X[j, :].T
		b2 = oS.b - Ej - \
			oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :] * oS.X[j, :].T - \
			oS.labelMat[j] * (oS.alphas[j] - alphaJold) * oS.X[j, :] * oS.X[j, :].T
		if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]):
			oS.b = b1
		elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]):
			oS.b = b2
		else:
			oS.b = (b1 + b2)/2.0
		return 1
	else:
		return 0


## ---- start testing with already MLIA code instead of mine

def testRbfMlia(k1=1.3):
    dataArr, labelArr = loadDataSet('testSetRBF.txt')
    b, alphas = smoP(dataArr, labelArr, 200, 0.0001, 10000, ('rbf', k1)) #C=200 important
    datMat = np.mat(dataArr)
    labelMat = np.mat(labelArr).transpose()
    svInd = np.nonzero(alphas.A > 0)[0]
    sVs = datMat[svInd] #get matrix of only support vectors
    labelSV = labelMat[svInd]
    print "there are %d Support Vectors" % np.shape(sVs)[0]
    print "b = " + str(b)
    # for idx in svInd:
    #     y = labelMat[idx]
    #     print "idx = %d, y = %f" % (idx, y)
    m, n = np.shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i, :], ('rbf', k1))
        predict = kernelEval.T * np.multiply(labelSV, alphas[svInd]) + b
        if np.sign(predict) != np.sign(labelArr[i]): errorCount += 1
    print "the training error rate is: %f" % (float(errorCount)/m)
    w1 = calcWs(alphas, dataArr, labelArr)
    dataArr, labelArr = loadDataSet('testSetRBF2.txt')
    errorCount = 0
    datMat = np.mat(dataArr)
    labelMat = np.mat(labelArr).transpose()
    m, n = np.shape(datMat)
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i, :], ('rbf', k1))
        predict = kernelEval.T * np.multiply(labelSV, alphas[svInd]) + b
        if np.sign(predict)!= np.sign(labelArr[i]): 
            # print "ERROR predict = %f, labelArr[%d] = %f" % (predict, i, labelArr[i])
            errorCount += 1    
        # else:
            # print "predict = %f, labelArr[%d] = %f" % (predict, i, labelArr[i])
    print "the test error rate is: %f" % (float(errorCount)/m)    
    return b, alphas, svInd, sVs, w1









