data = ["ram","shyaam","hari","gita","sita"]

filList = [i for i in data if len(i)>4]

# for i in data:
#     if len(i)>4:
#         filList.append(i)

print(filList)        


marks = [100,78,89,67,77,54,88]

filMarks = [i for i in marks if i >=60 and i %2 ==0]
print(filMarks)



names = ["am it","hari","geeta","see ta"]        

filNames  =[i for i in names if " " in i]
print(filNames)