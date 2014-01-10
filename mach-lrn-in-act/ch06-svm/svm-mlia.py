import numpy as np
import pandas as pd

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
			fXi = float(np.multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T)) + b
			# Ei = error based on prediction
			Ei = fXi - float(labelMat[i])
			#  If error is large, then alpha can be optimized
			if ((labelMat[i] * Ei < toler) and (alphas[i] < C)) or \
				((labelMat[i] * Ei > toler) and (alphas[i] > 0)):
				# Enter optimiztion if alphas can be changed
				# Randomly select 2nd alpha
				j = selectJrand(i, m)
				# fXj = prediction of class
				fXj = float(np.multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[j, :].T)) + b
				# Ej = error for 2nd alpha
				Ej = fXj - float(labelMat[j])
				alphaIold = alphas[i].copy()
				alphaJold = alphas[j].copy()
				#  Guarantee alpha stays between 0 and C
				if(labelMat[i] != labelMat[j]):
					L = max(0, alphas[j] - alphas[i])
					H = min(C, C + alphas[j] - alphas[i])
				else:
					L = max(0, alphas[j] + alphas[i] - C)
					H = min(C, alphas[j] + alphas[i])
				if L == H:
					print "L == H"
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
					print "j not moving enough"
					continue
				# Change alpha[i] by opposite sign
				alphas[i] += labelMat[j] * labelMat[i] * (alphaJold - alphas[j])
				# Set constant term after adjusting alphas
				b1 = b - Ei - labelMat[i] * (alphas[i] - alphaIold) * \
					dataMatrix[i, :] * dataMatrix[i, :].T - \
					labelMat[j] * (alphas[j] - alphaJold) * \
					dataMatrix[i, :] * dataMatrix[j, :].T
					# i vs j here?
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
				print "iter: %d i: %d, pairs changed %d" % (iter, i, alphaPairsChanged)
		#  Exit while loop if go through maxIter times without changing alphas
		if (alphaPairsChanged == 0):
			iter += 1
		else:
			iter = 0
		print "iteration number: %d" % iter
	return b, alphas
	



