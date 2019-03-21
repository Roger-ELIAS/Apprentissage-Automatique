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
        baseImage = Image.open("Data/Mer/"+fileName)
        nb = 36
        name = fileName.split(".")
        while nb < 360:
            newImage = baseImage.rotate(nb,Image.BICUBIC, True)
            newfile = name[0] + str(nb) + "." + name[1]
            nb = nb+36
            newImage.save("Data/Mer/" + newfile)

    files = os.listdir("Data/Ailleurs")

    for fileName in files:
        baseImage = Image.open("Data/Ailleurs/" + fileName)
        nb = 36
        test = fileName.split(".")
        while nb < 360:
            newImage = baseImage.rotate(nb, Image.BICUBIC, True)
            newfile = test[0] + str(nb) + "." + test[1]
            nb = nb + 36
            newImage.save("Data/Ailleurs/" + newfile)

rotateImage()