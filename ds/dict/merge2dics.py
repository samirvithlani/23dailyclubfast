a = {1:"a", 2:"b", 3:"c"}
b = {4:"d", 5:"e", 6:"f"}

#1st way to merge two dictionaries
a.update(b)
print(a)

#2nd way to merge two dictionaries
a | b
print(a)

#3rd way to merge two dictionaries
a = {**a, **b}
print(a)