users = ["ram","raj","parth","amit","ankit"]
print(users)
#removedElm = users.pop()
removedElm = users.pop(2)
print("removing...",removedElm)
print(users)

if users.count("rama") > 0:
    users.remove("rama")
else:
    print("not found")
print(users)