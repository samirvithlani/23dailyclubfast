age = int(input("enter your age: "))

match age:
    
    case age if age>=18 and age<=25:
        print("you are eligible for voting")
    case age if age>=25 and age<=50:
        print("you are eligible for marriage")
    case _:
        print("you are not eligible for voting and marriage you can enjoy your life")        
