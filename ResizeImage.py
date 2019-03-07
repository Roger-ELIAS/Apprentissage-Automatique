import PIL
from PIL import Image
import os

files = os.listdir("Data/MerBase")

for fileName in files :
    baseImage = Image.open(fileName)
    baseImage = baseImage.resize((200,200))
    baseImage.save("Date/Mer/"+fileName)