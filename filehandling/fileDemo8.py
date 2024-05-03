file = open("./filehandling/myfile.txt", "r")
count =0
x =[]
line = ""
while True:
    data = file.read(1)
    if data == ".":
        print()
    print(data,end="")
    
        
    if data == "":
        break

print("Total characters in file are:",count)    
print("line = ",line)