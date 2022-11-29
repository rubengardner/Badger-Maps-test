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


def check_in_dates(df):
    """
    Prints the users wich have the earliest and latest check
    in date.
    Converts the columns 'Check-in Datetime' values into
    datetime objects (Originally str)
    """
    df['Check-in Datetime'] = pd.to_datetime(
        df['Last Check-In Date'], dayfirst=True, format="%d/%m/%Y"
        )
    user_min = df.loc[df['Check-in Datetime'] == df['Check-in Datetime'].min()]
    user_max = df.loc[df['Check-in Datetime'] == df['Check-in Datetime'].max()]
    print(
        "Earliest check in date: \n"
        f"{user_min['First Name'].iloc[0]} "
        f"{user_min['Last Name'].iloc[0]}, "
        f"{user_min['Check-in Datetime'].iloc[0].strftime('%d/%m/%Y')}\n"
    )
    print(
        "Latest check in date:\n"
        f"{user_max['First Name'].iloc[0]} "
        f"{user_max['Last Name'].iloc[0]}, "
        f"{user_max['Check-in Datetime'].iloc[0].strftime('%d/%m/%Y')}\n"
    )


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
    check_in_dates(data)
    full_name_list(data)
    jobs_list(data)


main()
