# def getUsers(*args):
#     print(args)
#     print(type(args))

# def getUsers(*args,x):
#     print("x-",x)
#     print(args)
#     print(type(args))

# def getUsers(x,*args):
#     print("x-",x)
#     print(args)
#     print(type(args))
    
def getUsers(*args,x):
    print(args)
    print(type(args))
    
getUsers("amit","sumit","ramit","shyamit",x="amit")    


# def getUsers1(**kwargs):
#     print(kwargs)
#     print(type(kwargs))


# def getUsers1(**kwargs,x): #compile time error
#     print(kwargs)
#     print(type(kwargs))


# def getUsers1(x,**kwargs):
#     print("x-",x)
#     print(kwargs)
#     print(type(kwargs))
    

def getUsers1(x,**kwargs):
    print("x-",x)
    print(kwargs)
    print(type(kwargs))
    

getUsers1(100,name="amit",age=30,city="delhi",y=100)    