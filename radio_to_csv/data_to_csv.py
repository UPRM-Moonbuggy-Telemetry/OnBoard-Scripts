from .csv_funcs import create_csv_file, exists_csv, write_to_csv, randomize_data
from radiodata.radiodata import RadioData


# This is the main function of the Radio-to-CSV script. 
# It writes the data given by a RadioData object into a CSV file with the given name.
def data_to_csv(data_obj: RadioData, filename: str):

    # Creating a new CSV if there doesn't exist one
    if not exists_csv(filename):
        create_csv_file(filename, data_obj.get_fieldnames())

    # Writing to the CSV
    # (For loop is there for testing purposes; script will only add one data row per call)
    # for i in range(5):
    write_to_csv(filename, randomize_data(data_obj.get_data_dict()))


""" 
To-Do:
    -> (DONE) create package for RadioData
    -> (DONE) Documentation
    -> (NOPE) add memory management side (set max. csv data lines, )
        - set max. csv data lines
        - move csv to storage
        - create new csv

"""