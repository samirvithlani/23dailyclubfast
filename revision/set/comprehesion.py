users = {1,2,3,55,67,89,43,56,78,9}

x = {x for x in users if x % 2 == 0}
print(x)