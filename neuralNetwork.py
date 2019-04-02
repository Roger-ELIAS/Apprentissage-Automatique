from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import pickle

def train(dataset):
    X = dataset[0]  # vecteur d'image
    y = dataset[1]  # vecteur de classes

    mlp = MLPClassifier(hidden_layer_sizes=(25), max_iter=15000)

    scalar = StandardScaler()
    X = scalar.fit_transform(X)

    mlp.fit(X,y)
    pickle.dump(mlp, open("trainModelNeurones.joblib", "wb"))


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
def predict(dataset):
    train = pickle.load(open("trainModelNeurones.joblib", "rb"))
    result = train.predict(dataset)  # prediction avec le meme set que pour l'entrainement

    return result