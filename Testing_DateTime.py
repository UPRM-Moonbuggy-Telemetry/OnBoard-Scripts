import time
time = time.ctime()
timeArray = time.split(" ")
print(timeArray)
date = timeArray[0] + " " + timeArray[1] + " " + timeArray[2]
t = timeArray[3]
print(date)
print(t)
