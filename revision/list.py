#[] dt : list 
#list allows duplicate elements
#list is ordered
#list is mutable
#list is indexed
#list is iterable
#list is dynamic
#list is heterogenous
#list is subscriptable

data = ["apple", "banana", "cherry", "apple", "cherry"]

# for i in data:
#     print(i)


# for i in range(0,len(data)):
#     print(data[i])

data.append("orange") # add element at the end
print(data)
data.insert(1, "mango") # add element at specific index
print(data)
data.remove("apple") # remove element by value
print(data)
data.pop() # remove element from end
print(data)
data.pop(1) # remove element by index
print(data)

cnt = data.count("apple") # count the number of occurence of element
print(cnt)

data.extend(["orange", "grapes"]) # add multiple elements at the end
print(data)

#data.clear() # remove all elements
#data.sort(reverse=True) # sort the list
#print(data)
data.reverse() # reverse the list
print(data)


