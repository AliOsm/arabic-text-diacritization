# -*- coding: utf-8 -*-

import sys
import argparse
import pickle as pkl

CONSTANTS_PATH = 'constants'

def get_diacritic_class(idx, line, case_ending, arabic_letters, diacritic_classes):
  # Handle without case ending
  if not case_ending:
    end = True
    for i in range(idx + 1, len(line)):
      if line[i] not in diacritic_classes:
        end = line[i].isspace()
        break
    if end:
      return -1

  if idx + 1 >= len(line) or line[idx + 1] not in diacritic_classes:
    # No diacritic
    return 0

  diac = line[idx + 1]

  if idx + 2 >= len(line) or line[idx + 2] not in diacritic_classes:
    # Only one diacritic
    return diacritic_classes.index(diac) + 1

  diac += line[idx + 2]

  try:
    # Try the possibility of double diacritics
    return diacritic_classes.index(diac) + 1
  except:
    try:
      # Try the possibility of reversed double diacritics
      return diacritic_classes.index(diac[::-1]) + 1
    except:
      # Otherwise consider only the first diacritic
      return diacritic_classes.index(diac[0]) + 1

def get_diacritics_classes(line, case_ending, arabic_letters, diacritic_classes, style):
  classes = list()
  for idx, char in enumerate(line):
    if style == 'Fadel':
      if char in arabic_letters:
        classes.append(get_diacritic_class(idx, line, case_ending, arabic_letters, diacritic_classes))
    elif style == 'Zitouni':
      if char in diacritic_classes or char.isspace():
        continue
      classes.append(get_diacritic_class(idx, line, case_ending, arabic_letters, diacritic_classes))
  return classes

def clear_line(line, arabic_letters, diacritic_classes):
  line = ' '.join(''.join([char if char in list(arabic_letters) + diacritic_classes + [' '] else ' ' for char in line]).split())
  new_line = ''
  for idx, char in enumerate(line):
  	if char not in diacritic_classes or (idx > 0 and line[idx - 1] != ' '):
  		new_line += char
  line = new_line
  new_line = ''
  for idx, char in enumerate(line):
  	if char not in diacritic_classes or (idx > 0 and line[idx - 1] != ' '):
  		new_line += char
  return new_line

def calculate_der(original_file, target_file, arabic_letters, diacritic_classes, style, case_ending=True, no_diacritic=True):
  with open(original_file, 'r') as file:
    original_content = file.readlines()

  with open(target_file, 'r') as file:
    target_content = file.readlines()

  assert(len(original_content) == len(target_content))

  equal = 0
  not_equal = 0
  for (original_line, target_line) in zip(original_content, target_content):
    if style == 'Fadel':
      original_line = clear_line(original_line, arabic_letters, diacritic_classes)
      target_line = clear_line(target_line, arabic_letters, diacritic_classes)

    original_classes = get_diacritics_classes(original_line, case_ending, arabic_letters, diacritic_classes, style)
    target_classes = get_diacritics_classes(target_line, case_ending, arabic_letters, diacritic_classes, style)

    assert(len(original_classes) == len(target_classes))

    for (original_class, target_class) in zip(original_classes, target_classes):
      if not no_diacritic and original_class == 0:
        continue
      if original_class == -1 and target_class != -1:
        print('WOW!')
      if original_class != -1 and target_class == -1:
        print('WOW!')
      if original_class == -1 and target_class == -1:
        continue

      equal += (original_class == target_class)
      not_equal += (original_class != target_class)

  return round(not_equal / max(1, (equal + not_equal)) * 100, 2)

def calculate_wer(original_file, target_file, arabic_letters, diacritic_classes, style, case_ending=True, no_diacritic=True):
  with open(original_file, 'r') as file:
    original_content = file.readlines()

  with open(target_file, 'r') as file:
    target_content = file.readlines()

  assert(len(original_content) == len(target_content))

  equal = 0
  not_equal = 0
  for idx, (original_line, target_line) in enumerate(zip(original_content, target_content)):
    if style == 'Fadel':
      original_line = clear_line(original_line, arabic_letters, diacritic_classes)
      target_line = clear_line(target_line, arabic_letters, diacritic_classes)

    original_line = original_line.split()
    target_line = target_line.split()

    assert(len(original_line) == len(target_line))

    for (original_word, target_word) in zip(original_line, target_line):
      original_classes = get_diacritics_classes(original_word, case_ending, arabic_letters, diacritic_classes, style)
      target_classes = get_diacritics_classes(target_word, case_ending, arabic_letters, diacritic_classes, style)

      assert(len(original_classes) == len(target_classes))

      if len(original_classes) == 0:
        continue

      equal_classes = 0
      for (original_class, target_class) in zip(original_classes, target_classes):
        if not no_diacritic and original_class == 0:
          equal_classes += 1
          continue
        equal_classes += (original_class == target_class)

      equal += (equal_classes == len(original_classes))
      not_equal += (equal_classes != len(original_classes))

  return round(not_equal / max(1, (equal + not_equal)) * 100, 2)

