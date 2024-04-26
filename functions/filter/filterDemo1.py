#predicate statment 
#
sales = [1,3,4,5,8,7,9]
evenSales = filter(lambda x: x%2==0,sales)
print(list(evenSales)) 

users = ["amit","neh a","sur esh","rame sh","akshit"]

user1 = list(filter(lambda x:x.startswith("a"),users))
print(user1)

user2 = filter(lambda x:x if " " in x else False,users)
print(list(user2))




