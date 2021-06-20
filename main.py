## Import useful packages
import argparse

## Import useful functions
from utils import *

## Main code
def main(args):

	# Adding mask and increasing contrast + sharpness
	if args.process:

		# Call process function
		process(args.fDir, args.ext, args.fC, args.fS)

	print('\nEnd of main.py.')

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Reading info for main.')

	# Arguments to convert video to frames
	parser.add_argument('--process', action='store_true', help='Flag to convert video to frames.')
	parser.add_argument('--fDir', action='store', nargs='?', type=str, default='input/example/', help='Source frames.')
	parser.add_argument('--ext', action='store', nargs='?', type=str, default='tif', help='Frames image extension.')
	parser.add_argument('--fC', action='store', nargs='?', type=float, default=1.5, help='Factor to increase contrast.')
	parser.add_argument('--fS', action='store', nargs='?', type=float, default=2.0, help='Factor to increase sharpness.')
	# Example:
	# python main.py --process --fDir /input/example/ --ext tif --fC 1.5 --fS 2.0

	# Parse arguments
	args = parser.parse_args()

	main(args)