# -*- coding: utf-8 -*-

import argparse

from os import listdir
from os.path import isfile, join

def file_lookup(folder_path, line):
  files = [file for file in listdir(folder_path) if isfile(join(folder_path, file))]

  found_files = []
  for file in files:
    if line in open(join(folder_path, file)).read():
      found_files.append(file)

  return found_files

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Search for line into folder files')
  parser.add_argument('-in', '--folder-path', help='Folder path to search in', required=True)
  parser.add_argument('-line', help='Line to search for', required=True)
  args = parser.parse_args()

  found_files = file_lookup(args.folder_path, args.line)

  for file in found_files:
    print('Found in:', file)
