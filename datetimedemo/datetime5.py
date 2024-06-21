from datetime import time
a = time()
print(a)

b = time(11, 34, 56)
print(b)

c = time(hour=11, minute=34, second=56)
print(c)

print(b.hour)
print(b.minute)
print(b.second)