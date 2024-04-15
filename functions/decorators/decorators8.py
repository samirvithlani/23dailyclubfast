def isValid(func):
    def inner(*args): #2,4,3,5,7
        flag = True #True
        for i in args:
            #4 True
            if isPrime(i) == False:
                flag = False
                break
        
        if flag == True:
            func(*args)
        else:
            print("Invalid input")        
    
    return inner        


def isPrime(num): #2
    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            #4 %2 == 0
            #4 %3 == 1
            if (num % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                break

    # check if flag is True
        if flag == True:
            return False
        else:
            return True


@isValid
def display(*args):
    print("Prime numbers are:",args)        

display(2,3,5,7,44)