import csv
import random as rnd
import time as t
timeArray = t.ctime().split(" ")
time = timeArray[3]
date = timeArray[0] + " " + timeArray[1] + " " + timeArray[2]


for i in range(10):         # a for append newline = "" because by default it is \n
    with open('test.csv', 'a', newline="") as csvFile:
        writer = csv.writer(csvFile)
        data = {
            "id": rnd.randint(0, 100),
            "strain_sensor_1": rnd.randint(0, 100),
            "strain_sensor_2": rnd.randint(0, 100),
            "strain_sensor_3": rnd.randint(0, 100),
            "strain_sensor_4": rnd.randint(0, 100),
            "vibration_sensor_1": rnd.randint(0, 100),
            "vibration_sensor_2": rnd.randint(0, 100),
            "vibration_sensor_3": rnd.randint(0, 100),
            "vibration_sensor_4": rnd.randint(0, 100),
            "vibration_sensor_5": rnd.randint(0, 100),
            "battery_status": rnd.randint(0, 100),
            "latitude": rnd.randint(0, 100),
            "longitude": rnd.randint(0, 100),
            "OBC_time": time,
            "OBC_date": date
         }
        writer.writerow(data.values())
    csvFile.close()
