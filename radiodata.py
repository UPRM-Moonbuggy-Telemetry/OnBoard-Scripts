class RadioData():

    # This is the global data structure used to store radio-transmitted data across the system.

    def __init__(self, data_dict = None):
        # The object can be initialized either manually or by an input dictionary.
        if(data_dict != None):
            for data in data_dict:
                setattr(self, data, data_dict[data])
        else:
            self.buggyId = None
            self.strain_front_lft_1 = None
            self.strain_front_lft_2 = None
            self.strain_front_lft_3 = None
            self.strain_front_rt_1 = None
            self.strain_front_rt_2 = None
            self.strain_front_rt_3 = None
            self.strain_center_1 = None
            self.strain_center_2 = None
            self.strain_center_3 = None
            self.vibration_front_lft = None
            self.vibration_front_rt = None
            self.vibration_rear_lft = None
            self.vibration_rear_rt = None
            self.vibration_center = None
            self.battery_status = None
            self.latitude = None
            self.longitude = None
            self.GSC_time = None
            self.GSC_date = None
            self.OBC_time = None
            self.OBC_date = None


        # All RadioData objects will have a fieldnames list attribute
        self.fieldnames = ['buggyId', 'strain_front_lft_1', 'strain_front_lft_2','strain_front_lft_3',
                            'strain_front_rt_1', 'strain_front_rt_2', 'strain_front_rt_3', 
                            'strain_center_1', 'strain_center_2', 'strain_center_3', 
                            'vibration_front_lft', 'vibration_front_rt', 'vibration_rear_lft', 
                            'vibration_rear_rt', 'vibration_center', "battery_status", "latitude", 
                            "longitude", 'GSC_time', 'GSC_date', "OBC_time", "OBC_date"]

    # This method is used to update the object's data with a given dict.
    # (CONSTAINT: The keys of the parameter dict must be EQUAL to the object's fieldnames.)
    def updateData(self, data_dict: dict):
        try:
            # for data in data_dict:
            #     setattr(self, data, data_dict[data])

            self.buggyId = data_dict.buggyId
            self.strain_front_lft_1 = data_dict.strain_front_lft_1
            self.strain_front_lft_2 = data_dict.strain_front_lft_2
            self.strain_front_lft_3 = data_dict.strain_front_lft_3
            self.strain_front_rt_1 = data_dict.strain_front_rt_1
            self.strain_front_rt_2 = data_dict.strain_front_rt_2
            self.strain_front_rt_3 = data_dict.strain_front_rt_3
            self.strain_center_1 = data_dict.strain_center_1
            self.strain_center_2 = data_dict.strain_center_2
            self.strain_center_3 = data_dict.strain_center_3
            self.vibration_front_lft = data_dict.vibration_front_lft
            self.vibration_front_rt = data_dict.vibration_front_rt
            self.vibration_rear_lft = data_dict.vibration_rear_lft
            self.vibration_rear_rt = data_dict.vibration_rear_rt
            self.vibration_center = data_dict.vibration_center
            self.battery_status = data_dict.battery_status
            self.latitude = data_dict.latitude
            self.longitude = data_dict.longitude
            self.GSC_time = data_dict.GSC_time
            self.GSC_date = data_dict.GSC_date
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
            'buggyId': self.buggyId,
            'strain_front_lft_1': self.strain_front_lft_1,
            'strain_front_lft_2': self.strain_front_lft_2,
            'strain_front_lft_3': self.strain_front_lft_3,
            'strain_front_rt_1': self.strain_front_rt_1,
            'strain_front_rt_2': self.strain_front_rt_2,
            'strain_front_rt_3': self.strain_front_rt_3,
            'strain_center_1': self.strain_center_1,
            'strain_center_2': self.strain_center_2,
            'strain_center_3': self.strain_center_3,
            'vibration_front_lft': self.vibration_front_lft,
            'vibration_front_rt': self.vibration_front_rt,
            'vibration_rear_lft': self.vibration_rear_lft,
            'vibration_rear_rt': self.vibration_rear_rt,
            'vibration_center': self.vibration_center,
            'battery_status': self.battery_status,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'GSC_time': self.GSC_time,
            'GSC_date': self.GSC_date,
            'OBC_time': self.OBC_time,
            'OBC_date': self.OBC_date
        }

        return data_dict
