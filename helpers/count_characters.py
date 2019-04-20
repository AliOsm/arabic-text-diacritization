# -*- coding: utf-8 -*-

import argparse
import pickle as pkl

CONSTANTS_PATH = 'constants'

def count_characters(file_path, arabic_letters, diacritics):
  with open(file_path, 'r') as file:
    lines = file.readlines()

  arabic_letters_count = 0
  diacritics_count = 0
  for line in lines:
    for ch in line:
      if ch in ARABIC_LETTERS_LIST:
        arabic_letters_count += 1
      elif ch in DIACRITICS_LIST:
        diacritics_count += 1

  return arabic_letters_count, diacritics_count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Count Arabic letters and diacritics')
  parser.add_argument('-in', '--file-path', help='File path to count from', required=True)
  args = parser.parse_args()

  with open(CONSTANTS_PATH + '/ARABIC_LETTERS_LIST.pickle', 'rb') as file:
    ARABIC_LETTERS_LIST = pkl.load(file)

  with open(CONSTANTS_PATH + '/DIACRITICS_LIST.pickle', 'rb') as file:
    DIACRITICS_LIST = pkl.load(file)

  arabic_letters_count, diacritics_count = count_characters(args.file_path, ARABIC_LETTERS_LIST, DIACRITICS_LIST)

  print('Arabic characters count:', arabic_letters_count)
  print('Diacritic characters count:', diacritics_count)
