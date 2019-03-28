from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy

def diff(a, b):
    target = numpy.array(a)
    result = numpy.array(b)
    error = numpy.mean(target != result)
    return round(100 - error * 100, 1)


def training(dataSet):
    from sklearn.neural_network import MLPClassifier

    #mlp = MLPClassifier(hidden_layer_sizes=(20, 15, 10, 5), max_iter=2000, solver="sgd")
    #mlp.fit(dataSet[0], dataSet[1])
    #predictions = mlp.predict(dataSet[0])

    X_train, X_test, y_train, y_test = train_test_split(dataSet[0], dataSet[1])

    mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=500, solver="sgd")

    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)


    mlp.fit(X_train, y_train)
    predicted = mlp.predict(X_test)

    print("Taux de réussite : ", diff(predicted, y_test))

    return predicted