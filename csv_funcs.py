import csv
from io import TextIOWrapper
import random as rnd
import os.path
import json

from os import close, path

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

def csv_to_json(csvFile: TextIOWrapper, break_loop):
    # Open the DataLog.csv (don't close it nevel)
    # Reads the lines as they are updated in order

    """
    Use a buffer file and a backup log file.
    Append to the buffer until disconnection,
    then the buffer is overwritten and then 
    appended until another disconnection, if any.
    """
    csv_rows = csv.DictReader(csvFile,fieldnames=None)
    next_csv_row = None

    if(csv_rows.__next__().__next__() != None):
        next_csv_row = csv_rows.__next__()
    else: 
        #Read from current line to line before eof
        next_csv_row = csv_rows.__next__()
        csvFile.close()
        break_loop = False
        

    return json.dumps(next_csv_row), break_loop
    # return json_list