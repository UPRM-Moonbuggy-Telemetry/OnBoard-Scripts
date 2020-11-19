import Pre_Processor
import serial
import serial.tools.list_ports
# Maybe implement this to return a list
# of all available serial ports connected

#import time
import RPi.GPIO as GPIO
import pynmea2 #Download pynmea2 on raspberry pi being used
from radiodata.radiodata import RadioData
from data_to_csv import data_to_csv
from serializeObjects import send_json
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

def setup(): 
    arduino = serial.Serial('COM5', 9600) #Replace 'COM' port for 'ttyACM*some number*' when not using windows
    GPIO.setmode(GPIO.BOARD)
    decoded_data = None
    GPS_Input = GPIO.setup(8, input)

#   print(arduino)
    while True:
        # data refers to direct arduino reads
        data = arduino.readline()

        # We flag for signal, True = connected
        flag = True # serial.read() # Serial read from groundstation
        # Possibly neeed to set it to the same port?
        # What happens if read doesnt read? Does it stay hanging??
        # Make sure read returns atleast garbage values and not hangs.
        # Does serial.read() read from any source?? Is there a way to make it a specific read???

        # reconnect flags for specific behavior once reconnection happens
        reconnect = False

        # Assume 'data' is true when signal is not lost and is receiving data
        if data:
            decoded_data = data.decode("utf-8")
            cleaned_data_list, gps_data_list = parser(decoded_data, GPS_Input)
            obj = RadioData(cleaned_data_list, gps_data_list) # Creates object of type RadioData with parsed data lists // Comment if it does not work correctly
            data_to_csv(obj, "DataLog.csv") # Comment if it does not work correctly
            # Keep local CSV file that is appended so that data loss is prevented in case of signal loss.

        
        if flag:
#           print(data.decode("utf-8"))

            # Prototype functionality for disconection and reconnection
            # Assuming existing functions
            if reconnect:
                # Create function "local_upload" to upload local data log
                # Implement multithreading to prevent data back ups
                # Use try-except-finally
                send_json(csv_to_json("DataLog_Local.csv"))
                reconnect = False
            
            #ifdef obj
            send_json(obj) # Comment if it does not work correctly
            #endif

        else:
            reconnect = True
            # Buffer log for data collected during disconnection
            if data:
                data_to_csv(obj, "DataLog_Local.csv")
            # Does not send JSON package due to signal loss
            
        
 
if "__main__" == __name__:
    setup()

"""
Made by: Felix M. Perez Quinones
"""