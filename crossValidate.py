from sklearn.model_selection import cross_val_score
from sklearn import svm

# Fonction de cross validation.
# Parametre : dataset est un vecteur contenant 
# deux vecteurs. Le premier est un vecteur d'images
# et le second est un vecteur contenant les classes
# de chaque images du premier vecteur.
def crossLinear(dataset):
    X = dataset[0]     # vecteur d'image
    y = dataset[1]     # vecteur de classes
    
    clf = svm.SVC(kernel='linear', C=1)		# creation et entrainement de l'estimateur avec les donnees test
    scores = cross_val_score(clf, X, y, cv=5)	# cross validation avec les donnees test
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    return scores    


def crossChi2(dataset):
    X = dataset[0]     # vecteur d'image
    y = dataset[1]     # vecteur de classes

    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)   # Separation des donnees pour test et train

    # cross validation en utilisant
    clf = svm.SVC(kernel="chi2_kernel", C=1)
    scores = cross_val_score(clf, X, y, cv=5)  # cross validation avec les donnees test
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    return scores

def crossNW(dataset): 
    X = dataset[0]
    y = dataset[1]

    mlp = MLPClassifier(hidden_layer_sizes=(15, 15), max_iter=4000)

    scalar = StandardScaler()
    X = scalar.fit_transform(X)

    scores = cross_val_score(mlp, X, y, cv=5)
    
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    return scores

def crossNB(dataset):
    X = dataset[0]
    y = dataset[1]

    clf = GaussianNB()

    scores = cross_val_score(clf, X, y , cv=5)

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    return scores
    

