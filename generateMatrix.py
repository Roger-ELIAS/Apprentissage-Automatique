import PIL
from PIL import Image
import os

matrix = []
vector = []

def resizeImage(image) :
    baseImage = image.resize((200, 200))
    return baseImage

def rotateImage(baseImage, deg) :
    newImage = baseImage.rotate(deg, Image.BICUBIC, True)
    return newImage

def append(histo, classe) :
        matrix.append(histo)
        vector.append(classe)

def rotateSingleImage(imageResize, rotationDegre, classe) :
	imageRotate = rotateImage(imageResize, rotationDegre)
	histo = imageRotate.histogram()
	append(histo, classe)

def rotateImages(images, deg, classe) :
    for image in images :
        rotateSingleImage(image, deg, classe)


def rotate(folder, classe):
        files = os.listdir(folder)

        for fileName in files:
                baseImage = Image.open(folder + fileName)
                images = []

                imageResize = resizeImage(baseImage)
                imageFlipLR = imageResize.transpose(Image.FLIP_LEFT_RIGHT)
                imageFlipTB = imageResize.transpose(Image.FLIP_TOP_BOTTOM)

                images.append(imageResize)
                images.append(imageFlipLR)
                images.append(imageFlipTB)

                histo = imageResize.histogram()
                append(histo, classe)

                histo = imageFlipLR.histogram()
                append(histo, classe)

                histo = imageFlipTB.histogram()
                append(histo, classe)

                for rotationPhase in range(0,3):
                        for deg in range(1,3) :
                                rotateImages(images, rotationPhase * 90 + deg, classe)
                                rotateImages(images, rotationPhase * 90 - deg, classe)

                        rotateImages(images, (rotationPhase + 1) * 90, classe)
                            
                for deg in range(1,3) :
                        rotateImages(images, 270 + deg, classe)
                        rotateImages(images, 270 - deg, classe)

def generateMatrixTrain(foldername) :
    rotate(foldername + "/Mer/", 1)
    rotate(foldername + "/Ailleurs/", -1)
    return [matrix,vector]


def generateMatrixTest(folder) :
    matrix = []
	
    file = folder + "/"
    files = os.listdir(file)

    for fileName in files :
        baseImage = Image.open(file+fileName)
        imageResize = resizeImage(baseImage)
        histo =  imageResize.histogram()
        matrix.append(histo)

    return matrix
