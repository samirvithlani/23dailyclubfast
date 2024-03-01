users = {"name":"ram","age":23,"city":"ayodhya","age":25}
print(users)

# removedElm = users.pop("city")
# print("removing",removedElm)
# print(users)


remvedElm = users.popitem()
print("removing",remvedElm)
print(type(remvedElm))
print(users)