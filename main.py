import glob
import cv2
from PIL import Image, ImageEnhance
import numpy as np

## Main code
def main(args):

	# Reading mask
	mask = Image.open('./mask/mask_single_channel.png')

	# Divide by max pixel brightness
	maskArray = np.asarray(mask)//255

	# Display shape
	print('Mask shape: ' + str(maskArray.shape))


	# Reading image
	originalImage = Image.open('./input/RealData_309_tm_25C_top_need_35C/0000.tif')

	# Increasing contrast
	cEnhancer = ImageEnhance.Contrast(originalImage)

	fContrast = 1.5 # factor to increase contrast
	image = cEnhancer.enhance(fContrast)

	# Increasing contrast
	fEnhancer = ImageEnhance.Sharpness(image)

	fSharpness = 2 # factor to increase sharpness
	image = fEnhancer.enhance(fSharpness)

	# Convert to numpy array and ta
	imArray = np.transpose(np.asarray(image), (2, 0, 1))

	print(imArray.shape)

	output = []
	for channel in imArray:

		output.append(channel*maskArray)

	output = np.transpose(np.asarray(output), (1, 2, 0))

	outIm = Image.fromarray(output, 'RGB')
	outIm.save('./output/0000.tif')

	originalImage.show()
	outIm.show()

	print('\nEnd of main.py.')

if __name__ == '__main__':

	args = None

	main(args)