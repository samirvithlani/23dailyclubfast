#ram --> datbase
#parth --> admin
#amit ->    user


name = input("Enter your name: ")

match name:
    case "ram" | "RAM":
        print("you are in database")
    case "parth":
        print("you are admin")
    case "amit":
        print("you are user")
    case _:
        print("you are not allowed")            

