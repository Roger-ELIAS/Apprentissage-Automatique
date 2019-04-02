import generateMatrix
import crossValidate
import learn
import numpy
import sys
import AABagging
import pickle
import linear
import chi2
import neuralNetwork


def diff(a, b):
    target = numpy.array(a)
    result = numpy.array(b)
    error = numpy.mean(target != result)
    return round(100 - error * 100, 10)


#if __name__ == '__main__':
#    final = generateMatrix.generateMatrixTrain("DATA_TRAIN_FOLDER")
    
#    learn.predict(final)
    
#    validateResult = crossValidate.crossLinear(final)
#    validateResult = crossValidate.crossChi2(final)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage : pyhton3 main.py <--action> <folder>")
        sys.exit(1)
    folder = sys.argv[2]

    if sys.argv[1] == "--fit":
        final = generateMatrix.generateMatrixTrain(folder)
        pickle.dump(final, open("dataset.joblib","wb"))
        learn.train(final)
        chi2.train(final)
        linear.train(final)
        neuralNetwork.train(final)
    elif sys.argv[1] == "--predict":
        test = generateMatrix.generateMatrixTest(folder)
        result = AABagging.Bagging(test)
        print(result)
        arrayTest = [-1,1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,1,1,1]
        print(diff(result,arrayTest))        
    #print("Taux de réussite : ", diff(result, final[1]))
