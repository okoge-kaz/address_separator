import os

import pandas as pd


def get_input_csv_data(Relative_PATH: str = "/input/input.xlsx") -> pd.DataFrame:
    """
    args: relative_path: str
    return: csv_data: pd.DataFrame
    """
    Current_Path = os.getcwd()
    PATH = Current_Path + Relative_PATH
    try:
        CSV_DATA = pd.read_excel(PATH)
    except FileNotFoundError:
        CSV_DATA = pd.read_csv(Current_Path + "/input/input.csv")
    return CSV_DATA
