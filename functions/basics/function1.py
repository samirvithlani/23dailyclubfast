def test():
    print("Tets called")
    #with return without params


def add(no1,no2) -> int:
    #with return with params
    no3 = no1 + no2
    return no3


test()    

ans = add(100.20,20.70)
print("ans = ",ans)


def sum():
    sales  =[100,200,300,400,500]
    # m = max(sales)
    # return m
    return max(sales)

maxno =sum()
print("maxno = ",maxno)

print("max --->",sum())

