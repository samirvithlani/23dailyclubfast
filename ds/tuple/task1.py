#Write a Python program to find strings in a given list starting with a given prefix.
#Input:
#[( ca,('cat', 'car', 'fear', 'center'))]
#Output:
#['cat', 'car']

data = [('ca',('cat', 'car', 'fear', 'center'))]
matchVar = data[0][0]
print(matchVar)
output = [] #blank list
#print(data[0][1])

for i in data[0][1]:
    if i.startswith(matchVar):
        output.append(i)


print(output)        

