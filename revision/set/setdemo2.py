# users = {"ram", "shyam", "hari", "gita", "sita","nita" }
# emps =  {"rita", "nita", "tita", "mita", "kita","ram","shyam"}

users = {1,2,3,4,5,6,7}
emps = {6,7,8,9,10}

x = users.difference(emps)
print(x)


x = users.intersection(emps)
print(x)

x = users.union(emps)
print(x)

x = users.symmetric_difference(emps)
print(x)

# print(type(users))