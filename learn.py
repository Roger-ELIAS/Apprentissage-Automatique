from sklearn.naive_bayes import ComplementNB

# fonction de prédiction d'image qui utilise
# un algo de Bayes. Cette fonction entraine un 
# algo et essaie de prédire la classe d'un 
# ensemble d'image.
# Parametre : c'est un vecteur contenant deux 
# vecteurs. Le premier correspond aux images 
# sous forme de vecteur, le second correspond 
# aux classes des images.
# Renvoie : un vecteur de classe correspondant
# aux prediction des images.
def training (dataSet):
    algo = ComplementNB()
    train = algo.fit(dataSet[0], dataSet[1])	# entrainement de l'algo avec le set d'image
    predict = train.predict(dataSet[0])		# prediction avec le meme set que pour l'entrainement

    return predict
