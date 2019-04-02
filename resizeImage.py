import PIL
from PIL import Image
import os

def resizeImage(image) :
    baseImage = image.resize((200, 200))
    return baseImage

def rotateSingleImage(baseImage, deg) :
    newImage = baseImage.rotate(deg, Image.BICUBIC, True)
    return newImage
