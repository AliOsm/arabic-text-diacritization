from os import listdir
from os.path import isfile, join
import sys

if len(sys.argv) != 3:
	sys.exit("usage: python %s [FOLDER_PATH] [LINE_TO_SEARCH]" %sys.argv[0])

folder_path = sys.argv[1]
files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
line = sys.argv[2]

for file in files:
	if line in open(folder_path+file).read():
		print("Found in:", file)