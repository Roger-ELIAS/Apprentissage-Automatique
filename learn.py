from sklearn.naive_bayes import ComplementNB
#from joblib import dump, load
import pickle
#def diff(a, b): 
#    target = numpy.array(a)
#    result = numpy.array(b)
#    error = numpy.mean(target != result)
#    return round(100 - error * 100, 10) 



def train(dataset): 
	X = dataset[0]     # vecteur d'image
	y = dataset[1]     # vecteur de classes

	algo = ComplementNB()
	train = algo.fit(X, y)	# entrainement de l'algo avec le set d'image
	pickle.dump(train, open("trainModel.joblib", "wb"))

# fonction de prédiction d'image qui utilise
# un algo de Bayes. Cette fonction entraine un 
# algo et essaie de prédire la classe d'un 
# ensemble d'image.
# Parametre : c'est un vecteur contenant deux 
# vecteurs. Le premier correspond aux images 
# sous forme de vecteur, le second correspond 
# aux classes des images.
# Renvoie : un vecteur de classe correspondant
# aux prediction des images.
def predict (dataset):
	train = pickle.load(open("trainModel.joblib", "rb"))
	result = train.predict(dataset)		# prediction avec le meme set que pour l'entrainement
	
	return result
