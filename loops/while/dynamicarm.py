no = int(input("Enter a number: "))
temp = no

noofdigits = 0
while temp>0:
    temp = temp // 10
    noofdigits += 1

print("No of digits: ", noofdigits)    

rem = 0
add = 0
while no>0:
    rem = no % 10    
    add = add + rem**noofdigits
    no = no // 10

print("Sum of digits: ", add) 

#1634
#1^4 + 6^4 + 3^4 + 4^4 = 1634   
