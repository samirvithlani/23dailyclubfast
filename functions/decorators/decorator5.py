def orderPizza(func):
    
    #qty =20
    def inner(qty):
        print("qty ",qty)
        print("Ordering pizza")
        if qty>=1:
            func(qty*100) #throwParty(20*100)
        else:
            print("Invalid quantity")
    
    return inner



@orderPizza
def throwParty(amount):
    print("Throwing party and your bill is: ", amount)
    

throwParty(20)    
                