# -*- coding: utf-8 -*-

import os
import re
import argparse

def fix_fathatan(file_path):
  with open(file_path, 'r') as file:
    lines = file.readlines()

  new_lines = []
  for line in lines:
    new_lines.append(re.sub(r'اً', 'ًا', line))

  file_path = file_path.split(os.sep)
  file_path[-1] = 'fixed_' + file_path[-1]
  file_path = os.sep.join(file_path)

  with open(file_path, 'w') as file:
    file.write(''.join(new_lines))

  print(file_path)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Changes after-Alif fathatan to before-Alit fathatan')
  parser.add_argument('-in', '--file-path', help='File path to fix it', required=True)
  args = parser.parse_args()

  fix_fathatan(args.file_path)
