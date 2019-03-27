from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier


def cross(dataset):
    X = dataset[0]
    y = dataset[1]

    mlp = MLPClassifier(hidden_layer_sizes=(25, 25, 25), max_iter=500, solver="sgd")
    scores = cross_val_score(mlp, X, y, cv=20)  # cross validation avec les donnees test

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))