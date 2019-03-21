from sklearn import datasets, linear_model
from sklearn.model_selection import cross_validate
from sklearn.metrics.scorer import make_scorer
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn import svm

def cross(dataset):
    X = dataset[0]
    y = dataset[1]
    
    clf = svm.SVC(kernel='linear', C=1)		# creation et entrainement de l'estimateur avec les donnees test
    scores = cross_val_score(clf, X, y, cv=20)	# cross validation avec les donnees test
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
