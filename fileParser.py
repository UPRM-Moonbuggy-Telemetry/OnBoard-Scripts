import csv, time as t
from datetime import date as d


def fileParser(file_path):
    json_list = []
    with open(file_path) as csv_file:
        csv_rows = csv.reader(csv_file, delimiter=',')
        for row in csv_rows:
            row_list = list(row)
            date = d.today()
            time = t.ctime().split()[3]
            json = {
                "strain_sensor_1": int(row_list[0]),
                "strain_sensor_2": int(row_list[1]),
                "strain_sensor_3": int(row_list[2]),
                "strain_sensor_4": int(row_list[3]),
                "vibration_sensor_1": int(row_list[4]),
                "vibration_sensor_2": int(row_list[5]),
                "vibration_sensor_3": int(row_list[6]),
                "vibration_sensor_4": int(row_list[7]),
                "vibration_sensor_5": int(row_list[8]),
                "battery_status": int(row_list[9]),
                "latitude": float(row_list[10]),
                "longitude": float(row_list[11]),
                "OBC_time": time,
                "OBC_date": date
             }
            json_list.append(json)
        return json_list
