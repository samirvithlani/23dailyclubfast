sales = [10,20,22,34,5,23,5,67,80,87]

#sales1 = [i**2 for i in sales if i % 2 == 0]
#even sq and odd cube
sales1 = [i**2 if i %2 ==0 else i **3 for i in sales]
print(sales1)


names = ["naman","race","amit","madam"]

palindromeNames = [i.upper() for i in names if i == i[::-1]]

# for i in names:
#     if i == i[::-1]:
#         palindromeNames.append(i)

print(palindromeNames)        
