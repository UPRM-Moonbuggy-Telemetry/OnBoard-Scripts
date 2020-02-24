import json

from serial import Serial
from datetime import datetime
from radiodata.radiodata import RadioData

# import serial.tools.list_ports as ports


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def send_json(obj: RadioData):
    port = '/dev/ttyACM0'
    br = 9600

    ser = Serial(port, baudrate=br, timeout=1)

    timestamp = datetime.now().strftime("%Y-%b-%d;%I:%M:%S:%p").split(';')
    obj.OBC_date = timestamp.pop(0)
    obj.OBC_time = timestamp.pop(0)

    data_to_send = obj.get_data_dict()

    data = json.dumps(data_to_send, cls=MyEncoder)
    ser.write(data.encode('utf-8'))
    # ser.flush()


if '__main__' == __name__:
    # for port in list(ports.comports()):
    #     print(port)
    dummy = RadioData({})
    send_json(dummy)

