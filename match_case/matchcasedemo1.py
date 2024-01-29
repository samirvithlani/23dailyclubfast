no1 = int(input("enter first number: "))
no2 = int(input("enter second number: "))

print("enter 1 for add")
print("enter 2 for sub")
print("enter 3 for mul")
print("enter 4 for div")


choice = int(input("enter your choice: "))



match choice:
    case 1:
        add = no1 + no2
        print("addition is: ", add)
    case 2:
        sub = no1 - no2
        print("subtraction is: ", sub)   
    case _:
        print("invalid choice")     

