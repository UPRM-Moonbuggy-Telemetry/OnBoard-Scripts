import requestsHTTP as req
import queue
import random as rnd
import time as t
from datetime import date as d

date = d.today()
time = t.ctime().split()[3]

data = {}   # Info obtain from the text file must convert to json format
q = queue.Queue()     # This will store the values when there's no connection
dataArray = []      # Array containing all the data
randomData = []
while True:
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
    # randomData.append(data)
    try:
        r = req.getAll()  # Check if there's connection
        if not q.empty():  # If queue is not empty and there's connection dequeue all data to the dataArray
            for i in range(q.qsize()):
                d = q.get()  # Functions as dequeue
                dataArray.append(d)
                req.postData(dataArray)
        else:
            dataArray.append(data)  # If there's connection and the queue is empty just push data to the dataArray
            req.postData(dataArray)
            t.sleep(3)
    except Exception:
        print("Enter exception")
        q.put(data)
        t.sleep(3)


