import random as rnd
import time as t

from datetime import date as d
from radiodata import RadioData
from data_to_csv import data_to_csv

date = d.today()
time = t.ctime().split()[3]
filename = "buggyData.csv"

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

dataObj = RadioData(data)

data_to_csv(dataObj, filename)