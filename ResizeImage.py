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

def rotateImage():

    files = os.listdir("Data/Mer")

    for fileName in files :
        baseImage = Image.open("Data/Mer/" + fileName)
        test = fileName.split(".")

        for rotationPhase in range(0, 2) :
            imgNb = 0
            for deg in range(1, 4) :
                newImage = baseImage.rotate(rotationPhase * 90 + deg, Image.BICUBIC, True)
                newfile = test[0] + str(imgNb) + "." + test[1]
                newImage.save("Data/Mer/" + newfile)
                imgNb += 1

            newImage = baseImage.rotate((rotationPhase + 1) * 90, Image.BICUBIC, True)
            newfile = test[0] + str(imgNb) + "." + test[1]
            newImage.save("Data/Mer/" + newfile)

        for deg in range(1, 4):
            newImage = baseImage.rotate(270 + deg, Image.BICUBIC, True)
            newfile = test[0] + str(imgNb) + "." + test[1]
            newImage.save("Data/Mer/" + newfile)
            imgNb += 1

    files = os.listdir("Data/Ailleurs")

    for fileName in files:
        baseImage = Image.open("Data/Ailleurs/" + fileName)
        test = fileName.split(".")
        imgNb = 0

        for rotationPhase in range(0, 3):
            for deg in range(1, 4):
                newImage = baseImage.rotate(rotationPhase * 90 + deg, Image.BICUBIC, True)
                newfile = test[0] + str(imgNb) + "." + test[1]
                newImage.save("Data/Ailleurs/" + newfile)
                imgNb += 1

            newImage = baseImage.rotate((rotationPhase + 1) * 90, Image.BICUBIC, True)
            newfile = test[0] + str(imgNb) + "." + test[1]
            newImage.save("Data/Ailleurs/" + newfile)
            imgNb += 1

        for deg in range(1, 4):
            newImage = baseImage.rotate(270 + deg, Image.BICUBIC, True)
            newfile = test[0] + str(imgNb) + "." + test[1]
            newImage.save("Data/Ailleurs/" + newfile)
            imgNb += 1

#rotateImage()