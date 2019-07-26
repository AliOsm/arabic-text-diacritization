# -*- coding: utf-8 -*-

import argparse
import pickle as pkl

CONSTANTS_PATH = 'constants'

def count_each_dic(FILE_PATH):
  each = dict()

  with open(CONSTANTS_PATH + '/CLASSES_LIST.pickle', 'rb') as file:
    CLASSES_LIST = pkl.load(file)
  
  with open(CONSTANTS_PATH + '/ARABIC_LETTERS_LIST.pickle', 'rb') as file:
    ARABIC_LETTERS_LIST = pkl.load(file)

  with open(CONSTANTS_PATH + '/DIACRITICS_LIST.pickle', 'rb') as file:
    DIACRITICS_LIST = pkl.load(file)

  with open(FILE_PATH, 'r') as file:
    lines = file.readlines()
  for line in lines:
    for idx, char in enumerate(line):
      if char in DIACRITICS_LIST:
          continue
      char_diac = ''
      if idx + 1 < len(line) and line[idx + 1] in DIACRITICS_LIST:
          char_diac = line[idx + 1]
          if idx + 2 < len(line) and line[idx + 2] in DIACRITICS_LIST and char_diac + line[idx + 2] in CLASSES_LIST:
              char_diac += line[idx + 2]
          elif idx + 2 < len(line) and line[idx + 2] in DIACRITICS_LIST and line[idx + 2] + char_diac in CLASSES_LIST:
              char_diac = line[idx + 2] + char_diac
      try:
        each[char_diac] += 1
      except:
        each[char_diac] = 1
          
  return each

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Count each diacritic frequency')
  parser.add_argument('-in', '--file-path', help='File path to count from', required=True)
  args = parser.parse_args()

  each = count_each_dic(args.file_path)

  name = {'' : 'No Diacritic       ',
          'َ' : 'Fatha              ',
          'ً' : 'Fathatah           ',
          'ُ' : 'Damma              ',
          'ٌ' : 'Dammatan           ',
          'ِ' : 'Kasra              ',
          'ٍ' : 'Kasratan           ',
          'ْ' : 'Sukun              ',
          'ّ' : 'Shaddah            ',
          'َّ' : 'Shaddah + Fatha    ',
          'ًّ' : 'Shaddah + Fathatah ',
          'ُّ' : 'Shaddah + Damma    ',
          'ٌّ' : 'Shaddah + Dammatan ',
          'ِّ' : 'Shaddah + Kasra    ',
          'ٍّ' : 'Shaddah + Kasratan '}

  for key in name:
    print(name[key] + ':', each[key])