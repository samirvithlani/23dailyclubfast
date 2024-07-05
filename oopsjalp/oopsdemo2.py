#constructor:
'''
    const is special function which has same name as class name....
    def __init__(self):
    type of const
    default const
    patam const

'''

class User:
    
    def __init__(self):
        print("This is a constructor")
        self.name = "Sachin"
        self.age = 28
        self.salary = 10000
    
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)    



u = User()    
u.display()    
    
    