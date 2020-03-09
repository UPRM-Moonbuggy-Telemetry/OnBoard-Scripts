import json

from serial import Serial
from datetime import datetime
from radiodata.radiodata import RadioData
from radio_to_csv.csv_script_test import generate_random_positions, generate_random_data
from env_variables import BUGGY_ID, SEND_JSON_PORT, BAUDRATE

# import serial.tools.list_ports as ports


def get_buggy_name_by_id(pk):
    return "NewBuggy" if pk == 1 else "OldBuggy"


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def send_json(obj: RadioData):
    ser = Serial(SEND_JSON_PORT, baudrate=BAUDRATE, timeout=1)

    timestamp = datetime.now().strftime("%Y-%b-%d;%I:%M:%S:%p").split(';')
    obj.OBC_date = timestamp.pop(0)
    obj.OBC_time = timestamp.pop(0)

    data_to_send = {"data": obj.get_data_dict(), "buggy_name": get_buggy_name_by_id(BUGGY_ID)}

    data = json.dumps(data_to_send, cls=MyEncoder)
    ser.write(data.encode('utf-8'))
    # ser.flush()
    ser.close()


if __name__ == '__main__':
    # for port in list(ports.comports()):
    #     print(port)
    dummy_obj = RadioData(generate_random_data(), generate_random_positions())
    dummy_obj.OBC_date, dummy_obj.OBC_time = datetime.now().strftime("%Y-%b-%d;%I:%M:%S:%p").split(';')
    send_json(dummy_obj)
