import sys
import pickle as pkl

def count_characters(FILE_PATH):
  CONSTANTS_PATH = 'constants'

  with open(CONSTANTS_PATH + '/ARABIC_LETTERS_LIST.pickle', 'rb') as file:
    ARABIC_LETTERS_LIST = pkl.load(file)

  with open(CONSTANTS_PATH + '/DIACRITICS_LIST.pickle', 'rb') as file:
    DIACRITICS_LIST = pkl.load(file)

  with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

  arabic_characters = 0
  diacritic_characters = 0
  for line in lines:
    for ch in line:
      if ch in ARABIC_LETTERS_LIST:
        arabic_characters += 1
      elif ch in DIACRITICS_LIST:
        diacritic_characters += 1

  return arabic_characters, diacritic_characters

if __name__ == '__main__':
  if len(sys.argv) != 2:
  	sys.exit('usage: python %s [FILE_PATH]' % sys.argv[0])

  FILE_PATH = sys.argv[1]

  arabic_characters, diacritic_characters = count_characters(FILE_PATH)

  print('Arabic characters count:', arabic_characters)
  print('Diacritic characters count:', diacritic_characters)
