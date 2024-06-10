#regular expression demo
import re

data = 'okjava'

c = re.compile(r'\w')
res = c.fullmatch(data)
if res:
    print('Matched')
else:
    print('Not Matched')   

