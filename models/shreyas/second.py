import nltk
import cPickle
import sys, os
pth = os.path.realpath(os.path.dirname(os.path.abspath(__file__))+'/../../data')
sys.path.append(pth)
from Dataset import Dataset
from Cache import cache_it

from random import shuffle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

def pos_tags(text):
	return ' '.join([tag for (word, tag) in nltk.pos_tag(nltk.word_tokenize(text))])

X = []
Y = []

def istats(Y):
	dic = {}
	for y in Y:
		c = dic.get(y, 0)
		dic[y] = c+1
	# for k in dic.keys():
	# 	print '%s: %d' % (k, dic[k])

def stats(Y, Yd):
	Yz = zip(Y, Yd)
	correct = sum(1 for (y, yd) in Yz if y==yd)
	dic = {}
	for (y, yd) in Yz:
		(c, t) = dic.get(y, (0,0))
		if y==yd:
			c+=1
		t+=1
		dic[y] = (c,t)
		
	return 1.0*correct/len(Y)


def train_chunk(X, Y, Xe, Ye):
	clf = KNeighborsClassifier(n_neighbors=5).fit(X, Y)
	#clf = GaussianNB().fit(X, Y)

	Yd = clf.predict(Xe)

	return stats(Ye, Yd)

def main():
	global X
	global Y

	ds = Dataset.open('quora')
	(X, Y) = ([x.split('.') for x in ds.X], ds.Y)
	X = ([sum([len( filter(None, y.split(' ')) ) for y in x])/len(x) for x in X])
	X = zip(X, [len( filter(None, x.split('\n')) ) for x in ds.X])

	# print [x for x in ds.X if len( filter(None, x.split('\n')) ) > 1]

	# print [(x, y) for (x, y) in X if y > 1]
	X = [[x, y] for (x, y) in X]



	Z = zip(X, Y)
	shuffle(Z)
	(X, Y) = zip(*Z)
	si=0
	acc = 0.0
	cnt = 0
	while si<len(X):
		Xe = X[si:si+50]
		Ye = Y[si:si+50]
		X1 = X[:si] + X[si+50:]
		Y1 = Y[:si] + Y[si+50:]
		acc += train_chunk(X1, Y1, Xe, Ye)
		cnt += 1
		si += 50

	print 'Accuracy: %f' % (acc/cnt)

if __name__=='__main__':
	main()