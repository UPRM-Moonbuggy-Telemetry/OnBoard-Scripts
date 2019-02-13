from http_request_script import requestsHTTP as Req
import random as rnd

example =[{
            "strain_sensor_1": 42,
            "strain_sensor_2": 65,
            "strain_sensor_3": 0,
            "strain_sensor_4": 1,
            "vibration_sensor_1": 9,
            "vibration_sensor_2": 20,
            "vibration_sensor_3": 3,
            "vibration_sensor_4": 18,
            "vibration_sensor_5": 0,
            "battery_status": 98,
            "latitude": 87.01343143,
            "longitude": 23.63418
         }]
randomData = []

for x in range(30):
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
            "longitude": rnd.randint(0, 100)
         }
    randomData.append(data)

p = Req.postData(randomData)


print(p)
