import nltk
import cPickle
import sys, os
pth = os.path.realpath(os.path.dirname(os.path.abspath(__file__))+'/../../Data')
sys.path.append(pth)
from Dataset import Dataset
from Cache import cache_it

from random import shuffle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
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
	for k in dic.keys():
		print '%s: %d/%d' % (k, dic[k][0], dic[k][1])
	print '%d/%d = %f' % (correct, len(Y), 1.0*correct/len(Y))

@cache_it
def get_tagged_text(X):
	return [pos_tags(x) for x in X]

def main():
	global X
	global Y
	ds = Dataset.open('quora')
	(X, Y) = (get_tagged_text(ds.X), ds.Y)

	XX=[]
	YY=[]
	for (auth, ans) in zip(Y, X):
	 	if len(nltk.word_tokenize(ans)) > 200:
	 		XX.append(ans)
	 		YY.append(auth)
	(X, Y) = (XX, YY)

	Z = zip(X, Y)
	shuffle(Z)
	(X, Y) = zip(*Z)
	Xe = X[-50:]
	Ye = Y[-50:]
	X = X[:-50]
	Y = Y[:-50]

	count_vect = CountVectorizer(input='content',ngram_range=(2,3), min_df=0.2, max_df=1.0)
	X_train_counts = count_vect.fit_transform(X)
	tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
	X_train_tf = tf_transformer.transform(X_train_counts)

	clf = MultinomialNB().fit(X_train_tf, Y)
	clf2 = KNeighborsClassifier(n_neighbours=5).fit(X_train_tf, Y)

	X_new_counts = count_vect.transform(Xe)
	X_new_tfidf = tf_transformer.transform(X_new_counts)
	Yd = clf.predict(X_new_tfidf)

	istats(Y)
	print ''
	stats(Ye, Yd)

if __name__=='__main__':
	main()