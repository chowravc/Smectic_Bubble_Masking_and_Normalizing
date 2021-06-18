import glob
import numpy as np
from PIL import Image

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