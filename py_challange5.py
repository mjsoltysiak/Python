import string
import re
import urllib
import pickle

adress_web = 'http://www.pythonchallenge.com/pc/def/banner.p'
s = urllib.urlopen(adress_web)
    
k =  s.read()
data = pickle.loads(k)
print '\n'.join([''.join([p[0] * p[1] for p in row]) for row in data])


