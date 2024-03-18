data = {1:"Ahmedabad",2:"Surat",3:"Rajkot"}

#print(data.get(10))

k = data.keys()
print(k)
v = data.values()
print(v)
print(data)

#data1 = data.fromkeys([11,22,33],"Gujarat")
data1 = data.fromkeys("ok","Gujarat")
print(data1)