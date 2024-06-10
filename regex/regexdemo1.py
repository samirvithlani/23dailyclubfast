#regular expression demo
import re

data = 'ab'

c = re.compile(r'..')
res = c.match(data)
if res:
    print('Matched')
else:
    print('Not Matched')   

