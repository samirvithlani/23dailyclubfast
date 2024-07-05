class Employee:
    
    def __init__(self,name,age,salary):
        print("This is a constructor")
        self.name = name
        self.age = age
        self.salary = salary
        
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)   


e = Employee("Sachin",28,10000)
e.display()         
e1 = Employee("krish",22,10000)
e1.display()