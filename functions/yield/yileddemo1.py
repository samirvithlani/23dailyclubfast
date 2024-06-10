def getData():
    yield "Hello"
    yield 2
    yield 3
    yield 4
    yield 5

# x = getData()
# print(x)

for i in getData():
    print(i)