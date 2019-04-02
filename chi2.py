from sklearn import svm, metrics
from sklearn.metrics.pairwise import chi2_kernel
#from joblib import dump, load
import pickle
import numpy
#def diff(a, b): 
#    target = numpy.array(a)
#    result = numpy.array(b)
#    error = numpy.mean(target != result)
#    return round(100 - error * 100, 10) 



def train(dataset): 
    test = svm.SVC(kernel=chi2_kernel).fit(dataset[0],dataset[1])
    pickle.dump(test, open("trainModelChi2.joblib", "wb"))

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
