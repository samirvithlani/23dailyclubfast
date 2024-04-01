# def displaystudentList(students):
#     print(students)



# displaystudentList(["ram","shyam","mohan","sohan","rohan"])    

def printStuedntList(*args):
    print(args)
    print(type(args))


#printStuedntList()  
printStuedntList("ram","shyam","mohan","sohan","rohan")  


def printStuedntList1(name,*args,y,x):
    print(name)
    print(args)
    print(x)
    


printStuedntList1("ram","shyam","mohan","sohan","rohan",y=90,x=100)    



