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


def full_name_list(df):
    """
    Prints a list with all the full names.
    """
    full_name = (df['First Name'] + ' ' + df['Last Name']).tolist()
    full_name_clean = sorted([x for x in full_name if str(x) != 'nan'])
    print('Full name list of all the clients: ')
    print(full_name_clean, "\n")


def jobs_list(df):
    """
    Prints a list of all the different Jobs in the data.
    Duplicated jobs would be repeated in the list.
    """
    jobs = df['Job'].tolist()
    jobs_clean = sorted([x for x in jobs if str(x) != 'nan'])
    print('Job list of all the clients: ')
    print(jobs_clean)


def main():
    """
    Main function that calls all the other functions
    """
    data = read_file()
    full_name_list(data)
    jobs_list(data)


main()
