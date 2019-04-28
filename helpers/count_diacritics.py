# -*- coding: utf-8 -*-

import sys
import pickle as pkl

from os import listdir
from os.path import isfile, join

CONSTANTS_PATH = '../Constants'
each = dict()


def count_each_dic(FILE_PATH):
  
  with open(CONSTANTS_PATH + '/CLASSES_LIST.pickle', 'rb') as file:
    CLASSES_LIST = pkl.load(file)
  
  with open(CONSTANTS_PATH + '/ARABIC_LETTERS_LIST.pickle', 'rb') as file:
    ARABIC_LETTERS_LIST = pkl.load(file)

  with open(CONSTANTS_PATH + '/DIACRITICS_LIST.pickle', 'rb') as file:
    DIACRITICS_LIST = pkl.load(file)

  with open(FILE_PATH, 'r') as f:
    lines = f.readlines()

  previous_char = ''
  for line in lines:
    for index in range(len(line)):
      if line[index] in ARABIC_LETTERS_LIST:
        if index + 1 < len(line) and line[index + 1] in DIACRITICS_LIST:
          if index + 2 < len(line) and line[index + 1: index + 3] in CLASSES_LIST :
            try:
              each[line[index + 1: index + 2]] += 1
            except:
              each[line[index + 1: index + 2]] = 1
          elif (index + 2 < len(line) and line[index + 1: index + 3] not in CLASSES_LIST) or index + 2 >= len(line):
            try:
              each[line[index + 1]] += 1
            except:
              each[line[index + 1]] = 1
        if (index + 1 < len(line) and line[index + 1] not in DIACRITICS_LIST) or index + 1 >= len(line) :
          try:
            each['no_diac'] += 1
          except:
            each['no_diac'] = 1



if __name__ == '__main__':
  if len(sys.argv) != 2:
  	sys.exit('usage: python %s [FILE_PATH]' % sys.argv[0])

  FILE_PATH = sys.argv[1]

  count_each_dic(FILE_PATH)

  for key in each:
    print(key + ':', each[key])





