def checkName(name):
    if len(name)>3:
        if name == name[::-1]:
            return True
        else:
            return False
    else:
        return False

x  = lambda name: checkName(name)
ans = x("a")
print(ans)