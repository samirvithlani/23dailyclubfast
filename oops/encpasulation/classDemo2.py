#constructor: constructor is special method in python which us 
# use to initialize the instance variable of class
# def __init__(self)
# type of constructor: 1. default constructor 2. parameterized constructor

class bank:
    
    def __init__(self):
        self.name = "SBI"
        self.branch = "Kolkata"
        print("This is default constructor")
    
    
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch    
    
    def show(self):
        print("Name: ",self.name)
        print("Branch: ",self.branch)        



b = bank("SBI","Kolkata")    
#b = bank()
b.show()     