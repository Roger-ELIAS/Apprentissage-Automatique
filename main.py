import generateMatrix
import crossValidate
import learn
import numpy

def diff(a, b):
    target = numpy.array(a)
    result = numpy.array(b)
    error = numpy.mean(target != result)
    return round(100 - error * 100, 10)


if __name__ == '__main__':
    final = generateMatrix.generateMatrixTrain("DATA_TRAIN_FOLDER")
    result = learn.training(final)

    print("Taux de réussite : ", diff(result, final[1]))

    crossValidate.cross(final)
    
