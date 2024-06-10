#pass lmbda function as an argument to another function

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

#x = lambda a : a + 10
myfunc(lambda a : a + 10)
