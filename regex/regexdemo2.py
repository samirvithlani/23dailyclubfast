import re

'''
+ - one or more
* - zero or more

'''

data = "8460224296"
#c = re.compile(r'[a-z]+')
#c = re.compile(r'[a-z]+[0-9]*')
c = re.compile(r'[6-9]{1}[0-9]{9}')
res = c.match(data)
if res:
    print('Matched')
else:
    print('Not Matched')    
