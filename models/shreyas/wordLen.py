import nltk
import cPickle
import sys, os, re
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
	for k in dic.keys():
		print '%s: %d' % (k, dic[k])

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
	# for k in dic.keys():
	# 	print '%s: %d/%d' % (k, dic[k][0], dic[k][1])
	# print '%d/%d = %f' % (correct, len(Y), 1.0*correct/len(Y))
	return 1.0*correct/len(Y)


def train_chunk(X, Y, Xe, Ye):
	#clf = KNeighborsClassifier(n_neighbors=5).fit(X, Y)
	#clf = GaussianNB().fit(X, Y)
	clf = MultinomialNB().fit(X, Y)
	Yd = clf.predict(Xe)

	return stats(Ye, Yd)

def main():
	global X
	global Y

	ds = Dataset.open('quora')
	X,Y = ds.X,ds.Y


	#Z = [re.findall(r"[\w']+", x) for x in X]
	Z = [filter(None, x.split('.')) for x in X]
	Z = ["".join(s) for s in Z]
	Z = [z.split(' ') for z in Z]
	Z = [[len(s) for s in z] for z in Z]

	feature = []
	for a in Z:
		wordLenDist = [0]*100
		for ln in a:
				wordLenDist[ln]+=1
		feature.append(wordLenDist)

	X = feature
	Z = zip(X, Y)
	shuffle(Z)
	(X, Y) = zip(*Z)

	# X = [i for i in range(len(X))]

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
