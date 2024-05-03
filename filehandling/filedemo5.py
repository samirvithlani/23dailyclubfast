file = open("./filehandling/myfile.txt", "r")
# data  = file.readline()
# print(data)

#read all line using readline()
while True:
    data = file.readline()
    print(data)
    if data == "":
        break

