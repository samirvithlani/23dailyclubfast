class Usa:
    
    president = "Amit Shah"
    king = "prince shah"
    
    def __init__(self):
        self.population = 3000000
        self.name = "Usa"
        print("Usa Constructor")


class Uae():
    
    president = "Jay Shah"
    
    def __init__(self):
        self.population = 2000000
        self.country = "Uae"
        print("Uae Constructor")        


class Person(Usa,Uae):
    
    def __init__(self):
        super().__init__()
        print("Person Constructor")
    
    
    def myData(self):
        print(self.population)
        print(self.name)
        #print(self.country)       
        print(self.president)         
        print(self.king)
        
p = Person()
p.myData()
        
        