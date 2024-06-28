sales = ((100,20),(120,30),(150,70))

salesList = list(sales)
n1 = list(salesList[0])
print("n1",n1)
n1[0] = 200
print("n1",n1)
salesList[0] = tuple(n1)

print(salesList)



