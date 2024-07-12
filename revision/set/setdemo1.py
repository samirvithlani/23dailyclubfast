# data = set()
# print(data)
# print(type(data))
'''
set is a collection of unique elements
set is unordered
set is mutable
set is iterable
set is not subscriptable

'''

data = {10,20,30,40,50,10}
print(data)

data.add(60)
print(data)

# data.update([70,80,90])
# data.update("kunal")


data.remove(10)
try:
    data.remove(10)
except KeyError:
    print("Element not found")    


data.discard(10)
print(data)