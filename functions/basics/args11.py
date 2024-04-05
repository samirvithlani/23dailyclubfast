def getData(*args):
    print(args)
    print(type(args))



getData(12,22,"amit","kumar","singh")    

def getData1(*args,name):
    print(args)
    print(name)


getData1(12,22,"amit","raj","parth","ok",name = "rohit")    