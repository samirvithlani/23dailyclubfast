age = int(input("Enter your age: "))

if age>18:
    print("You are eligible to vote")
    if age>21:
        print("You are eligible to marry")
        if age>60:
            print("You are eligible to retire")
        else:
            print("You are not eligible to retire")    
        
    else:
        print("You are not eligible to marry")    
    

else:
    print("You are not eligible to vote")  
    
    if age>14:
        print("You are eligible for school")
    else:
        print("You are not eligible for school")      