def calculate_ser(original_file, target_file, arabic_letters, diacritic_classes, style, case_ending=True, no_diacritic=True):
  with open(original_file, 'r') as file:
    original_content = file.readlines()

  with open(target_file, 'r') as file:
    target_content = file.readlines()

  assert(len(original_content) == len(target_content))

  equal = 0
  not_equal = 0
  for idx, (original_line, target_line) in enumerate(zip(original_content, target_content)):
    if style == 'Fadel':
      original_line = clear_line(original_line, arabic_letters, diacritic_classes)
      target_line = clear_line(target_line, arabic_letters, diacritic_classes)

    original_line = original_line.split()
    target_line = target_line.split()

    assert(len(original_line) == len(target_line))

    equal_words = True
    for (original_word, target_word) in zip(original_line, target_line):
      original_classes = get_diacritics_classes(original_word, case_ending, arabic_letters, diacritic_classes, style)
      target_classes = get_diacritics_classes(target_word, case_ending, arabic_letters, diacritic_classes, style)

      assert(len(original_classes) == len(target_classes))

      if len(original_classes) == 0:
        continue

      equal_classes = 0
      for (original_class, target_class) in zip(original_classes, target_classes):
        if not no_diacritic and original_class == 0:
          equal_classes += 1
          continue
        equal_classes += (original_class == target_class)

      if equal_classes != len(original_classes):
        equal_words = False

    equal += equal_words
    not_equal += not equal_words

  return round(not_equal / max(1, (equal + not_equal)) * 100, 2)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Calculate DER and WER')
  parser.add_argument('-ofp', '--original-file-path', help='File path to original text', required=True)
  parser.add_argument('-tfp', '--target-file-path', help='File path to target text', required=True)
  parser.add_argument('-s', '--style', help='How to calculate DER and WER', required=False, default='Fadel', choices=['Zitouni', 'Fadel'])
  args = parser.parse_args()

  with open(CONSTANTS_PATH + '/ARABIC_LETTERS_LIST.pickle', 'rb') as file:
    ARABIC_LETTERS_LIST = pkl.load(file)

  with open(CONSTANTS_PATH + '/CLASSES_LIST.pickle', 'rb') as file:
    CLASSES_LIST = pkl.load(file)

  print('+---------------------------------------------------------------------------------------------+')
  print('|       |  With case ending  | Without case ending |  With case ending  | Without case ending |')
  print('|  DER  |------------------------------------------+------------------------------------------|')
  print('|       |          Including no diacritic          |          Excluding no diacritic          |')
  print('|-------+------------------------------------------+------------------------------------------|')
  print('|   %%   |        %5.2f       |        %5.2f        |        %5.2f       |        %5.2f        |' %
        (calculate_der(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style),
        calculate_der(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style, case_ending=False),
        calculate_der(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style, no_diacritic=False),
        calculate_der(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style, case_ending=False, no_diacritic=False)))
  print('+---------------------------------------------------------------------------------------------+')
  print('')
  print('+---------------------------------------------------------------------------------------------+')
  print('|       |  With case ending  | Without case ending |  With case ending  | Without case ending |')
  print('|  WER  |------------------------------------------+------------------------------------------|')
  print('|       |          Including no diacritic          |          Excluding no diacritic          |')
  print('|-------+------------------------------------------+------------------------------------------|')
  print('|   %%   |        %5.2f       |        %5.2f        |        %5.2f       |        %5.2f        |' %
        (calculate_wer(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style),
        calculate_wer(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style, case_ending=False),
        calculate_wer(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style, no_diacritic=False),
        calculate_wer(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style, case_ending=False, no_diacritic=False)))
  print('+---------------------------------------------------------------------------------------------+')
  print('')
  print('+---------------------------------------------------------------------------------------------+')
  print('|       |  With case ending  | Without case ending |  With case ending  | Without case ending |')
  print('|  SER  |------------------------------------------+------------------------------------------|')
  print('|       |          Including no diacritic          |          Excluding no diacritic          |')
  print('|-------+------------------------------------------+------------------------------------------|')
  print('|   %%   |        %5.2f       |        %5.2f        |        %5.2f       |        %5.2f        |' %
        (calculate_ser(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style),
        calculate_ser(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style, case_ending=False),
        calculate_ser(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style, no_diacritic=False),
        calculate_ser(args.original_file_path, args.target_file_path, ARABIC_LETTERS_LIST, CLASSES_LIST, args.style, case_ending=False, no_diacritic=False)))
  print('+---------------------------------------------------------------------------------------------+')
  
