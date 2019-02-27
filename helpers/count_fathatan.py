# -*- coding: utf-8 -*-

import sys

from os import listdir
from os.path import isfile, join

def count_fathatan(FOLDER_PATH):
  files = [file for file in listdir(FOLDER_PATH) if isfile(join(FOLDER_PATH, file))]

  before = 0
  after = 0
  for file in files:
    with open(join(FOLDER_PATH, file), 'r') as f:
      lines = f.readlines() 

      pre = ''
      for line in lines:
        for ch in line:
          if ch == 'ا' and pre == 'ً':
            before += 1
          elif ch == 'ً' and pre == 'ا':
            after += 1
          pre = ch

  return before, after

if __name__ == '__main__':
  if len(sys.argv) != 2:
  	sys.exit('usage: python %s [FOLDER_PATH]' % sys.argv[0])

  FOLDER_PATH = sys.argv[1]

  before, after = count_fathatan(FOLDER_PATH)
  
  print('Before Alif:', before)
  print('After Alif:', after)
