import sys
import pickle as pkl

# Constants
CONSTANTS_PATH = 'constants'

with open(CONSTANTS_PATH + '/ARABIC_LETTERS_LIST.pickle', 'rb') as file:
  ARABIC_LETTERS_LIST = pkl.load(file)

with open(CONSTANTS_PATH + '/CLASSES_LIST.pickle', 'rb') as file:
  CLASSES_LIST = pkl.load(file)

def get_diacritic_class(idx, line, case_ending):
  idxs = [idx + 1, idx + 2, idx + 3]

  # Handle without case ending
  if not case_ending:
    if idxs[0] == len(line):
      return -1
    if idxs[0] < len(line) and (line[idxs[0]] not in ARABIC_LETTERS_LIST and \
                                line[idxs[0]] not in CLASSES_LIST):
      return -1
    
    if idxs[0] < len(line) and line[idxs[0]] in CLASSES_LIST:
      if idxs[1] == len(line):
        return -1
      if idxs[1] < len(line) and (line[idxs[1]] not in ARABIC_LETTERS_LIST and \
                                  line[idxs[1]] not in CLASSES_LIST):
        return -1

      if idxs[1] < len(line) and line[idxs[1]] in CLASSES_LIST:
        if idxs[2] == len(line):
          return -1
        if idxs[2] < len(line) and (line[idxs[2]] not in ARABIC_LETTERS_LIST and \
                                    line[idxs[2]] not in CLASSES_LIST):
          return -1

  if idxs[0] >= len(line) or line[idxs[0]] not in CLASSES_LIST:
    # No diacritic
    return 0
  
  diac = line[idx + 1]

  if idxs[1] >= len(line) or line[idxs[1]] not in CLASSES_LIST:
    # Only one diacritic
    return CLASSES_LIST.index(diac) + 1
  
  diac += line[idxs[1]]

  try:
    # Try the possibility of double diacritics
    return CLASSES_LIST.index(diac) + 1
  except:
    try:
      # Try the possibility of reversed diacritics
      return CLASSES_LIST.index(diac[::-1]) + 1
    except:
      # Otherwise consider only the first diacritic
      return CLASSES_LIST.index(diac[0]) + 1

def get_diacritics_classes(line, case_ending):
  classes = list()
  for idx, char in enumerate(line):
    if char in ARABIC_LETTERS_LIST:
      classes.append(get_diacritic_class(idx, line, case_ending))
  return classes

def calculate_der(original_file, output_file, case_ending=True, no_diacritic=True):
  with open(original_file, 'r') as file:
    original_content = file.readlines()
  
  with open(output_file, 'r') as file:
    output_content = file.readlines()

  assert(len(original_content) == len(output_content))

  equal = 0
  not_equal = 0
  for (original_line, output_line) in zip(original_content, output_content):
    original_classes = get_diacritics_classes(original_line, case_ending)
    output_classes = get_diacritics_classes(output_line, case_ending)

    assert(len(original_classes) == len(output_classes))

    for (original_class, output_class) in zip(original_classes, output_classes):
      if not no_diacritic and original_class == 0:
        continue
      if original_class == -1 and output_class != -1:
        print('WOW!')
      if original_class != -1 and output_class == -1:
        print('WOW!')
      if original_class == -1 and output_class == -1:
        continue
      
      equal += (original_class == output_class)
      not_equal += (original_class != output_class)

  return round(not_equal / (equal + not_equal) * 100, 2)

def calculate_wer(original_file, output_file, case_ending=True, no_diacritic=True):
  with open(original_file, 'r') as file:
    original_content = file.readlines()
  
  with open(output_file, 'r') as file:
    output_content = file.readlines()
  
  assert(len(original_content) == len(output_content))

  equal = 0
  not_equal = 0
  for (original_line, output_line) in zip(original_content, output_content):
    original_line = original_line.split()
    output_line = output_line.split()

    assert(len(original_line) == len(output_line))

    for (original_word, output_word) in zip(original_line, output_line):
      original_classes = get_diacritics_classes(original_word, case_ending)
      output_classes = get_diacritics_classes(output_word, case_ending)

      assert(len(original_classes) == len(output_classes))

      if len(original_classes) == 0:
        continue

      equal_classes = 0
      for (original_class, output_class) in zip(original_classes, output_classes):
        if not no_diacritic and original_class == 0:
          equal_classes += 1
          continue
        equal_classes += (original_class == output_class)

      equal += (equal_classes == len(original_classes))
      not_equal += (equal_classes != len(original_classes))

  return round(not_equal / (equal + not_equal) * 100, 2)

if __name__ == '__main__':
  if len(sys.argv) != 3:
    sys.exit('usage: python %s [ORIGINAL_TEXT_FILE] [PREDICTED_TEXT_FILE]' % sys.argv[0])

  ORIGINAL_TEXT_FILE = sys.argv[1]
  PREDICTED_TEXT_FILE = sys.argv[2]

  print('DER with case ending (no diacritics included):', calculate_der(ORIGINAL_TEXT_FILE, PREDICTED_TEXT_FILE))
  print('DER without case ending (no diacritics included):', calculate_der(ORIGINAL_TEXT_FILE, PREDICTED_TEXT_FILE, case_ending=False))
  print('WER with case ending (no diacritics included):', calculate_wer(ORIGINAL_TEXT_FILE, PREDICTED_TEXT_FILE))
  print('WER without case ending (no diacritics included):', calculate_wer(ORIGINAL_TEXT_FILE, PREDICTED_TEXT_FILE, case_ending=False))
  print('')
  print('DER with case ending (no diacritics not included):', calculate_der(ORIGINAL_TEXT_FILE, PREDICTED_TEXT_FILE, no_diacritic=False))
  print('DER without case ending (no diacritics not included):', calculate_der(ORIGINAL_TEXT_FILE, PREDICTED_TEXT_FILE, case_ending=False, no_diacritic=False))
  print('WER with case ending (no diacritics not included):', calculate_wer(ORIGINAL_TEXT_FILE, PREDICTED_TEXT_FILE, no_diacritic=False))
  print('WER without case ending (no diacritics not included):', calculate_wer(ORIGINAL_TEXT_FILE, PREDICTED_TEXT_FILE, case_ending=False, no_diacritic=False))
