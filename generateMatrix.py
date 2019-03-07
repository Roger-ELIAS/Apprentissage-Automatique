import PIL
from PIL import Image
import os


def getHistogram(fileName) :
    baseImage = Image.open(fileName)
    return baseImage.histogram()

def generateMatrixTrain(foldername) :
    matrix = []
    vector = []
    files = os.listdir(foldername +"/Mer")
    for fileName in files :
        histo = getHistogram(foldername +"/Mer/"+fileName)
        matrix.append(histo)
        vector.append(1)

    files = os.listdir(foldername +"/Ailleurs")
    for fileName in files:
        histo = getHistogram(foldername +"/Ailleurs/" + fileName)
        matrix.append(histo)
        vector.append(-1)

    return [matrix,vector]

def generateMatrixTest(folder) :
    matrix = []

    files = os.listdir(folder)


    for fileName in files :
        histo = getHistogram(folder+ "/" + fileName)
        matrix.append(histo)

    return matrix