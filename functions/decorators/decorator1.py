

def orderPizza(func): #3 func = throwParty()
    print(func)
    def inner(): #5
        print("Pizza ordered!") #6
        func() #7 throwParty()
    
    return inner #4   
    


@orderPizza #2
def throwParty(): #8
    print("Party thrown!") #9


throwParty()  #1    


@orderPizza
def test():
    print("Test")
    
test()    