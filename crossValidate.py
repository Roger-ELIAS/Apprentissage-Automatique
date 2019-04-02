from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.metrics.pairwise import chi2_kernel

def crossLinear(dataset):
    X = dataset[0]     # vecteur d'image
    y = dataset[1]     # vecteur de classes
    
    clf = svm.SVC(kernel='linear', C=1)
    scores = cross_val_score(clf, X, y, cv=5)
    print("Linear : Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    return scores    


def crossChi2(dataset):
    X = dataset[0]     # vecteur d'image
    y = dataset[1]     # vecteur de classes

    clf = svm.SVC(kernel=chi2_kernel).fit(dataset[0],dataset[1])
    scores = cross_val_score(clf, X, y, cv=5)
    print("Chi2 : Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    return scores


def crossNW(dataset): 
    X = dataset[0]
    y = dataset[1]

    mlp = MLPClassifier(hidden_layer_sizes=(25), max_iter=15000)

    scalar = StandardScaler()
    X = scalar.fit_transform(X)

    scores = cross_val_score(mlp, X, y, cv=5)
    
    print("NeuralNetwork : Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    return scores

def crossNB(dataset):
    X = dataset[0]
    y = dataset[1]

    clf = GaussianNB()

    scores = cross_val_score(clf, X, y , cv=5)

    print("Naive Bayse : Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    return scores
    

