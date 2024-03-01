# users = {} #empty dictionary
# print(users)
# print(type(users))

users = {"name":"ram","age":23,"city":"ayodhya","age":25}
print(users)

print(users["name"])
print(users["age"])


x = users.items()

for i,j in users.items():
    print(i,j)

