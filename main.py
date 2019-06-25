import numpy
#import chi2
import os
import generateMatrix
import naiveBayes
import sys
import AABagging
import pickle
import linear
import json
import neuralNetwork

def generateResultJSON() :
    files = os.listdir(folder)
    i = 0
    dictResult = {}

    for fileName in files:
        dictResult[fileName] = result[i]
        i += 1

    with open('result.json', 'w') as outfile:
        json.dump(dictResult, outfile)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage : pyhton3 main.py <--action> <folder>")
        sys.exit(1)
    folder = sys.argv[2]

    if sys.argv[1] == "--fit":
        final = generateMatrix.generateMatrixTrain(folder)
        pickle.dump(final, open("dataset.joblib","wb"))
        naiveBayes.train(final)
        #chi2.train(final)
        linear.train(final)
        neuralNetwork.train(final)
        print("Succesful")
    elif sys.argv[1] == "--predict":
        test = generateMatrix.generateMatrixTest(folder)
        result = AABagging.Bagging(test)

        generateResultJSON()