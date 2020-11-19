# Directory: radio_to_csv/csv_funcs.py

$ Methods:
- create_csv_file(filename: str, fields: list): 
    This function creates a new CSV file with the given name, 
    and adds a header containing the given fields.

- exists_csv(filename: str) -> bool:
    This function checks if there already exists a CSV 
    file with the given name. (It's used to avoid errors 
    thrown by reading from empty files.)

- write_to_csv(filename: str, data: dict):
    This function appends a row of data from the given dict to 
    the CSV file with the given name.

- randomize_data(data: dict) -> dict:
    This function randomizes the continuous data values of a given 
    radio data dict. (FOR TESTING PURPOSES)

# Directory: radio_to_csv/data_to_csv.py

$ Methods:
- data_to_csv(data_obj: RadioData, filename: str):
    This is the main function of the Radio-to-CSV script.
    It writes the data given by a RadioData object into a 
    CSV file with the given name.
