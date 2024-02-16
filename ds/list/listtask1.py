data= []
while True:
    name = input("Enter name")
    data.append(name)
    choice = int(input("do you want to add more names? yes/no prees 1 for yes"))
    if choice != 1:
        break
        
    
print(data)    