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


resizeImage()