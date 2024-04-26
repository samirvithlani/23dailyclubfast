#map #filter #reduce
#map will return all data 
#filter will return only those data which satisfy the condition
#reduce will return only one data

from functools import reduce

x = [10,20,30,40,50]

add = reduce(lambda a,b:a+b,x)
#a = 10 b = 20
#a = 30 b = 30
#a = 60 b = 40
#a = 100 b = 50

print(add)
