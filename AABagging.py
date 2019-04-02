from sklearn.naive_bayes import GaussianNB
import crossValidate
import random
#On va récupérer les prédicts depuis les 4 sources différentes : chi2, réseau
#de neurones, un SVC, et Naive Bayes. 

def getMaxArray(array) : 
    maxArray = []
    maxValue = array[0]
    for i in range(0,len(array)) : 
        if maxValue == array[i] :
            maxArray.append(i)
        elif maxValue < array[i] : 
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

    GNBClassifier = pickle.load(open("trainModelGNB.joblib", "rb")) 
    Chi2Classifier = pickle.load(open("trainModelChi2.joblib", "rb"))
    NWClassifier = pickle.load(open("trainModelNW.joblib", "rb"))
    SVCClassifier = pickle.load(open("trainModelSVC.joblib", "rb"))

    arrayGNB = GNBClassifier.predict(testData)
    arrayChi2 = Chi2Classifier.predict(testData)
    arrayNW = NWClassifier.predict(testData)
    arraySVC = SVCClassifier.predict(testData)

    classifierArray [arrayGNB, arrayChi2, arrayNW, arraySVC]

    scoreArray[0] = crossValidate.crossNW(dataset)
    scoreArray[1] = crossValidate.crossNB(dataset)
    scoreArray[2] = crossValidate.crossLinear(dataset)
    scoreArray[3] = crossValidate.crossChi2(dataset)

    arrayMaxScores = getMaxArray(scoreArray)

    for i in range(0, testDataSize):
        count = 0
        if arrayGNB[i] == 1 :
            ++count
        if arrayChi2[i] == 1 : 
            ++count
        if arrayNW[i] == 1 : 
            ++count
        if arraySVC[i] == 1 : 
            ++ count
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
 
