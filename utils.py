import os
import shutil
import glob
import cv2
from PIL import Image, ImageEnhance
import numpy as np

def process(framesDir, extension, fContrast, fSharpness):

	print('\nProcessing images.')

	# Check if frames directory exists
	if len(glob.glob(framesDir)) == 0:

		print('\nDid not find input directory.')

	else:

		# Reading mask
		mask = Image.open('./mask/mask_single_channel.png')

		# Divide by max pixel brightness
		maskArray = np.asarray(mask)//255

		# Display shape
		print('\nMask loaded. Mask shape: ' + str(maskArray.shape))

		# Read images
		imagesList = glob.glob(framesDir + '*.' + extension)

		# Create output directory
		if len(glob.glob('output/')) == 0:

			os.mkdir('output/')

		# Output directory
		outDir = framesDir.replace('input', 'output')

		# If it does exist, delete it
		if len(glob.glob(outDir)) != 0:

			shutil.rmtree(outDir)

		# Make directory
		os.mkdir(outDir)

		# Display how many images are detected
		print('\nDetected ' + str(len(imagesList)) + ' images.')

		# For each image:
		for i, imageSource in enumerate(imagesList):

			# Display progress
			if i%10 == 0:

				print(str(100*i/len(imagesList))[:4]+'%')

			# Destination of image
			imageDest = outDir + imageSource.split('\\')[-1]

			# Reading image
			originalImage = Image.open(imageSource)

			# Increasing contrast
			cEnhancer = ImageEnhance.Contrast(originalImage)
			image = cEnhancer.enhance(fContrast)

			# Increasing sharpness
			fEnhancer = ImageEnhance.Sharpness(image)
			image = fEnhancer.enhance(fSharpness)

			# Convert to numpy array and ta
			imArray = np.transpose(np.asarray(image), (2, 0, 1))

			# Storing output of image
			output = []

			# Multiply each channel by mask
			for channel in imArray:

				output.append(channel*maskArray)

			# Rearrage tensor
			output = np.transpose(np.asarray(output), (1, 2, 0))

			# Convert numpy array to image
			outIm = Image.fromarray(output, 'RGB')

			# Save the processed image
			outIm.save(imageDest)

			# originalImage.show()
			# outIm.show()

def making_mask():
	
	img = Image.open('./mask/mask.png')

	numpydata = np.asarray(img)

	trans = np.transpose(numpydata, (2, 0, 1))

	img = Image.fromarray(trans[0], 'L')
	img.save('./mask/mask_single_channel.png')
	img.show()

	print('\nExported Mask.')

if __name__ == '__main__':

	making_mask()