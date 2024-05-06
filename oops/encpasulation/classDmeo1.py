class Test:
    x =100 # all class variable are by default static..in python
    
    def getUserData(self):
        print(self)
        #self is an current object of class
        self.name = "amit" #instance variable #0070
        print("get user data...")
    
    def printUserData(self):
        print(self.name)    #000 name7


t = Test() # object of class Test
t.getUserData() # calling method of class Test 
t.printUserData() # calling method of class Test     

print(Test.x) #100