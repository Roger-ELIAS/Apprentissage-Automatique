import numpy
import generateMatrix
from sklearn import svm, metrics
from sklearn.metrics.pairwise import chi2_kernel

dataSet = generateMatrix.generateMatrixTrain("Data")

test = svm.SVC(kernel=chi2_kernel).fit(dataSet[0],dataSet[1])

print(test.predict(dataSet[0]))

#test = svm.SVC(kernel=metrics.pairwise.chi2_kernel(dataSet[0],dataSet[1]))
#test.fit(dataSet[0],dataSet[1])