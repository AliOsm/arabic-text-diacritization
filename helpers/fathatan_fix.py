import io, os, sys, re
import pickle as pkl

if len(sys.argv) != 2:
  sys.exit('usage: python %s [FILE_PATH]' % sys.argv[0])

FILE_PATH = sys.argv[1]

with open(FILE_PATH, 'r') as file:
  lines = file.readlines()

new_lines = []
for line in lines:
	new_lines.append(re.sub(r'اً', 'ًا', line))

FILE_PATH = FILE_PATH.split(os.sep)
FILE_PATH[-1] = 'fathatan_fixed_' + FILE_PATH[-1]
FILE_PATH = os.sep.join(FILE_PATH)

with open(FILE_PATH, 'w') as file:
	file.write(''.join(new_lines))
