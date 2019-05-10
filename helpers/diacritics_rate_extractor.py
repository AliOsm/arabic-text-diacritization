# -*- coding: utf-8 -*-

import os
import argparse
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

def get_diacritics_percentage(line):
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

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Keeps lines with p%% diacritics to Arabic characters rate or more')
  parser.add_argument('-in', '--folder-path', help='File path to fix it', required=True)
  parser.add_argument('-p', help='Diacritization percentage', required=True, type=float)
  args = parser.parse_args()

  ARABIC_LETTERS_LIST, CLASSES_LIST = load_constants()

  files = [file for file in listdir(args.folder_path) if isfile(join(args.folder_path, file))]

  sum_cnt = 0

  for file in files:
    print('File being processed: ' + file)
    with open(join(args.folder_path, file), 'r') as f_processed:
      lines_processed = f_processed.readlines()

      new_lines_processed = list()
      cnt = 0

      for line_processed in lines_processed:
        if get_diacritics_percentage(line_processed) >= args.p:
          cnt += len(line_processed.split(' '))
          new_lines_processed.append(line_processed.strip())

      sum_cnt += cnt
      with open(join(args.folder_path, '80-' + file), 'w') as ff:
        ff.write('\n'.join(new_lines_processed))

      print('Original number of lines:', len(lines_processed))
      print('Picked number of lines:', len(new_lines_processed))
      print('Number of words:', cnt)

  print('Total number of words:', sum_cnt)
