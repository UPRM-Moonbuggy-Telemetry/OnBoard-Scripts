import serial
import queue
import json
from time import sleep
from postdata import post_data
from data_to_csv import data_to_csv

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)  # Establish the connection on a specific port (VERIFY)
q = queue.Queue()

while True:
    if(ser.is_open):
        data = ser.readline()
        post_data(data["data"], data["buggy_name"], q) 
        data_to_csv(json.loads(data), "buggy_data.txt")
        sleep(1)
    else:
        break