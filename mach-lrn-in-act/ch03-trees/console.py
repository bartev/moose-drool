myData, labels = createDataSet()

data = {'a':1, 'b':2}

mylist = ['a', 'b', 'a', 'c', 'a', 'b', 'c']

myTree = retrieveTree(0)


fr=open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = createTree(lenses, lensesLabels)
createPlot(lensesTree)

storeTree((lensesTree, lensesLabels), 'lensesTreeClassifier.txt')
tree, labs = grabTree('lensesTreeClassifier.txt')