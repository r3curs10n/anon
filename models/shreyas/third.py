import nltk
import cPickle
import sys, os
pth = os.path.realpath(os.path.dirname(os.path.abspath(__file__))+'/../../data')
sys.path.append(pth)
from Dataset import Dataset
from Cache import cache_it

from random import shuffle
from second import stats, istats, train_chunk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

from gensim import corpora, models, similarities

from nltk.corpus import stopwords
import re

X = []
Y = []
SIM = []

def cleanword(word):
	return re.sub(r'\W+', '', word).strip()

def main():
	global X
	global Y
	global SIM

	ds = Dataset.open('quora')
	(X, Y) = (ds.X, ds.Y)

	for i in range(0, 200):
		ans = filter(None, X[i].split('.'))
		# texts = [filter(None, sentence.split(' ')) for sentence in ans]

		if len(nltk.word_tokenize(X[i])) < 100:
			continue

		documents = ans

		# remove common words and tokenize
		stoplist = stopwords.words('english')
		stoplist.append('')
		texts = [[cleanword(word) for word in document.lower().split() if cleanword(word) not in stoplist]
				 for document in documents]

		# remove words that appear only once
		all_tokens = sum(texts, [])
		tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)

		texts = [[word for word in text if word not in tokens_once] for text in texts]

		dictionary = corpora.Dictionary(texts)
		corp = [dictionary.doc2bow(text) for text in texts]
		
		lsi = models.lsimodel.LsiModel(corpus=corp, id2word=dictionary, num_topics=2)
		
		# print lsi.print_topics(2)

		sim = []
		for j in range(1, len(ans)):
			s = ans[j]
			vec_bow = dictionary.doc2bow(s.lower().split())
			vec_lsi = lsi[vec_bow] # convert the query to LSI space
			index = similarities.MatrixSimilarity(lsi[corp]) # transform corpus to LSI space and index it
			sims = index[vec_lsi] # perform a similarity query against the corpussims = index[vec_lsi] # perform a similarity query against the corpus
			sim.append( list(enumerate(sims))[j-1][1] ) # print (document_number, document_similarity) 2-tuples

		SIM.append(sim)

	X = [[sum(sim)/(1 + len(sim))] for sim in SIM]
	print X
	Z = zip(X, Y)
	print Z
	shuffle(Z)
	(X, Y) = zip(*Z)
	si=0
	acc = 0.0
	cnt = 0
	print X,Y
	print len(X),len(Y)
	while si<len(X):
		Xe = X[si:si+50]
		Ye = Y[si:si+50]
		X1 = X[:si] + X[si+50:]
		Y1 = Y[:si] + Y[si+50:]
		print len(X1),len(Xe), len(Y1), len(Ye)
		acc += train_chunk(X1, Y1, Xe, Ye)
		cnt += 1
		si += 50

	print 'Accuracy: %f' % (acc/cnt)

if __name__=='__main__':
	main()