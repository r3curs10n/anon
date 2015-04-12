import nltk
import cPickle
import sys, os
pth = os.path.realpath(os.path.dirname(os.path.abspath(__file__))+'/../../data')
sys.path.append(pth)
from Dataset import Dataset
from Cache import cache_it
from Proc import Proc

from random import shuffle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from nltk.tokenize import RegexpTokenizer

from first import get_tagged_text

def pos_tags(text):
	return ' '.join([tag for (word, tag) in nltk.pos_tag(nltk.word_tokenize(text))])

X = []
Y = []
ans_to_tag = {}

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


class feature1:
	def __init__(self):
		self.count_vect = CountVectorizer(input='content',ngram_range=(2,3), min_df=0.2, max_df=1.0)
	def preprocess_X(self, X):
		X = [ans_to_tag[ans] for ans in X]
		X_train_counts = self.count_vect.fit_transform(X)
		self.tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
		X_train_tf = self.tf_transformer.transform(X_train_counts)
		return X_train_tf
	def preprocess_Y(self, Y):
		X_new_counts = self.count_vect.transform(Y)
		return self.tf_transformer.transform(X_new_counts)

# def feature1(X):
# 	X = [ans_to_tag[ans] for ans in X]
# 	count_vect = CountVectorizer(input='content',ngram_range=(2,3), min_df=0.2, max_df=1.0)
# 	X_train_counts = count_vect.fit_transform(X)
# 	tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
# 	X_train_tf = tf_transformer.transform(X_train_counts)
# 	return X_train_tf

class feature2:
	def __init__(self):
		pass
	def preprocess_common(self, X):
		Xf = [x.split('.') for x in X]
		Xf = ([sum([len( filter(None, y.split(' ')) ) for y in x])/len(x) for x in Xf])
		Xf = zip(Xf, [len( filter(None, x.split('\n')) ) for x in X])
		Xf = [[x, y] for (x, y) in Xf]
		return Xf
	def preprocess_X(self, X):
		return self.preprocess_common(X)
	def preprocess_Y(self, X):
		return self.preprocess_common(X)


class feature3:
	def __init__(self):
		pass
	def preprocess_common(self, X):
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
		return feature

	def preprocess_X(self, X):
		return self.preprocess_common(X)
	def preprocess_Y(self, X):
		return self.preprocess_common(X)

class feature4:
	def __init__(self):
		pass
	def preprocess_common(self, X):
		feature = []
		tokenizer = RegexpTokenizer(r'\w+')
		for x in X:
			All = len(nltk.word_tokenize(x))
			numPunctuation = All - len(tokenizer.tokenize(x))
			numWords = All - numPunctuation
			ff = [abs(numPunctuation), abs(numWords)]
			feature.append(ff)
		return feature
	def preprocess_X(self, X):
		return self.preprocess_common(X)
	def preprocess_Y(self, X):
		return self.preprocess_common(X)


# def feature2(X):
# 	Xf = [x.split('.') for x in X]
# 	Xf = ([sum([len( filter(None, y.split(' ')) ) for y in x])/len(x) for x in Xf])
# 	Xf = zip(Xf, [len( filter(None, x.split('\n')) ) for x in X])
# 	Xf = [[x, y] for (x, y) in Xf]
# 	return Xf


auth_to_id = {}

def addVector(lst, authName):
	for auth in auth_to_id:
		lst.append(1 if auth==authName else 0)
@cache_it
def gen_feature_vector(X, Y, Xe):
	classifiers = [KNeighborsClassifier(n_neighbors=6),
				   GaussianNB(),
	 			   MultinomialNB(),
				   svm.SVC(),
				   RandomForestClassifier(n_estimators=5)]
	densify = [False, True, True, False, True]
	features = [feature1(), feature2(), feature3(), feature4()]

	p = Proc()
	p.X = X
	p.Y = Y

	new_feature_vector = [[] for i in X]
	new_feature_vector_Xe = [[] for i in Xe]
	
	for f in features:
		p.preprocess = f
		p.prepare_input()
		for (dens, c) in zip(densify, classifiers):
			p.classifier = c
			p.densify = dens
			p.fit_classifier()
			Yd = p.predict(X)
			Yde = p.predict(Xe)
			for v, predicted_y in zip(new_feature_vector, Yd):
				addVector(v,predicted_y)
			for v, predicted_y in zip(new_feature_vector_Xe, Yde):
				addVector(v,predicted_y)
			

	return new_feature_vector, new_feature_vector_Xe




def train_chunk(X, Y, Xe, Ye):
	# clf = KNeighborsClassifier(n_neighbors=8).fit(X, Y)
	clf = GaussianNB().fit(X, Y)
	# clf = svm.SVC().fit(X,Y)
	# clf = RandomForestClassifier(n_estimators=5).fit(X,Y)
	Yd = clf.predict(Xe)

	return stats(Ye, Yd)
	
def getTagsforAll(answers):
	tags = get_tagged_text(answers)
	for ans, tag in zip(answers, tags):
		ans_to_tag[ans] = tag
	print 'tagging done'

@cache_it
def pred_shuffle(X):
	X = X[:]
	shuffle(X)
	return X

def main():
	global X
	global Y
	global auth_to_id

	ds = Dataset.open('quora')
	# (X, Y) = ([x.split('.') for x in ds.X], ds.Y)
	#X = ([sum([len( filter(None, y.split(' ')) ) for y in x])/len(x) for x in X])
	#X = zip(X, [len( filter(None, x.split('\n')) ) for x in ds.X])
	(X, Y) = (ds.X, ds.Y)

	mx = 0
	for auth in Y:
		if auth not in auth_to_id:
			auth_to_id[auth] = mx
			mx+=1

	getTagsforAll(X)
	# print [x for x in ds.X if len( filter(None, x.split('\n')) ) > 1]

	# print [(x, y) for (x, y) in X if y > 1]
	#X = [[x, y] for (x, y) in X]



	Z = zip(X, Y)
	Z = pred_shuffle(Z)
	(X, Y) = zip(*Z)
	si=0
	acc = 0.0
	cnt = 0
	while si<len(X):
		print "doing iteration ", cnt
		Xe = X[si:si+50]
		Ye = Y[si:si+50]
		X1 = X[:si] + X[si+50:]
		Y1 = Y[:si] + Y[si+50:]
		train, pred  = gen_feature_vector(X1, Y1, Xe)
		acc += train_chunk(train, Y1, pred, Ye)
		cnt += 1
		si += 50

	print 'Accuracy: %f' % (acc/cnt)

if __name__=='__main__':
	main()