import random as rnd
import time as t

from datetime import date as d
from radiodata.radiodata import RadioData
from .data_to_csv import data_to_csv


def generate_random_data():
    data = [
        rnd.randint(0, 100),    # strain_front_lft_1
        rnd.randint(0, 100),    # strain_front_lft_2
        rnd.randint(0, 100),    # strain_front_lft_3
        rnd.randint(0, 100),    # strain_front_rt_1
        rnd.randint(0, 100),    # strain_front_rt_2
        rnd.randint(0, 100),    # strain_front_rt_3
        rnd.randint(0, 100),    # strain_center_1
        rnd.randint(0, 100),    # strain_center_2
        rnd.randint(0, 100),    # strain_center_3
        rnd.randint(0, 100),    # vibration_front_lft
        rnd.randint(0, 100),    # vibration_front_rt
        rnd.randint(0, 100),    # vibration_rear_lft
        rnd.randint(0, 100),    # vibration_rear_rt
        rnd.randint(0, 100),    # vibration_center
        rnd.randint(0, 100),    # battery_status
    ]
    return data


def generate_random_positions():
    return [
        rnd.uniform(0, 100),    # latitude
        rnd.uniform(0, 100)     # longitude
    ]


if __name__ == "__main__":
    filename = "buggyData.csv"
    dataObj = RadioData(generate_random_data(), generate_random_positions())
    dataObj.OBC_date = d.today()
    dataObj.OBC_time = t.ctime().split()[3]
    data_to_csv(dataObj, filename)
