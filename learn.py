def training (dataSet):

#    from sklearn.naive_bayes import BernoulliNB
#    algo = GaussianNB()
#    from sklearn.naive_bayes import GaussianNB
#    algo = BernoulliNB()
#    from sklearn.naive_bayes import MultinomialNB 
#    algo = MultinomialNB() meilleur

    from sklearn.naive_bayes import ComplementNB
    algo = ComplementNB()
    train = algo.fit(dataSet[0], dataSet[1])
    predict = train.predict(dataSet[0])

#    print(predict)
    return predict

