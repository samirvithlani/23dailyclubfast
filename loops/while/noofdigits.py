#123
#123 / 10 = 12
#12 // 10 = 1
#1//10 = 0

#78965
#78965 / 10 = 7896
#7896 // 10 = 789
#789 // 10 = 78
#78 // 10 = 7
#7 // 10 = 0



no = int(input("Enter a number: "))
count=0
while no>0:
    no = no // 10 
    count += 1


print("No of digits: ", count)    

    