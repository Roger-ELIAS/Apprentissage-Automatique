import PIL
from PIL import Image
import os


def getHistogram(fileName) :
    baseImage = Image.open(fileName)
    return baseImage.histogram()

def generateMatrix() :
    matrix = []
    vector = []
    files = os.listdir("/Users/romaincolonnadistria/Documents/Apprentissage-Automatique-/Data/Mer")
    for fileName in files :
        histo = getHistogram("Data/Mer/"+fileName)
        matrix.append(histo)
        vector.append(1)

    files = os.listdir("Data/Ailleurs")
    for fileName in files:
        histo = getHistogram("Data/Ailleurs/" + fileName)
        matrix.append(histo)
        vector.append(-1)

    return [matrix,vector]
