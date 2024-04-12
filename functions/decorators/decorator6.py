def loginRequired(func):
    
    def inner(**kwargs): #{role="admin",isLogin=True}
        if kwargs["role"] == "admin" and  kwargs["isLogin"]==True:
            func(**kwargs) #homePage()
        else:
            print("You are not authorized to access this page")    

    return inner



@loginRequired
def homePage(**kwargs): #{role="admin",isLogin=True}
    print("Welcome to home page")
    print("Role: ",kwargs["role"])
    print("isLogin: ",kwargs["isLogin"])        


homePage(role="user",isLogin=True)    
