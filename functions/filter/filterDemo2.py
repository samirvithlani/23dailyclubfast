data = [{"id":101,"name":"raj","age":23,"city":"bangalore","marks":95},{"id":102,"name":"manit","age":25,"city":"bangalore","marks":85},{"id":101,"name":"kunal","age":23,"city":"bangalore","marks":87}]
#print(data)


def has_marks(x):
    return x["marks"]>85 #return True or False


#x = filter(lambda x:x if x["marks"]>85 else False,data)
x = filter(has_marks,data)
print(list(x))