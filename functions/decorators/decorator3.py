def checkRole(func): # getAccess
    
    def inner(userRole,x): #
        
        if userRole == "admin":
            func("hello all","hi all") # getAccess("admin")
        else:
            print("You are not authorized to access this function")    
    
    return inner



@checkRole #inner("admin")
def getAccess(data1,data2):
    print("Access granted")        
    print(data1)
    print(data2)
    


getAccess("admin",100)    