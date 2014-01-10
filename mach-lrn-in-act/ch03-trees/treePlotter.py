import matplotlib.pyplot as plt
plt.interactive(True)

# Define box and arrow formatting
decisionNode = dict(boxstyle='sawtooth', fc='0.8')  # fc = 1 : white, 0 : black
leafNode = dict(boxstyle='round', fc='0.8')
arrow_args = dict(arrowstyle='<-')

# createPlot.ax1 is a global variabl
# plotNode draws on createPlot.ax1
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
	""" draw annotations with arrows """
	createPlot.ax1.annotate(nodeTxt, 
				xy=parentPt, 
				xycoords='axes fraction',
				xytext=centerPt,
				textcoords='axes fraction',
				va='center',
				ha='center',
				bbox=nodeType,
				arrowprops=arrow_args)

def testCreatePlot():
	""" create new figure, clear it, draw 2 nodes"""
	fig = plt.figure(1, facecolor='white')
	fig.clf()
	createPlot.ax1 = plt.subplot(111, frameon=False)
	plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
	plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
	plotNode('a 2nd leaf node', (0.5, 0.5), (0.3, 0.5), leafNode)
	plotNode('a 3rd leaf node', (0.5, 0.9), (0.3, 0.5), leafNode)
	plotNode('a 4th leaf node', (0.2, 0.7), (0.2, 0.4), leafNode)
	# plotNode('a 3rd leaf node', (0.5, 1.5), (0.5, 0.5), leafNode)
	plt.show()

def getNumLeafs(myTree):
	""" Traverse entire tree to count leaf nodes"""
	numLeafs = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		# if type(secondDict[key]).__name__ == 'dict':
		if isinstance(secondDict[key], dict):	# isinstance preferred over type()
			numLeafs += getNumLeafs(secondDict[key])
		else: numLeafs += 1
	return numLeafs

def getTreeDepth(myTree):
	""" Count number of decision nodes. Stop at leaf nodes """
	maxDepth = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if isinstance(secondDict[key], dict):
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else: thisDepth = 1
		if thisDepth > maxDepth: maxDepth = thisDepth
	return maxDepth

# Helper function for testing
def retrieveTree(i):
	listOfTrees = [{'no surfacing': 
						{0: 'no', 
						 1: {'flippers': {0: 'no', 1: 'yes'}}}},
					{'no surfacing':
						{0: 'no',
						 1: {'flippers': 
						 	{0: {'head': {0: 'no', 1: 'yes'}},
						 	 1: 'no'}}}},
					{'no surfacing':
						{0: 'no',
						 1: {'flippers': 
						 	{0: {'head': {0: 'no', 1: 'yes'}},
						 	 1: 'no'}},
						 3: 'maybe'}},
					{'no surfacing':
						{0: 'no',
						 1: {'flippers': 
						 	{0: {'head': {0: 'no', 1: 'yes'}},
						 	 1: 'no'}},
						 2: {'fins':
						 	{0: {'tail': {0: 'yes', 1: 'no'}},
						 	 1: 'other'}},
						 3: {'maybe':
						 	{5: 'earth',
						 	 6: 'sea'}}}}
					]
	return listOfTrees[i]

def plotMidText(centerPt, parentPt, txtString):
	""" Plot text between child and parent
	"""
	xMid = (parentPt[0] - centerPt[0]) / 2.0 + centerPt[0]
	yMid = (parentPt[1] - centerPt[1]) / 2.0 + centerPt[1]
	createPlot.ax1.text(xMid, yMid, txtString, va='center', ha='center', rotation=30)

def plotTree(myTree, parentPt, nodeTxt):
	# Get width and height
	numLeafs = getNumLeafs(myTree)
	getTreeDepth(myTree)
	firstStr = myTree.keys()[0]
	centerPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
	plotMidText(centerPt, parentPt, nodeTxt)
	plotNode(firstStr, centerPt, parentPt, decisionNode)
	secondDict = myTree[firstStr]
	plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
	for key in secondDict.keys():
		# if type(secondDict[key]).__name__=='dict':
		if isinstance(secondDict[key], dict):
			plotTree(secondDict[key], centerPt, str(key))
		else:
			plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
			plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), centerPt, leafNode)
			plotMidText((plotTree.xOff, plotTree.yOff), centerPt, str(key))
	plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def createPlot(inTree):
	fig = plt.figure(1, facecolor='white')
	fig.clf()
	axprops = dict(xticks=[], yticks=[])
	createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
	# createPlot.ax1 = plt.subplot(111, frameon=False)
	plotTree.totalW = float(getNumLeafs(inTree))
	plotTree.totalD = float(getTreeDepth(inTree))
	plotTree.xOff = -0.5/plotTree.totalW
	plotTree.yOff = 1.0
	plotTree(inTree, (0.5, 1.0), '')
	plt.show()


# Global variables are set up
# Width and depth of tree
# plotTree.totalW -- width
# plotTree.totalD -- depth

# Keep track of what has been plotted and appropriate coordinat for next node
# plotTree.xOff
# plotTree.yOff

