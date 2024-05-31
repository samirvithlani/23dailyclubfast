from CustException import invalidString

class InvalidAgeException(Exception):
    
    def __init__(self,message):
        super().__init__(message)



try:
    age = int(input("Enter your age: "))
    if(age<18):
        raise InvalidAgeException("You are not eligible to vote")
except ValueError:
    print("Please enter a valid number")   
except InvalidAgeException as e:     
    print(e)
finally:
    print("End of the program")    
    #transaction management logic
    #database conn close
    #file close
    #network conn close
    #socket close
try:
    name = input("Enter your name: ")
    if not name.isalpha():
        raise invalidString("Please enter a valid name")
except invalidString as e:
    print(e)        

    


    