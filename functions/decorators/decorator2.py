
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))

#12 2
def smartdiv(func): # div()
    
    def inner():
        if no2 == 0:
            print("Cannot divide by zero")
            return
        else:
            func() # div()
    
    return inner



@smartdiv
def div():
    print("div function called")
    print(no1//no2)        


div()            
        
    