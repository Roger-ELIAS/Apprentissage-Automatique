from PIL import Image
import os
import resizeImage


def getHistogram(fileName) :
	return fileName.histogram()

def generateMatrixTrain(foldername) :
	matrix = []
	vector = []

	files = os.listdir(foldername +"/Mer/")

	for fileName in files:
		baseImage = Image.open(foldername +"/Mer/"+fileName)
		imageResize = resizeImage.resizeImage(baseImage)
		histo = getHistogram(imageResize)
		matrix.append(histo)
		vector.append(1)
		
		for rotationPhase in range(0,3):
			for deg in range(1,3) :
				imageRotate = resizeImage.rotateSingleImage(imageResize, rotationPhase * 90 + deg)
				histo = getHistogram(imageRotate)
				matrix.append(histo)
				vector.append(1)
				


				imageRotate = resizeImage.rotateSingleImage(imageResize, rotationPhase * 90 - deg)
				histo = getHistogram(imageRotate)
				matrix.append(histo)
				vector.append(1)
				


			imageRotate = resizeImage.rotateSingleImage(imageResize, (rotationPhase + 1) * 90)
			histo = getHistogram(imageRotate)
			matrix.append(histo)
			vector.append(1)
			

			
		for deg in range(1,3) :
			imageRotate = resizeImage.rotateSingleImage(imageResize, 270 + deg)
			histo = getHistogram(imageRotate)
			matrix.append(histo)
			vector.append(1)

			imageRotate = resizeImage.rotateSingleImage(imageResize, 270 - deg)
			histo = getHistogram(imageRotate)
			matrix.append(histo)
			vector.append(1)
			

	files = os.listdir(foldername +"/Ailleurs/")
	for fileName in files:
		baseImage = Image.open(foldername +"/Ailleurs/"+fileName)
		imageResize = resizeImage.resizeImage(baseImage)
		histo = getHistogram(imageResize)
		matrix.append(histo)
		vector.append(-1)
		
		for rotationPhase in range(0,3) :
			for deg in range(1,3) :
				imageRotate = resizeImage.rotateSingleImage(imageResize, rotationPhase * 90 + deg)
				histo = getHistogram(imageRotate)
				matrix.append(histo)
				vector.append(-1)

				imageRotate = resizeImage.rotateSingleImage(imageResize, rotationPhase * 90 - deg)
				histo = getHistogram(imageRotate)
				matrix.append(histo)
				vector.append(-1)


			imageRotate = resizeImage.rotateSingleImage(imageResize, (rotationPhase + 1) * 90)
			histo = getHistogram(imageRotate)
			matrix.append(histo)
			vector.append(-1)

		for deg in range(1,3) :
			imageRotate = resizeImage.rotateSingleImage(imageResize, 270 + deg)
			histo = getHistogram(imageRotate)
			matrix.append(histo)
			vector.append(-1)

			imageRotate = resizeImage.rotateSingleImage(imageResize, 270 - deg)
			histo = getHistogram(imageRotate)
			matrix.append(histo)
			vector.append(-1)

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

#generateMatrixTrain("Data")