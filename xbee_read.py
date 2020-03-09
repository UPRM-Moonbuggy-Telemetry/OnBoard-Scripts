import serial
import queue
import json
from time import sleep
from postdata import post_data
from data_to_csv import data_to_csv

ser = serial.Serial('COM1', 9600, timeout=1)  # Establish the connection on a specific port
q = queue.Queue()

while True:
    if(ser.is_open):
        data = ser.readline()
        post_data(data, buggy_flag=None, q) # How do we get the buggy flag?? (json)
        data_to_csv(json.loads(data), "buggy_data.txt") # How do we get the input filename??
        sleep(1)
    else:
        break