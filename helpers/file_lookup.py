import sys

from os import listdir
from os.path import isfile, join

def file_lookup(FOLDER_PATH, LINE_TO_SEARCH):
  files = [file for file in listdir(FOLDER_PATH) if isfile(join(FOLDER_PATH, file))]

  found_files = []
  for file in files:
    if LINE_TO_SEARCH in open(join(FOLDER_PATH, file)).read():
      found_files.append(file)

  return found_files

if __name__ == '__main__':
  if len(sys.argv) != 3:
  	sys.exit('usage: python %s [FOLDER_PATH] [LINE_TO_SEARCH]' % sys.argv[0])

  FOLDER_PATH = sys.argv[1]
  LINE_TO_SEARCH = sys.argv[2]

  found_files = file_lookup(FOLDER_PATH, LINE_TO_SEARCH)

  for file in found_files:
    print('Found in:', file)
