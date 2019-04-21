# -*- coding: utf-8 -*-

import argparse

from os import listdir
from os.path import isfile, join

def count_fathatan(folder_path):
  files = [file for file in listdir(folder_path) if isfile(join(folder_path, file))]

  before = 0
  after = 0
  for file in files:
    with open(join(folder_path, file), 'r') as f:
      lines = f.readlines() 

      pre = ''
      for line in lines:
        for ch in line:
          if ch == u'ا' and pre == u'ً':
            before += 1
          elif ch == u'ً' and pre == u'ا':
            after += 1
          pre = ch

  return before, after

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Count fathatan before and after Alif')
  parser.add_argument('-in', '--folder-path', help='Folder path to count from all files inside it', required=True)
  args = parser.parse_args()

  before, after = count_fathatan(args.folder_path)
  
  print('Before Alif:', before)
  print('After Alif:', after)
