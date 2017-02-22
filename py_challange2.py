import string

myfile = file('data.txt')

encoded_string = myfile.read()
#encoded_string = 'http://www.pythonchallenge.com/pc/def/map.html'
decoded_string = ''

for single_char in encoded_string:
    if single_char in  list(string.ascii_lowercase):
             decoded_string += single_char

print decoded_string


