#remove duplicates from a list
data = ["ram","shyam","geeta","sita","shyam","ram","hari"]
unique = []

for i in data:
    if i not in unique:
        unique.append(i)
    
print(unique)    

#sales list -->[100,20,33,56,78,90]
#2 sep list

#50 above sales --> 10% discount -->list..
#50 below sales --> 5% discount -->list..