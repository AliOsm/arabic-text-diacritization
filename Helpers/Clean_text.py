import io
import csv


DIAC_LIST = ['َ', 'ً', 'ِ', 'ٍ', 'ُ', 'ٌ', 'ْ', 'ّ']

with io.open("text.txt", "r", encoding="utf-8") as my_file:
     lines = my_file.readlines()


new_lines = []

for line in lines:
	new_line  = ""
	for ch in line:
		if  ch in DIAC_LIST:
			continue
		new_line += ch
	new_lines.append(new_line)

print(new_lines)	 


with io.open("t.txt", 'w', encoding="utf-8") as my_file:
	for line in new_lines:
		my_file.write(line)