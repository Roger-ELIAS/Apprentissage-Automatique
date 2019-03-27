def training(dataSet):
    from sklearn.neural_network import MLPClassifier

    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=2000, solver="sgd")
    mlp.fit(dataSet[0], dataSet[1])
    predictions = mlp.predict(dataSet[0])

    return predictions