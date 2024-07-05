class Parent:
    
    def __init__(self):
        print("parent class constructor")
        self.prop = 100
        self.data = "parent data"


class Child(Parent):
    
    def __init__(self):
        super().__init__() #calling parent class constructor
        print("Child class constructor")
    
    def display(self):
        print("Property: ",self.prop)
        print("Data: ",self.data)    



c = Child()     
c.display()   