import csv
import csv_funcs

from radiodata import RadioData

"""
    This is the function that will produce the
    CSV which will be used to generate the dataloss
    queue.
"""

# This is the main function of the Radio-to-CSV script. 
# It writes the data given by a RadioData object into a CSV file with the given name.
def data_to_csv(data_obj: RadioData, filename: str):

    # Creating a new CSV if there doesn't exist one
    if not csv_funcs.exists_csv(filename):
        csv_funcs.create_csv_file(filename, data_obj.get_fieldnames()) 

    # Writing to the CSV
    csv_funcs.write_to_csv(filename, csv_funcs.randomize_data(data_obj.get_data_dict()))
    # We can turn this csv into a JSON and just return it
    # 2 line change: CSV --> JSON conversion and return JSON (to be used by send_json)


""" 
To-Do:
    -> (NOPE) add memory management side (set max. csv data lines, )
        - set max. csv data lines
        - move csv to storage
        - create new csv

"""