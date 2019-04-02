from sklearn import svm
from sklearn.metrics.pairwise import chi2_kernel
import pickle

def train(dataset): 
    test = svm.SVC(kernel=chi2_kernel).fit(dataset[0],dataset[1])
    pickle.dump(test, open("trainModelChi2.joblib", "wb"))

def predict (dataset):
	train = pickle.load(open("trainModel.joblib", "rb"))
	result = train.predict(dataset)
	
	return result
