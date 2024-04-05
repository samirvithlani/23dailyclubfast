# def add():
#     print("add function")
    
#     def inner():
#         print("sum function")
        
#     inner()

# add()

        

# def outer():
    
#     y =190
#     def inner(a,b):
#         x = 1000
#         print("value of a is",a)
#         print("value of b is",b)
#         print("value of y is",y)
    
    
#     inner(10,20)
#     #print("value of x is",x) error..

# outer()                



# def outer(a,b):
    
#     def inner(x,y):
#         print("value of x is",x)
#         print("value of y is",y)
    
#     inner(a,b)  



# outer(10,20)      
    
    
# def outer(a,b):
    
#     def inner(x,y):
#         print("value of x is",x)
#         print("value of y is",y)
#         return x+y
    
    
#     ans = inner(a,b)
#     print("sum is",ans)


# outer(20,90)    

# def outer(a,b):
    
#     def inner(x,y):
#         print("value of x is",x)
#         print("value of y is",y)
#         return x+y
    
    
#     ans = inner(a,b)
#     return ans


# ans = outer(20,90)
# print("sum is",ans)


def outer(a,b):
    
    def inner(x,y):
        print("value of x is",x)
        print("value of y is",y)
        return x+y
    
    
    return inner(a,b)
    


ans = outer(20,90)        
print("sum is",ans)