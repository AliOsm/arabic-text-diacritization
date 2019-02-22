import sys

ALTR_LIST = 'ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي'
DIAC_LIST = ['َ', 'ً', 'ِ', 'ٍ', 'ُ', 'ٌ', 'ْ', 'ّ']

if len(sys.argv) != 2:
	sys.exit("usage: python %s [FILE_PATH]" %sys.argv[0])

file_path = sys.argv[1]

arabic_chars = 0
diacratic_chars = 0
with open(file_path, 'r') as file:
	lines = file.readlines()

for line in lines:
	for ch in line:
		if ch in ALTR_LIST:
			arabic_chars += 1
		elif ch in DIAC_LIST:
			diacratic_chars += 1

print("Arabic characters count:", arabic_chars)
print("Diacritic characters count:", diacratic_chars)
