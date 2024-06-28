users = {1:"amit",2:"raj",33:"sparta",44:"sachin",5:"sachin"}

fileUsers = {i:j for i,j in users.items() if j.startswith("s")}

# for  i,j in users.items():
#     if j.startswith("s"):
#         fileUsers[i] =j

print(fileUsers)        


emps = {"1":"amit patel","2":"raj shah","3":"kunal patel","4":"rahul kirpekar","5":"sachin tendulkar"}

emps1  = {i:j for i,j in emps.items() if j.endswith("patel")}
print(emps1)

