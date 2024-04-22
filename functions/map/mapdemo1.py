#map demo

users = ["amit","neha","suresh","ramesh"]

#d = lambda x:x.upper()
#d("amit")
#only give that kind of expression which is returning something
#do not give predicate expression
users1 = map(lambda x:x.upper(),users)
print(list(users1))

marks = [["amit","a"],["raj","r"],["kunal","k"]]

#marks1 = map(lambda x:x[0],marks)
marks1 = map(lambda x:list(map(lambda y:y.upper(),x)),marks) #[amit,78],[raj.82],[kunal,64]
print(list(marks1))


data = [1,2,3,4] #[2,4,6,8]
data1 = map(lambda x:x*2,data)
print(list(data1))

d1 = [1,2,3]
d2 = [4,5,6] #[5,7,9]

add = map(lambda x,y:x+y,d1,d2)
print(list(add))

#map with if
users = ["amit","neha","suresh","ramesh","akshit"]

userWithAinUpper = map(lambda x:x.upper() if x.startswith("a") else x,users)
print(list(userWithAinUpper))

sales = [1,3,4,5,8,7,9]

sales1 = map(lambda x:x**2 if x %2==0 else x**3,sales)
print(list(sales1))

name = "parth"

name1 = map(lambda x:x,name)
print(list(name1))
