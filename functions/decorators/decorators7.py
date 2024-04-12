def isValid(func):
    
    def inner(*args):
        flag = True
        for i in args:
            if type(i) != str:
                #print("Invalid data")
                flag = False
        
        if flag == True:
            func(*args)   #voterData("ram","shyam","mohan")      
        else:
            print("Invalid data")    
               
    
    return inner



@isValid
def voterData(*args):
    print("Voter data is: ",args)


voterData("ram","shyam","mohan")    
