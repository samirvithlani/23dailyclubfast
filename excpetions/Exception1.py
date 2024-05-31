try:
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    print("First number is: ", no1)
    print("Second number is: ", no2)
    result = no1 / no2
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Second number should not be zero")   

except Exception:
    print("Some error occured")     

else:
    print("Result is: ", result)    


print("End of the program")        