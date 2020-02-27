import csv
import random as rnd

from os import path


# This function creates a new CSV file with the given name, and adds a header containing the given fields.
def create_csv_file(filename: str, fields: list):
    with open(filename, 'a', newline='') as csvDataFile:
        dictwriter = csv.DictWriter(csvDataFile, fieldnames=fields)
        dictwriter.writeheader()


# This function checks if there already exists a CSV file with the given name.
# (It's used to avoid errors thrown by reading from empty files.)
def exists_csv(filename: str) -> bool:
    return path.exists(filename)


# This function appends a row of data from the given dict to the CSV file with the given name.
def write_to_csv(filename: str, data: dict):
    with open(filename, 'a', newline='') as csvDataFile:
        fileWriter = csv.writer(csvDataFile)
        fileWriter.writerow(data.values())


# This function randomizes the continuous data values of a given radio data dict.
# (FOR TESTING PURPOSES)
def randomize_data(data: dict) -> dict:
    for key in data.keys():
        if key != "OBC_time" or key != "OBC_date":
            data[key] = rnd.randint(0, 100)
    return data
