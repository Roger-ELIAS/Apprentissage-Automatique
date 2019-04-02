from sklearn.naive_bayes import ComplementNB
import pickle

def train(dataset): 
	X = dataset[0]     # vecteur d'image
	y = dataset[1]     # vecteur de classes

	algo = ComplementNB()
	train = algo.fit(X, y)
	pickle.dump(train, open("trainModel.joblib", "wb"))


def predict (dataset):
	train = pickle.load(open("trainModel.joblib", "rb"))
	result = train.predict(dataset)
	
	return result
