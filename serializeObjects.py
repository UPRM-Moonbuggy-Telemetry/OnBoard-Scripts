import json

from serial import Serial
from datetime import datetime

# import serial.tools.list_ports as ports


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def send_json(obj):
    port = '/dev/ttyACM0'
    br = 9600

    ser = Serial(port, baudrate=br, timeout=1)

    data_to_send = {"data": obj.__dict__, "timestamp": datetime.now().strftime("%Y-,%b-%d;%I:%M:%S:%p")}

    data = json.dumps(data_to_send, cls=MyEncoder)
    ser.write(data.encode('utf-8'))
    # ser.flush()


class Dummy:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if '__main__' == __name__:
    # for port in list(ports.comports()):
    #     print(port)
    obj = Dummy(name="Everson", age=21)
    send_json(obj)

