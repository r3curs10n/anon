import datetime
import cPickle
import os

class Dataset:
	def __init__(self):
		self.X = []
		self.Y = []
		self.ts = datetime.datetime(1970,1,1)

	@staticmethod
	def open(dsname):
		path = os.path.dirname(os.path.abspath(__file__)) + '/' + dsname + '/data'
		with open(path) as f:
			ds = cPickle.load(f)
			return ds