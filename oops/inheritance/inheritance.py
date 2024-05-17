class RBI:
    
    def __init__(self):
        self.name = "RBI"
        print("RBI Constructor")


class SBI(RBI):
    
    def __init__(self):
        super().__init__()
        print("SBI Constructor")
        

    def  display(self):
        print("SBI Display")
        print(self.name)


s  = SBI()   
s.display()             