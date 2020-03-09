import serial
import serial.tools.list_ports
import time

def parser(Data_String):
"""
    data_types = Data_string.split(':')
    Data_String = data_types[0]
    GPS_string = data_types[1]
"""
    Data_List = Data_String.split(',')
#    GPS_List = GPS_parser(GPS_string)
    
    for i in range(len(Data_List)):
        Data_List[i] = Data_List[i].strip()

    return Data_List, GPS_List

def GPS_parser(GPS_String):
    GPS_info_list = GPS_String.split(' ')
    for i in range(len(GPS_info_list)):
        GPS_info_list = GPS_info_list[i].strip()
    return GPS_info_list

def setup():

      arduino =serial.Serial('COM5',9600)
      decoded_data = None
#      print(arduino)
      while True:
#          data = int(arduino.readline())
          data = arduino.readline()
          if data:
#          print(data.decode("utf-8"))
              decoded_data = data.decode("utf-8")
              cleaned_data_sensors, gps_data = parser(decoded_data)
              #obj = Buggy(cleaned_data, gps_data)
              #csv_reader(obj)
              #send_json(obj)
 
if "__main__" == __name__:
    setup()

"""
Made by: Felix M. Perez Quinones
"""