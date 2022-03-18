import os

import pandas as pd


def input_data(Relative_PATH: str) -> pd.DataFrame:
    """
    args: relative_path: str
    return: csv_data: pd.DataFrame
    """
    Current_Path = os.getcwd()
    PATH = Current_Path + Relative_PATH
    CSV_DATA = pd.read_csv(PATH)
    return CSV_DATA
