from os import close
import Pre_Processor
import serial
import sys
import serial.tools.list_ports
# Maybe implement this to return a list
# of all available serial ports connected

import _thread
from env_variables import DATA_LISTENER, PING_LISTENER

import time
import RPi.GPIO as GPIO
import pynmea2 #Download pynmea2 on raspberry pi being used
from radiodata.radiodata import RadioData
from data_to_csv import data_to_csv
from serializeObjects import send_json
from csv_funcs import csv_to_json
import pypreprocessor #Download pypreprocessor on raspberry pi being used

"""
GPIO manda string directo (GPS data)
Todo lo que se mande por Arduino a serial hay que darle un .decode 
Parser se llama despues de todos los calculos y visnes

TO DO:
    Modificar parsing function
"""

def parser(Data_String, GPS_String):
    # Splits all data recieved and chops it up by its delimiter to be
    # assigned to their respective variables to be processed.
    data_types = Data_String.split(',')
    
    """
    GPS recieved via GPIO(UART) pins
    Make calls to GPIO and receive list
    """

    GPS_List = pynmea2.parse(GPS_String)
    GPS_LL_List = [GPS_List.latitude, GPS_List.longitude] # This requires Pynmea2
    
    #------------------------------|
    del GPS_List      # Releasing memory due to limitations of rasberry pi
    del Data_String   # in order to increase speed/efficiency, hopefully :) 
    #------------------------------|

    return data_types, GPS_LL_List

def process_data(threadID): 
    arduino = serial.Serial('COM5', 9600) #Replace 'COM' port for 'ttyACM*some number*' when not using windows
    # Raspberry Pi sends through one port
    GPIO.setmode(GPIO.BOARD)
    decoded_data = None
    GPS_Input = GPIO.setup(8, input)

    print("Thread ID: #{} is online.\nReading data from Arduino.\n".format(threadID))

#   print(arduino)
    while True:
        
        time.sleep(0.2)
        # data refers to direct arduino reads
        data = arduino.readline()

        # Assume 'data' is true when signal is not lost and is receiving data
        if data:
            decoded_data = data.decode("utf-8")
            cleaned_data_list, gps_data_list = parser(decoded_data, GPS_Input)
            obj = RadioData(cleaned_data_list, gps_data_list) # Creates object of type RadioData with parsed data lists // Comment if it does not work correctly
            data_to_csv(obj, "DataLog.csv") # Comment if it does not work correctly
            # Keep local CSV file that is appended so that data loss is prevented in case of signal loss. 

def send_data(threadID):
    reconnect = False 
    # Groundstation pings the thread
    antenna = serial.Serial('COM6', 9600) #Replace 'COM' port for 'ttyACM*some number*' when not using windows
    # Raspberry Pi recieves through another port

    print("Thread ID: #{} is online.\nListening for grounstation Pings.\n".format(threadID))

    break_loop = True

    with open("DataLog.csv",) as csvf: 
        while True and break_loop:
            time.sleep(0.3) #Sleeping in case this fnct is faster than 'process data' ---------------|
            flag = antenna.readline()

            if flag == 1:

                    # Prototype functionality for disconection and reconnection
                    # Assuming existing functions

                    if reconnect:
                        # Create function "local_upload" to upload local data log
                        # Implement multithreading to prevent data back ups
                        # Use try-except-finally
                        send_json()
                        reconnect = False
                    
                    #ifdef obj
                    send_json(csv_to_json(csvf, break_loop)) # Comment if it does not work correctly
                    #endif
            else:
                reconnect = True             
    print("Thread ID: #{} is shutting down.\n".format(threadID))

if "__main__" == __name__:
    try:
        _thread.start_new_thread(process_data, DATA_LISTENER)
        _thread.start_new_thread(send_data, PING_LISTENER)
    except:
        print("An error has occurred while attempting to start threads...\n")

"""
Made by: Felix M. Perez Quinones
"""