from sklearn.model_selection import cross_val_score
from sklearn import svm

# Fonction de cross validation.
# Parametre : dataset est un vecteur contenant 
# deux vecteurs. Le premier est un vecteur d'images
# et le second est un vecteur contenant les classes
# de chaque images du premier vecteur.
def cross(dataset):
    X = dataset[0]     # vecteur d'image
    y = dataset[1]     # vecteur de classes
    
    clf = svm.SVC(kernel='linear', C=1)		# creation et entrainement de l'estimateur avec les donnees test
    scores = cross_val_score(clf, X, y, cv=20)	# cross validation avec les donnees test
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
