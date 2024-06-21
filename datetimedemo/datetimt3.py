from datetime import datetime


now = datetime.now()
# mills = now.timestamp() * 1000
# print(mills)

#get time from milliseconds
#timestamp = mills / 1000
time = datetime.fromtimestamp(now.timestamp())
print(time)



