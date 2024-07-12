users = {1,2,3,4,5,6,7}
emps = {6,7,8,9,10}


#users.difference_update(emps)


#users.intersection_update(emps)
# users.symmetric_difference_update(emps)
# print(users)

x = users.copy()

x = users.issubset(emps)
print(x)

x = users.isdisjoint(emps)
print(x)
