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
    except Exception:
        print('Error, the file could not be loaded')


def exception_handling(df):
    """
    Handles the exceptions:
    Exceptions considered are:
    - Blank rows
    - Row with at least 1 NaN argument
    """
    list_of_blank_rows = df.index[df.isnull().all(axis=1)].tolist()

    if len(list_of_blank_rows) != 0:
        print(
            f'The data contains {len(list_of_blank_rows)} blank row(s).\n'
            f'The index(es):  {list_of_blank_rows}\n'
        )
    df.dropna(axis=0, how='all', inplace=True)

    # Exception handling for requiered rows
    req_rows = df[['Street', 'Zip', 'City', 'Last Check-In Date', 'Company']]
    req_rows_with_nan = df.index[req_rows.isna().any(axis=1)].tolist()
    if len(req_rows_with_nan) != 0:
        print(
            f'The data contains {len(req_rows_with_nan)} row(s)'
            ' with NaN values in the requiered fields.\n'
            f'The index(es):  {req_rows_with_nan}\n'
        )
    
    # Exception handling for non-requiered rows
    other_rows = df[['First Name', 'Last Name', 'Type', 'Job', 'Phone']]
    other_rows_with_nan = df.index[other_rows.isna().any(axis=1)].tolist()
    if len(other_rows_with_nan) != 0:
        print(
            f'The data contains {len(other_rows_with_nan)} row(s)'
            ' with NaN values in the non-requiered fields.\n'
            f'The index(es):  {other_rows_with_nan}\n'
        )
    df.dropna(axis=0, how='any', inplace=True)
    return df


def check_in_dates(df):
    """
    Prints the user's which have the earliest and latest check
    in date.
    Converts the columns 'Check-in Datetime' values into
    DateTime objects (Originally str)
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
    raw_data = read_file()
    clean_data = exception_handling(raw_data)
    check_in_dates(clean_data)
    full_name_list(clean_data)
    jobs_list(clean_data)


main()
