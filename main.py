import generateMatrix
import learn 
import numpy

def diff(a, b): 
    target = numpy.array(a)
    result = numpy.array(b)
    error = numpy.mean(target != result)
    return round(100 - error * 100, 1)


if __name__ == '__main__':
    final = generateMatrix.generateMatrixTrain("Data")

    result = learn.training(final)

    print("Taux de réussite : ", diff(result, final[1]))

