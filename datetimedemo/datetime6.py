from datetime import datetime

now = datetime.now() #current date,,,,

t = now.strftime("%H-%M-%S")
print("time:", t)

s1 = now.strftime("%m/%a/%Y, %H:%M:%S")
#d = now.strftime("%a")
#print("day:", d)
d = now.strftime("%A")
print("day:", d)
print("s1:", s1)
print(type(s1))