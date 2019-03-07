import os, sys
import pickle as pkl
from os import listdir
from os.path import isfile, join

def load_constants():
  CONSTANTS_PATH = 'constants'

  with open(CONSTANTS_PATH + '/ARABIC_LETTERS_LIST.pickle', 'rb') as file:
    ARABIC_LETTERS_LIST = pkl.load(file)

  with open(CONSTANTS_PATH + '/CLASSES_LIST.pickle', 'rb') as file:
    CLASSES_LIST = pkl.load(file)

  return ARABIC_LETTERS_LIST, CLASSES_LIST

def getDiacPerc(line):
	chars = 0
	diacs = 0
	for idx in range(len(line)):
		if line[idx] in ARABIC_LETTERS_LIST:
			chars += 1
			if idx + 1 < len(line) and line[idx + 1] in CLASSES_LIST:
				diacs += 1
	if chars == 0:
		return 0
	return diacs / chars

# Load constatns
ARABIC_LETTERS_LIST, CLASSES_LIST = load_constants()

FOLDER_PATH = '/home/kudo/Desktop/repositories/shakkelha/comparisons/shakkala/books'

files = [file for file in listdir(FOLDER_PATH) if isfile(join(FOLDER_PATH, file))]

sum_cnt = 0

for file in files:
	if(file[-4:] != '.txt'): continue
	print("\nFile being processed: " + file)
	with open(join(FOLDER_PATH, file), 'r') as f_processed:
		lines_processed = f_processed.readlines()

		new_lines_processed = list()
		cnt = 0

		for line_processed in lines_processed:
			if getDiacPerc(line_processed) >= 0.8:
				cnt += len(line_processed.split(' '))
				new_lines_processed.append(line_processed.strip())

		sum_cnt += cnt
		with open(join(FOLDER_PATH, '80-' + file), 'w') as ff:
			ff.write('\n'.join(new_lines_processed))

		print('Original number of lines:', len(lines_processed))
		print('Picked number of lines:', len(new_lines_processed))
		print('Number of words:', cnt)

print('Total number of words:', sum_cnt)