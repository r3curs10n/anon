from scipy.sparse import csr_matrix
class Proc:
	def __init__(self):
		self.preprocess = None
		self.classifier = None
		self.densify = None
		self.X = []
		self.Y = []
		self.Xp = []
	def prepare_input(self):
		self.Xp = self.preprocess.preprocess_X(self.X)
	def fit_classifier(self):
		if self.densify:
			self.classifier = self.classifier.fit(csr_matrix(self.Xp).todense(), self.Y)
		else:
			self.classifier = self.classifier.fit(self.Xp, self.Y)
	def predict(self,X_to_predict):
		X_to_predict = self.preprocess.preprocess_Y(X_to_predict)
		
		if self.densify:
			X_to_predict = csr_matrix(X_to_predict).todense()
		return self.classifier.predict(X_to_predict)

