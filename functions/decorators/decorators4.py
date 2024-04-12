
no1 =int(input("Enter number 1: "))
no2 =int(input("Enter number 2: "))

def smartDiv(func): #div
    
    def inner():
        print("I am going to divide numbers")
        #func()  #div()
        if no2 ==0:
            print("Whoops! cannot divide")
        else:
            func()    
    
    return inner



@smartDiv
def div():
    print(no1/no2)    


div()    