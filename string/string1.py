#mutablity and immutablitity
#python string is immutable
#string is an iterable
#string is subscriptable

name = "amit thakkar"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

l = len(name)
print("len" , l)

# for i in range(0,l):
# for i in range(0,len(name)):
#     print(name[i])

#membrship operator

for i in name:
    print(i, end="")




data = "hi this is India"
count =1

for i in data:
    if i == " ":
        count+=1

print("count", count)        
