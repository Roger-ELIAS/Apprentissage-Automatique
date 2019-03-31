import PIL
from PIL import Image
import os

def resizeImage() :

    files = os.listdir("Data/MerBase")

    for fileName in files :
        baseImage = Image.open("Data/MerBase/"+fileName)
        print(fileName)
        baseImage = baseImage.resize((200, 200))
        baseImage.save("Data/Mer/" + fileName)

    files = os.listdir("Data/AilleursBase")

    for fileName in files :
        baseImage = Image.open("Data/AilleursBase/"+fileName)
        print(fileName)
        baseImage = baseImage.resize((200, 200))
        baseImage.save("Data/Ailleurs/" + fileName)

def rotateSingleImage(baseImage, imageName, pathToSave, deg, imageNb) :
    newImage = baseImage.rotate(deg, Image.BICUBIC, True)
    newfile = imageName[0] + str(imageNb) + "." + imageName[1]
    newImage.save(pathToSave + newfile)

def rotateImage():
    pathToSave = "Data/Mer/"
    files = os.listdir(pathToSave)

    for fileName in files :
        baseImage = Image.open(pathToSave + fileName)
        imageName = fileName.split(".")
        imageNb = 0

        for rotationPhase in range(0, 3) :
            for deg in range(1, 3) :
                rotateSingleImage(baseImage, imageName, pathToSave, rotationPhase * 90 + deg, imageNb)
                imageNb += 1

                rotateSingleImage(baseImage, imageName, pathToSave, rotationPhase * 90 - deg, imageNb)
                imageNb += 1

            rotateSingleImage(baseImage, imageName, pathToSave, (rotationPhase + 1) * 90, imageNb)
            imageNb += 1

        for deg in range(1, 3):
            rotateSingleImage(baseImage, imageName, pathToSave, 270 + deg, imageNb)
            imageNb += 1

            rotateSingleImage(baseImage, imageName, pathToSave, 270 - deg, imageNb)
            imageNb += 1

    pathToSave = "Data/Ailleurs/"
    files = os.listdir(pathToSave)

    for fileName in files:
        baseImage = Image.open(pathToSave + fileName)
        imageName = fileName.split(".")
        imageNb = 0

        for rotationPhase in range(0, 3):
            for deg in range(1, 3):
                rotateSingleImage(baseImage, imageName, pathToSave, rotationPhase * 90 + deg, imageNb)
                imageNb += 1

                rotateSingleImage(baseImage, imageName, pathToSave, rotationPhase * 90 - deg, imageNb)
                imageNb += 1

            rotateSingleImage(baseImage, imageName, pathToSave, (rotationPhase + 1) * 90, imageNb)
            imageNb += 1

        for deg in range(1, 3):
            rotateSingleImage(baseImage, imageName, pathToSave, 270 + deg, imageNb)
            imageNb += 1

            rotateSingleImage(baseImage, imageName, pathToSave, 270 - deg, imageNb)
            imageNb += 1