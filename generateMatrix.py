from PIL import Image
import os
import resizeImage


def getHistogram(fileName) :
    baseImage = Image.open(fileName)
    return baseImage.histogram()

def generateMatrixTrain(foldername) :
    matrix = []
    vector = []

    files = os.listdir(foldername +"/Mer")

    for fileName in files :
        baseImage = Image.open(foldername +"/Mer"+fileName)
        imageResize = resizeImage.resizeImage(baseImage)
        histo = getHistogram(imageResize)
        matrix.append(histo)
        vector.append(1)

    files = os.listdir(foldername +"/Ailleurs")
    for fileName in files:
        baseImage = Image.open(foldername +"/Ailleurs"+fileName)
        imageResize = resizeImage.resizeImage(baseImage)
        histo = getHistogram(imageResize)
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

generateMatrixTrain("Data")