# -*- coding: utf-8 -*-

import os
import argparse
import pickle as pkl

def remove_diacritics(file_path):
  def _remove_diacritics(content):
    return content.translate(str.maketrans('', '', ''.join(DIACRITICS_LIST)))

  CONSTANTS_PATH = 'constants'

  with open(CONSTANTS_PATH + '/DIACRITICS_LIST.pickle', 'rb') as file:
    DIACRITICS_LIST = pkl.load(file)

  with open(file_path, 'r') as file:
    lines = file.readlines()

  new_lines = []
  for line in lines:
    new_lines.append(_remove_diacritics(line).strip())

  file_path = file_path.split(os.sep)
  file_path[-1] = 'cleaned_' + file_path[-1]
  file_path = os.sep.join(file_path)

  print(file_path)

  with open(file_path, 'w') as file:
    file.write('\n'.join(new_lines))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Removes diacritics from file')
  parser.add_argument('-in', '--file-path', help='File path to remove diacritics from it', required=True)
  args = parser.parse_args()

  remove_diacritics(args.file_path)
