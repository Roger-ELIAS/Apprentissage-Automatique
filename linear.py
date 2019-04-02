from sklearn import svm
import pickle

def train(dataset): 
	test = svm.SVC(gamma="auto").fit(dataset[0],dataset[1])
	pickle.dump(test, open("trainModelSVC.joblib", "wb"))


def predict (dataset):
	train = pickle.load(open("trainModel.joblib", "rb"))
	result = train.predict(dataset)
	
	return result