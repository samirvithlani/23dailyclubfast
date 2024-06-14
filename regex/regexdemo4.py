import re

data = "ayea"

c = re.compile(r'(a|b|c)ye')
res =c.match(data)

if res:
    print('Matched')
else:
    print('Not Matched')    