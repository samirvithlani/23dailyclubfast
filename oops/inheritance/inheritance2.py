class Laptop:
    
    def __init__(self):
        x =100 #local variable
        self.brand = "Dell" #instance variable


class Charger(Laptop):
    
    def __init__(self):
        super().__init__()
        self.voltage = 220


class Cable(Charger):
    
    def __init__(self):
        super().__init__()
        self.length = 1.5
    
    
    def display(self):
        print(self.brand)
        print(self.voltage)
        print(self.length)                    
        

c = Cable()
c.display()        