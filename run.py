import pandas as pd
from datetime import datetime


def read_file():
    """
    Assumes the file containing the data is called 'data.csv'
    and is in a csv file.
    """
    try:
        file_name = 'data.csv'
        df = pd.read_csv(file_name)
        return df
    except NameError:
        print('Error, the file could not be loaded')


def main():
    """
    Main function that calls all the other functions
    """
    data = read_file()
    print(data)

main()
