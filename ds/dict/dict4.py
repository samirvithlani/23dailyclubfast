sales = {2010:1000,2015:1500,2020:1800,2024:2300}

for i,j in sales.items():
    print(i,j)

sales[2022] = 2100

removedElm = sales.pop(2020)    
print("removing",removedElm)
print(sales)



students = {"naman":23,"madam":"34","amit":33,"ram":23,"a":100}

for i,j in students.items():
    if i == i[::-1]:
        print(i,j)