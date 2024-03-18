#black

# data = {100,20}
# print(type(data))


data = {100,20,34,200,1,156,78,99,44,33,33,20}
print(data)

data.add(900)
print(data)
data.update({99,79})
data.update([999,679])
data.update((992,789))
data.update("9090")
print(data)



data.remove(20)
print("after remove")
print(data)


removedElm = data.pop()
print("removed element is ",removedElm)

print("after pop")
print(data)


data.discard(10089009)


# for i in data:
#     print(i)
