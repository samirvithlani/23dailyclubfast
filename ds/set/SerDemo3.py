users1  = {"amit","ram","shyam","mohan","sohan"}
users2  = {"amit","shyam","mohan","priya"}


x = users1.union(users2)
print(x)

x1 = users1.intersection(users2) 
print(x1)

#x2 = users1.difference(users2)
x2 = users2.difference(users1)
print("diff",x2)

x3 = users1.symmetric_difference(users2)
print(x3)


# users1.intersection_update(users2)
# print(users1)


users2.difference_update(users1)
print(users2)
#users1.symmetric_difference_update(users2)

