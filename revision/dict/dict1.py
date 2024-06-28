#[],() <--index ==> dict --> key:value
'''
dict stores data in key value pair
dict allows duplicate values | but not duplicate keys
dict is mutable
dict is unordered
'''

test = {1:"India",2:"Nepal",3:"Bhutan",4:"Srilanka",5:"Pakistan",3:"bhutan"}
print(test)
print(test[2])
print(test.get(2))

print(test.keys())
print(type(test.keys()))
print(test.values())

print(test.items())

# for i in test.keys():
#     print(i)

# for i in test.values():
#     print(i)    


# for i,j in test.items():
#     print(i,j)

#values add
test[6] = "Bangladesh"
#test[5] = "Bangladesh" overwrites the value of 5

test.update({5:"Bangladesh",55:"China"})


#remove

removedElm = test.pop(5)
print("removing...",removedElm)

removedElm = test.popitem()
print("removing...",removedElm)


test.clear()


print(test)