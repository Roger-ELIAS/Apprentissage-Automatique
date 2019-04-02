from sklearn.naive_bayes import GaussianNB
import crossValidate
import random
import learn
import linear
import chi2
import neuralNetwork
import pickle
#On va récupérer les prédicts depuis les 4 sources différentes : chi2, réseau
#de neurones, un SVC, et Naive Bayes. 

def getMaxArray(scoreArray) : 
    maxArray = []
    maxValue = scoreArray[0]
    for i in range(0,len(scoreArray)) : 
        if maxValue == scoreArray[i] :
            maxArray.append(i)
        elif maxValue < scoreArray[i] : 
            maxValue = scoreArray[i]
            maxArray = []
            maxArray.append(i)
    return maxArray

def Bagging(testData):
    #testData est une array d'histogrammes de couleur
    #accéder à gnbClassifier

    baggingArray = []
    scoreArray = []
    testDataSize = len(testData)

    dataset = pickle.load(open("dataset.joblib", "rb"))

    arrayGNB = learn.predict(testData)
    arrayChi2 = chi2.predict(testData)
    arrayNW = neuralNetwork.predict(testData)
    arraySVC = linear.predict(testData)

    classifierArray = [arrayGNB, arrayNW, arraySVC, arrayChi2] 
    scoreArray = []
	
    scoreArray.append(crossValidate.crossNW(dataset).mean())
    scoreArray.append(crossValidate.crossNB(dataset).mean())
    scoreArray.append(crossValidate.crossLinear(dataset).mean())
    scoreArray.append(crossValidate.crossChi2(dataset).mean())

    arrayMaxScores = getMaxArray(scoreArray)

    for i in range(0, testDataSize):
        count = 0
        if arrayGNB[i] == 1 :
            count = count + 1
        if arrayChi2[i] == 1 : 
            count = count + 1
        if arrayNW[i] == 1 : 
            count = count + 1
        if arraySVC[i] == 1 : 
            count = count + 1
        if count >= 3 : 
            baggingArray.append(1)
        elif count == 2 :
            if len(arrayMaxScores) == 1:
                baggingArray.append(classifierArray[arrayMaxScores[0]][i])
            else:
                countSea = 0
                countNotSea = 0
                for y in range(0,len(arrayMaxScores)) : 
                    if classifierArray[arrayMaxScores[y]][i] == 1 :
                        ++countSea
                    else : 
                        ++countNotSea
                if countSea>countNotSea :
                    baggingArray.append(1)
                elif countSea == countNotSea :
                    rand = random.Random()
                    if rand <= 0.5 : 
                        baggingArray.append(1)
                    else :
                        baggingArray.append(-1)
        else :
            baggingArray.append(-1)
    return baggingArray
 
