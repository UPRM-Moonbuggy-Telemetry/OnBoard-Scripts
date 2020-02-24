class RadioData:

    FIELDNAMES = {
        "ID": "id",
        "STRAIN_1": "strain_sensor_1",
        "STRAIN_2": "strain_sensor_2",
        "STRAIN_3": "strain_sensor_3",
        "STRAIN_4": "strain_sensor_4",
        "VIBRATION_1": "vibration_sensor_1",
        "VIBRATION_2": "vibration_sensor_2",
        "VIBRATION_3": "vibration_sensor_3",
        "VIBRATION_4": "vibration_sensor_4",
        "VIBRATION_5": "vibration_sensor_5",
        "BATTERY": "battery_status",
        "LATITUDE": "latitude",
        "LONGITUDE": "longitude",
        "OBC_TIME": "OBC_time",
        "OBC_DATE": "OBC_date",
    }

    def __init__(self, data_dict: dict):
        self.id = data_dict[RadioData.FIELDNAMES['ID']]
        self.strain_sensor_1 = data_dict[RadioData.FIELDNAMES['STRAIN_1']]
        self.strain_sensor_2 = data_dict[RadioData.FIELDNAMES['STRAIN_2']]
        self.strain_sensor_3 = data_dict[RadioData.FIELDNAMES['STRAIN_3']]
        self.strain_sensor_4 = data_dict[RadioData.FIELDNAMES['STRAIN_4']]
        self.vibration_sensor_1 = data_dict[RadioData.FIELDNAMES['VIBRATION_1']]
        self.vibration_sensor_2 = data_dict[RadioData.FIELDNAMES['VIBRATION_2']]
        self.vibration_sensor_3 = data_dict[RadioData.FIELDNAMES['VIBRATION_3']]
        self.vibration_sensor_4 = data_dict[RadioData.FIELDNAMES['VIBRATION_4']]
        self.vibration_sensor_5 = data_dict[RadioData.FIELDNAMES['VIBRATION_5']]
        self.battery_status = data_dict[RadioData.FIELDNAMES['BATTERY']]
        self.latitude = data_dict[RadioData.FIELDNAMES['LATITUDE']]
        self.longitude = data_dict[RadioData.FIELDNAMES['LONGITUDE']]
        self.OBC_time = data_dict[RadioData.FIELDNAMES['OBC_TIME']]
        self.OBC_date = data_dict[RadioData.FIELDNAMES['OBC_DATE']]

    def updateData(self, data_dict: dict):
        self.id = data_dict[RadioData.FIELDNAMES['ID']]
        self.strain_sensor_1 = data_dict[RadioData.FIELDNAMES['STRAIN_1']]
        self.strain_sensor_2 = data_dict[RadioData.FIELDNAMES['STRAIN_2']]
        self.strain_sensor_3 = data_dict[RadioData.FIELDNAMES['STRAIN_3']]
        self.strain_sensor_4 = data_dict[RadioData.FIELDNAMES['STRAIN_4']]
        self.vibration_sensor_1 = data_dict[RadioData.FIELDNAMES['VIBRATION_1']]
        self.vibration_sensor_2 = data_dict[RadioData.FIELDNAMES['VIBRATION_2']]
        self.vibration_sensor_3 = data_dict[RadioData.FIELDNAMES['VIBRATION_3']]
        self.vibration_sensor_4 = data_dict[RadioData.FIELDNAMES['VIBRATION_4']]
        self.vibration_sensor_5 = data_dict[RadioData.FIELDNAMES['VIBRATION_5']]
        self.battery_status = data_dict[RadioData.FIELDNAMES['BATTERY']]
        self.latitude = data_dict[RadioData.FIELDNAMES['LATITUDE']]
        self.longitude = data_dict[RadioData.FIELDNAMES['LONGITUDE']]
        self.OBC_time = data_dict[RadioData.FIELDNAMES['OBC_TIME']]
        self.OBC_date = data_dict[RadioData.FIELDNAMES['OBC_DATE']]

    @staticmethod
    def get_fieldnames():
        return RadioData.FIELDNAMES.values()

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
