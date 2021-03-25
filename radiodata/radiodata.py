class RadioData:

    # This is the global data structure used to store radio-transmitted data across the system.
    from env_variables import BUGGY_ID

    FIELDNAMES_NEW = [
        "strain_center_front_1", # Vertical 
        "strain_center_front_2", # Horizontal
        "strain_center_front_3", # 45 degree
        "strain_center_back_1", # Vertical
        "strain_center_back_2", # Horizontal
        "strain_center_back_3", # 45 degree
        "strain_backseat_1",
        "strain_backseat_2",
        "strain_backseat_3",
        "vibration_front_lft",
        "vibration_front_rt",
        "vibration_rear_lft",
        "vibration_rear_rt",
        "vibration_center_back",
        "battery_status",

        "latitude",
        "longitude",
        "OBC_time",
        "OBC_date",
        "GSC_time",
        "GSC_date",

        # Include speed from hall effect sensors
        # Formula for hall effect sensors: linear speed = radius x angular speed = r*2*π*(RPM)/60
        
        # Add extra sensor fieldnames at the end 
        # of the dictionary. That way if there are 
        # missing sensors, it will display a blank field.
        # If using old buggy, those "new" fields are blank,
        # only "filled" when using new buggy with the extra
        # sensors.
    ]

    FIELDNAMES_OLD = [
        "strain_center_front_1", # Vertical 
        "strain_center_front_2", # Horizontal
        "strain_center_front_3", # 45 degree
        "strain_center_back_1", # Vertical
        "strain_center_back_2", # Horizontal
        "strain_center_back_3", # 45 degree
        "strain_frontseat_1",
        "strain_frontseat_2",
        "strain_frontseat_3",
        "vibration_backseat_top",
        "vibration_backseat_bottom",
        "vibration_front_right",
        "vibration_front_left",
        "battery_status",

        "latitude",
        "longitude",
        "OBC_time",
        "OBC_date",
        "GSC_time",
        "GSC_date",

    ]

    def __init__(self, data_list: list, gps_list: list, BUGGY_ID):
        """
        RadioData constructor.
        :param data_list: contains all the data from the sensors except OBC and GSC timestamps.
                            Assuming data_list is of length 15 and values in same order as FIELDNAMES.
        :param gps_list: contains latitude and longitude in that order.
        """
        if(BUGGY_ID):
            
            # Strain sensors
            self.strain_center_front_1 = float(data_list[0]) # Changed to float
            """
            self.strain_center_front_2 = float(data_list[1]) # Changed to float
            self.strain_center_front_3 = float(data_list[2]) # Changed to float

            self.strain_center_back_1 = float(data_list[3]) # Changed to float
            self.strain_center_back_2 = float(data_list[4]) # Changed to float
            self.strain_center_back_3 = float(data_list[5]) # Changed to float

            self.strain_backseat_1 = float(data_list[6]) # Changed to float
            self.strain_backseat_2 = float(data_list[7]) # Changed to float
            self.strain_backseat_3 = float(data_list[8]) # Changed to float

            # Vibration sensors
            self.vibration_front_lft = float(data_list[9])
            self.vibration_front_rt = float(data_list[10])

            self.vibration_rear_lft = float(data_list[11])
            self.vibration_rear_rt = float(data_list[12])

            self.vibration_center_back = float(data_list[13])

            # Battery
            self.battery_status = float(data_list[14]) # Changed to float
            
            # GPS
            self.latitude = float(gps_list[0])
            self.longitude = float(gps_list[1])
            """
            # Include speed from hall effect sensors

            # On board computer
            self.OBC_time = ""
            self.OBC_date = ""

            # Ground station computer
            self.GSC_time = ""
            self.GSC_date = ""

        else:
            # Strain sensors
            self.strain_center_front_1 = float(data_list[0]) # Changed to float
            self.strain_center_front_2 = float(data_list[1]) # Changed to float
            self.strain_center_front_3 = float(data_list[2]) # Changed to float

            self.strain_center_back_1 = float(data_list[3]) # Changed to float
            self.strain_center_back_2 = float(data_list[4]) # Changed to float
            self.strain_center_back_3 = float(data_list[5]) # Changed to float

            self.strain_frontseat_1 = float(data_list[6]) # Changed to float
            self.strain_frontseat_2 = float(data_list[7]) # Changed to float
            self.strain_frontseat_3 = float(data_list[8]) # Changed to float

            # Vibration sensors
            self.vibration_backseat_top = float(data_list[9])
            self.vibration_backseat_bottom = float(data_list[10])

            self.vibration_front_right = float(data_list[11])
            self.vibration_front_left = float(data_list[12])

            # Battery
            self.battery_status = float(data_list[13]) # Changed to float
            
            # GPS
            self.latitude = float(gps_list[0])
            self.longitude = float(gps_list[1])

            # Include speed from hall effect sensors

            # On board computer
            self.OBC_time = ""
            self.OBC_date = ""

            # Ground station computer
            self.GSC_time = ""
            self.GSC_date = ""

    @staticmethod
    def get_fieldnames(BUGGY_ID) -> list:
        if(BUGGY_ID):
            return RadioData.FIELDNAMES_NEW
        else:
            return RadioData.FIELDNAMES_OLD

    def get_data_dict(self) -> dict:
        return self.__dict__
