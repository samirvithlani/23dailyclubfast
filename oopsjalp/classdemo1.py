#local variable def :
#instance variable def : self
#class variable def : class name static variable

class Bank:
    
    #//class leval static variable
    def account(self):  
        #self == current object
        print("Account class method")
        self.user = "Rajesh"
        self.balance = 1000
        
    def deposit(self,amount):
        print("Deposit class method")
        print("User Name : ",self.user)  
        self.balance = self.balance + amount
        print("Balance : ",self.balance)

#obj
b = Bank()
b.account() #class object        
b.deposit(1000) #class object