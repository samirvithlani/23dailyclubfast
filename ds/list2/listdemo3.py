marks = [90,78,65,45,67,89,45]

ind  = marks.index(45) # 3
print("index",ind)

cnt = marks.count(45)
print("count",cnt)


if marks.count(455) > 0:
    ind = marks.index(455) # 3
    print("index",ind)
else:
    print("not found")    


