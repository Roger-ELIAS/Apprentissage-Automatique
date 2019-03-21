import numpy
from sklearn.metrics.pairwise import chi2_kernel
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn import svm


def diff(a, b):
    target = numpy.array(a)
    result = numpy.array(b)
    error = numpy.mean(target != result)
    return round(100 - error * 100, 1)


def training (dataSet):

#    from sklearn.naive_bayes import BernoulliNB
#    algo = GaussianNB()
#    from sklearn.naive_bayes import GaussianNB
#    algo = BernoulliNB()
#    from sklearn.naive_bayes import MultinomialNB 
#    algo = MultinomialNB() meilleur

    from sklearn.naive_bayes import ComplementNB
    algo = ComplementNB()


    X = dataSet[0]
    y = dataSet[1]  # vecteur de class (2 valeurs)

    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)   # Separation des donnees pour test et train

    test = svm.SVC(kernel="linear", C=1)
    scores = cross_val_score(test, X, y, cv=5)                        # cross validation avec les donnees test
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))



    print("////////////////////////////////////////////////////////////////////////")

    # cross validation en utilisant
    test2 = svm.SVC(kernel=chi2_kernel, C=1)
    scores2 = cross_val_score(test2, X, y, cv=5)  # cross validation avec les donnees test
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores2.mean(), scores2.std() * 2))
