#role of print function...
name = input("Enter your name: ")
age =  int(input("Enter your age: "))

file = open("./filehandling/demo4.txt","a")
# print("Name = ",name,file = file)
# print("Age = ",age,file = file)
print(f"\nName = {name} \n age = {age}",file = file)
file.close() #transaction  management




