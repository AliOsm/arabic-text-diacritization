# -*- coding: utf-8 -*-

import os
import io
import sys
import argparse

ARABIC_LETTERS = [
  u'ء', u'آ', u'أ', u'ؤ', u'إ',
  u'ئ', u'ا', u'ب', u'ة', u'ت',
  u'ث', u'ج', u'ح', u'خ', u'د',
  u'ذ', u'ر', u'ز', u'س', u'ش',
  u'ص', u'ض', u'ط', u'ظ', u'ع',
  u'غ', u'ـ', u'ف', u'ق', u'ك',
  u'ل', u'م', u'ن', u'ه', u'و',
  u'ى', u'ي', u'ً', u'ٌ', u'ٍ',
  u'َ', u'ُ', u'ِ', u'ّ', u'ْ',
]

SYMBOL_LETTERS = [
  '\'', '|', '>', '&', '<',
  '}', 'A', 'b', 'p', 't',
  'v', 'j', 'H', 'x', 'd',
  '*', 'r', 'z', 's', '$',
  'S', 'D', 'T', 'Z', 'E',
  'g', '_', 'f', 'q', 'k',
  'l', 'm', 'n', 'h', 'w',
  'Y', 'y', 'F', 'N', 'K',
  'a', 'u', 'i', '~', 'o'
]

def transliteration(file_path, domain, range):
  d = { u:v for u, v in zip(domain, range) }

  with io.open(file_path, 'r', encoding='utf8') as file:
    lines = file.readlines()

  new_lines = list()
  for line in lines:
    new_line = ''
    for ch in line.strip():
      if ch in d.keys():
        new_line += d[ch]
      else:
        new_line += ch
    new_lines.append(new_line)

  file_path = file_path.split(os.sep)
  file_path[-1] = 'transliterated_' + file_path[-1]
  file_path = os.sep.join(file_path)

  with io.open(file_path, 'w', encoding='utf8') as file:
    file.write('\n'.join(new_lines))

  print(file_path)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Convert from/to Buckwalter transliteration')
  parser.add_argument('-fp', '--file-path', help='File path to be transliterated', required=True)
  parser.add_argument('-tbw', '--to-buckwalter', help='To Buckwalter transliteration from Arabic', required=False, default='False', choices=['True', 'False'])
  parser.add_argument('-fbw', '--from-buckwalter', help='From Buckwalter transliteration to Arabic', required=False, default='False', choices=['True', 'False'])
  args = parser.parse_args()

  if args.to_buckwalter == args.from_buckwalter:
    sys.exit('You need either to specify -tbw or -fbw\nRun `%s -h` for more information' % sys.argv[0])

  if args.to_buckwalter == 'True':
    transliteration(args.file_path, ARABIC_LETTERS, SYMBOL_LETTERS)
  else:
    transliteration(args.file_path, SYMBOL_LETTERS, ARABIC_LETTERS)
