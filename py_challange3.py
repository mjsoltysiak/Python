import string
import re

myfile = file('data2.txt')

encoded_string = myfile.read()
solution = ''

decoded = re.findall(r'[^A-Z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][^A-Z]', encoded_string)

print decoded

for cased_letter in decoded:
    solution += cased_letter[4]

print solution
