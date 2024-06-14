import re

data = "maan"

c = re.compile(r'ma?n')
res = c.match(data)
if res:
    print('Matched')
else:
    print('Not Matched')    

