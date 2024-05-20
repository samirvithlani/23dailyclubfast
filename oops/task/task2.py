bus_routes = {}
def readData():
    file = open("./bus.txt", "r")
    lines = file.readlines()
    print(lines)
    for l in lines:
        
        space = l.split()
        bus_name = space[0]
        source = space[1]
        destination = space[2]
        dept_time = space[3]
        arrival_time = space[4]
        fare = space[5]
        seats = space[6]
        bus_routes[bus_name] = {
            'source': source,
            'destination': destination,
            'dept_time': dept_time,
            'arrival_time': arrival_time,
            'fare': fare,
            'seats': seats
    }

readData()   
print(bus_routes)     