class RadioData():

    # This is the global data structure used to store radio-transmitted data across the system.

    def __init__(self, data_dict = None):
        # The object can be initialized either manually or by an input dictionary.
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

        # All RadioData objects will have a fieldnames list attribute
        self.fieldnames = ["id", "strain_sensor_1", "strain_sensor_2", "strain_sensor_3",
                            "strain_sensor_4", "vibration_sensor_1", "vibration_sensor_2",
                            "vibration_sensor_3", "vibration_sensor_4", "vibration_sensor_5",
                            "battery_status", "latitude", "longitude", "OBC_time", "OBC_date"]

    # This method is used to update the object's data with a given dict.
    # (CONSTAINT: The keys of the parameter dict must be EQUAL to the object's fieldnames.)
    def updateData(self, data_dict: dict):
        try:
            # for data in data_dict:
            #     setattr(self, data, data_dict[data])

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
        except:
            print("Dict does not coincide with object fieldnames.")

    # This method returns the object's fieldnames list.
    def get_fieldnames(self) -> list:
        return self.fieldnames

    # This method returns a dictionary of the data stored in the RadioData object.
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
