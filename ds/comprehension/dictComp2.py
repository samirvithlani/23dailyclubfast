users = ["ram","shyam","madam","naman","racecar","a","radar"]

#palindorme :
#1_
#d1 = {i:i for i in users if i == i[::-1]}
#print(d1)
#{1:"madam",2:"naman",3:"racecar",4:"a",5:"radar"}

#d1 ={i : users[i] for i in range(len(users)) if users[i] == users[i][::-1]}
d1 = {i :users[i] for i in range(0,len(users)) if users[i] == users[i][::-1]}
print(d1)

data = ["amit shah","modi","yogi","rahul gandhi"]

d2 = {i: i for i in data if " " not in i}
print(d2)