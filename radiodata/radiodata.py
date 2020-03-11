class RadioData:

    # This is the global data structure used to store radio-transmitted data across the system.

    FIELDNAMES = [
        "strain_front_lft_1",
        "strain_front_lft_2",
        "strain_front_lft_3",
        "strain_front_rt_1",
        "strain_front_rt_2",
        "strain_front_rt_3",
        "strain_center_1",
        "strain_center_2",
        "strain_center_3",
        "vibration_front_lft",
        "vibration_front_rt",
        "vibration_rear_lft",
        "vibration_rear_rt",
        "vibration_center",
        "battery_status",

        "latitude",
        "longitude",
        "OBC_time",
        "OBC_date",
        "GSC_time",
        "GSC_date",
    ]

    def __init__(self, data_list: list, gps_list: list):
        """
        RadioData constructor.
        :param data_list: contains all the data from the sensors except OBC and GSC timestamps.
                            Assuming data_list is of length 15 and values in same order as FIELDNAMES.
        :param gps_list: contains latitude and longitude in that order.
        """
        # Strain sensors
        self.strain_front_lft_1 = int(data_list[0])
        self.strain_front_lft_2 = int(data_list[1])
        self.strain_front_lft_3 = int(data_list[2])

        self.strain_front_rt_1 = int(data_list[3])
        self.strain_front_rt_2 = int(data_list[4])
        self.strain_front_rt_3 = int(data_list[5])

        self.strain_center_1 = int(data_list[6])
        self.strain_center_2 = int(data_list[7])
        self.strain_center_3 = int(data_list[8])

        # Vibration sensors
        self.vibration_front_lft = int(data_list[9])
        self.vibration_front_rt = int(data_list[10])

        self.vibration_rear_lft = int(data_list[11])
        self.vibration_rear_rt = int(data_list[12])

        self.vibration_center = int(data_list[13])

        # Battery
        self.battery_status = int(data_list[14])

        # GPS
        self.latitude = float(gps_list[0])
        self.longitude = float(gps_list[1])

        # On board computer
        self.OBC_time = ""
        self.OBC_date = ""

        # Ground station computer
        self.GSC_time = ""
        self.GSC_date = ""

    @staticmethod
    def get_fieldnames() -> list:
        return RadioData.FIELDNAMES

    def get_data_dict(self) -> dict:
        return self.__dict__
