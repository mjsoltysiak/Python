import string

encoded_string = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
#encoded_string = 'http://www.pythonchallenge.com/pc/def/map.html'
decoded_string = ''

for single_char in encoded_string:
    if single_char in  list(string.ascii_lowercase):
        if single_char not in {'y','z'}:
             decoded_string += chr((ord(single_char) +2)  )
        else:
             decoded_string += chr((ord(single_char) +2)-26  )
    else:
         decoded_string += chr(ord(single_char))

print decoded_string

intab = encoded_string
outtab = decoded_string
trantab = string.maketrans(intab, outtab)

str = "map.html";
print str.translate(trantab);
