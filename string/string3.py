
#lower
name = input("Enter your name: ")
upper= ""
#amit
for i in name:
    #i =a - 97
    if ord(i) >=97 and ord(i)<=122:
        #"" = ""+ chr(97-32)65 = A
        #"A"
        upper = upper + chr(ord(i)-32)

print(upper)        


x = 65
print(chr(x)) #A
x = "A"
print(ord(x)) #65