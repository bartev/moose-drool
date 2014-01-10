listOfPosts,listClasses = loadDataSet()
myVocabList = createVocabList(listOPosts)

setOfWords2Vec(myVocabList, listOPosts[0])
setOfWords2Vec(myVocabList, listOPosts[3])

trainMat = []
for postInDoc in listOfPosts:
	trainMat.append(setOfWords2Vec(myVocabList, postInDoc))

p0V, p1V, pAb = trainNBO(trainMat, listClasses)



mySent='This book is the best book on Python or M.L. I have ever laid eyes upon.'
mySent.split()

import re
regEx = re.compile('\\W*')
listOfTokens = regEx.split(mySent)

[tok.lower() for tok in listOfTokens if len(tok) > 0]

emailText = open('email/ham/6.txt').read()
listOfTokens = regEx.split(emailText)


run bayes.py
import feedparser as fp
ny = fp.parse('http://newyork.craigslist.org/stp/index.rss')
sf = fp.parse('http://sfbay.craigslist.org/stp/index.rss')
vocabList, pSF, pNY = localWords(ny, sf)
