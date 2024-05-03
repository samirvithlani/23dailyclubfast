file = open("./filehandling/myfile.txt", "r")
count =0    
for i in file:
    count +=1
    print(i,end="")

print("Total lines in file are:",count)    