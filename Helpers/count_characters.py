import sys
import pickle as pkl

# Constants
CONSTANTS_PATH = 'Constants'

with open(CONSTANTS_PATH + '/ARABIC_LETTERS_LIST.pickle', 'rb') as file:
  ARABIC_LETTERS_LIST = pkl.load(file)

with open(CONSTANTS_PATH + '/DIACRITICS_LIST.pickle', 'rb') as file:
  DIACRITICS_LIST = pkl.load(file)

if len(sys.argv) != 2:
	sys.exit('usage: python %s [FILE_PATH]' % sys.argv[0])

file_path = sys.argv[1]

with open(file_path, 'r') as file:
  lines = file.readlines()

arabic_chars = 0
diacratic_chars = 0
for line in lines:
	for ch in line:
		if ch in ARABIC_LETTERS_LIST:
			arabic_chars += 1
		elif ch in DIACRITICS_LIST:
			diacratic_chars += 1

print('Arabic characters count:', arabic_chars)
print('Diacritic characters count:', diacratic_chars)
