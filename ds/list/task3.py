data = [153,371,1634,90,78,90,1]
armstronglist = []
rem = 0
sum = 0
for i in data:
    lenght = len(str(i)) #153
    temp = i
    while i>0:
        rem = i%10
        sum = sum + rem**lenght
        i = i//10
    
    if sum == temp:
        armstronglist.append(temp)

    sum = 0

print(armstronglist)        

