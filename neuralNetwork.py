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


def predict(dataset):
    train = pickle.load(open("trainModelNeurones.joblib", "rb"))
    result = train.predict(dataset)

    return result