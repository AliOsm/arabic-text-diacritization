import io, sys
from os import listdir
from os.path import isfile, join

if len(sys.argv) != 2:
	sys.exit("usage: python %s [FOLDER_PATH]" %sys.argv[0])

folder_path = sys.argv[1]

files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

before_a = 0
after_a = 0
for file in files:
	with io.open(folder_path+file, 'r', encoding='utf-8') as my_file:
		lines = my_file.readlines() 

		pre = '0'
		for line in lines:
			for ch in line:
				if ch == 'ا' and pre == 'ً':
					before_a += 1
				elif ch == 'ً' and pre == 'ا':
					after_a += 1
				pre = ch

print("Before Alif:", before_a)
print("After Alif:", after_a)


