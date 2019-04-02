from PIL import Image
import os

matrix = []
vector = []

#Resize l'image pour avoir le meme nombre de pixel sur l'histogramme de couleur 
def resizeImage(image) :
    baseImage = image.resize((200, 200))
    return baseImage

#Rotate une image de deg passé en paramètre et la renvoie
def getImgageRotated(baseImage, deg) :
    newImage = baseImage.rotate(deg, Image.BICUBIC, True)
    return newImage

#Ajoute l'histogramme et la classe passés en paramètres à la matrix et au vector
def append(histo, classe) :
        matrix.append(histo)
        vector.append(classe)

#Récupère une image rotationnée par le biais de la fonction getImgageRotated et la stocke dans matric et vector grâce à append
def rotateSingleImage(imageResize, rotationDegre, classe) :
	imageRotate = getImgageRotated(imageResize, rotationDegre)
	histo = imageRotate.histogram()
	append(histo, classe)

#Rotate et stocke toutes les images passées en paramètres
def rotateImages(images, deg, classe) :
    for image in images :
        rotateSingleImage(image, deg, classe)

#Augmente le nombre de data en entrée en rotationnant et en flippant sur les images du dossier en paramètre
def augment(folder, classe):
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

#Récupère la matrice et le vector des images de Mer et d'Ailleurs préalablements augmentées
def generateMatrixTrain(foldername) :
    augment(foldername + "/Mer/", 1)
    augment(foldername + "/Ailleurs/", -1)
    return [matrix,vector]

#Génère la matrice des images utilisées pour tester
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
