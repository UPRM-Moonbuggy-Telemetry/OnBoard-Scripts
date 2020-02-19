class RadioData():

    def __init__(self, data_dict = None):
        if(data_dict != None):
            for data in data_dict:
                setattr(self, data, data_dict[data])
        else:
            self.id = None
            self.strain_sensor_1 = None
            self.strain_sensor_2 = None
            self.strain_sensor_3 = None
            self.strain_sensor_4 = None
            self.vibration_sensor_1 = None
            self.vibration_sensor_2 = None
            self.vibration_sensor_3 = None
            self.vibration_sensor_4 = None
            self.vibration_sensor_5 = None
            self.battery_status = None
            self.latitude = None
            self.longitude = None
            self.OBC_time = None
            self.OBC_date = None

        self.fieldnames = ["id", "strain_sensor_1", "strain_sensor_2", "strain_sensor_3",
                            "strain_sensor_4", "vibration_sensor_1", "vibration_sensor_2",
                            "vibration_sensor_3", "vibration_sensor_4", "vibration_sensor_5",
                            "battery_status", "latitude", "longitude", "OBC_time", "OBC_date"]


    def updateData(self, data_dict: dict):
        self.id = data_dict.id
        self.strain_sensor_1 = data_dict.strain_sensor_1
        self.strain_sensor_2 = data_dict.strain_sensor_2
        self.strain_sensor_3 = data_dict.strain_sensor_3
        self.strain_sensor_4 = data_dict.strain_sensor_4
        self.vibration_sensor_1 = data_dict.vibration_sensor_1
        self.vibration_sensor_2 = data_dict.vibration_sensor_2
        self.vibration_sensor_3 = data_dict.vibration_sensor_3
        self.vibration_sensor_4 = data_dict.vibration_sensor_4
        self.vibration_sensor_5 = data_dict.vibration_sensor_5
        self.battery_status = data_dict.battery_status
        self.latitude = data_dict.latitude
        self.longitude = data_dict.longitude
        self.OBC_time = data_dict.OBC_time
        self.OBC_date = data_dict.OBC_date

    def get_fieldnames(self) -> list:
        return self.fieldnames

    def get_data_dict(self) -> dict:
        data_dict = {
                "id": self.id,
                "strain_sensor_1": self.strain_sensor_1,
                "strain_sensor_2": self.strain_sensor_2,
                "strain_sensor_3": self.strain_sensor_3,
                "strain_sensor_4": self.strain_sensor_4,
                "vibration_sensor_1": self.vibration_sensor_1,
                "vibration_sensor_2": self.vibration_sensor_2,
                "vibration_sensor_3": self.vibration_sensor_3,
                "vibration_sensor_4": self.vibration_sensor_4,
                "vibration_sensor_5": self.vibration_sensor_5,
                "battery_status": self.battery_status,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "OBC_time": self.OBC_time,
                "OBC_date": self.OBC_date
        }

        return data_dict
