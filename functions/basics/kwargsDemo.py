#args + kwa


def printData(x,**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(x)


#printData()    
printData(100,name="raj",age=23,marks=78,rollno=23,city="delhi")