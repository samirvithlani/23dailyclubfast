data =["java",'python','c',"java",'c++']
print(data)
#removedELm = data.pop() #it will remove last element
# removedELm = data.pop(2) 
# print("removing...",removedELm)


if data.count("python1")>0:
    data.remove("python1")
else:
    print("not found")    
    
print(data)


cnt = data.count('java1')
print("count",cnt)


try:
    data.remove("abc")
except ValueError as e:
    print("Error",e)    










