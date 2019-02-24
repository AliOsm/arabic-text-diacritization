import os
import sys
import pickle as pkl

def remove_diacritics(FILE_PATH):
  def _remove_diacritics(content):
    return content.translate(str.maketrans('', '', ''.join(DIACRITICS_LIST)))

  CONSTANTS_PATH = 'constants'

  with open(CONSTANTS_PATH + '/DIACRITICS_LIST.pickle', 'rb') as file:
    DIACRITICS_LIST = pkl.load(file)

  with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

  new_lines = []
  for line in lines:
    new_lines.append(_remove_diacritics(line).strip())

  FILE_PATH = FILE_PATH.split(os.sep)
  FILE_PATH[-1] = 'cleaned_' + FILE_PATH[-1]
  FILE_PATH = os.sep.join(FILE_PATH)

  print(FILE_PATH)

  with open(FILE_PATH, 'w') as file:
    file.write('\n'.join(new_lines))

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.exit('usage: python %s [FILE_PATH]' % sys.argv[0])

  FILE_PATH = sys.argv[1]

  remove_diacritics(FILE_PATH)
