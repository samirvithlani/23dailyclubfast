data = [('a',('cat', 'car', 'fear', 'center','aamit','okaay','ahmedabad'))]
output = [] #blank list
matchVar = data[0][0]
#check a



# for i in data[0][1]:
#     if matchVar in i:
#         output.append(i)

# print(output)        


for i in data[0][1]:
    if i.count(matchVar) >= 2:
        output.append(i)

print(output)        