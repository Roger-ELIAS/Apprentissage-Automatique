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

def append(histo, classe):
        matrix.append(histo)
        vector.append(classe)

def getHistogram(fileName) :
	return fileName.histogram()

def rotateSingleImage(imageResize, rotationDegre, classe):
	imageRotate = rotateImage(imageResize, rotationDegre)
	histo = getHistogram(imageRotate)
	append(histo, classe)

def rotate(folder, classe):
        files = os.listdir(folder)

        for fileName in files:
                baseImage = Image.open(folder + fileName)
                imageResize = resizeImage(baseImage)
                imageFlipLR = imageResize.transpose(Image.FLIP_LEFT_RIGHT)
                imageFlipTB = imageResize.transpose(Image.FLIP_TOP_BOTTOM)
                histo = imageResize.histogram()
                append(histo, classe)
                histo = imageFlipLR.histogram()
                append(histo, classe)
                histo = imageFlipTB.histogram()
                append(histo, classe)

 
                for rotationPhase in range(0,3):
                        for deg in range(1,3) :
                                rotateSingleImage(imageResize, rotationPhase * 90 + deg, classe)
                                rotateSingleImage(imageFlipLR, rotationPhase * 90 + deg, classe)
                                rotateSingleImage(imageFlipTB, rotationPhase * 90 + deg, classe)
                                rotateSingleImage(imageResize, rotationPhase * 90 - deg, classe)
                                rotateSingleImage(imageFlipLR, rotationPhase * 90 - deg, classe)
                                rotateSingleImage(imageFlipTB, rotationPhase * 90 - deg, classe)

                        rotateSingleImage(imageResize, (rotationPhase + 1) * 90, classe)
                        rotateSingleImage(imageFlipLR, (rotationPhase + 1) * 90, classe)
                        rotateSingleImage(imageFlipTB, (rotationPhase + 1) * 90, classe)
                            
                for deg in range(1,3) :
                        rotateSingleImage(imageResize, 270 + deg, classe)
                        rotateSingleImage(imageFlipLR, 270 + deg, classe)
                        rotateSingleImage(imageFlipTB, 270 + deg, classe)
                        rotateSingleImage(imageResize, 270 - deg, classe)
                        rotateSingleImage(imageFlipLR, 270 - deg, classe)
                        rotateSingleImage(imageFlipTB, 270 - deg, classe)

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
		imageResize = resizeImage.resizeImage(baseImage)
		histo =  imageResize.histogram()
		matrix.append(histo)

	return matrix
