import os

import pandas as pd


def get_input_csv_data(relative_path: str = "/input/input.xlsx") -> pd.DataFrame:
    """
    read input file: 入力ファイルの読み込み

    Parameters
    ----------
    relative_path : str
        相対パス

    Returns
    -------
    pd.DataFrame
        入力データ
    """
    CURRENT_PATH: str = os.getcwd()
    PATH = CURRENT_PATH + relative_path

    try:
        CSV_DATA = pd.read_excel(PATH)
    except FileNotFoundError:
        CSV_DATA = pd.read_csv(CURRENT_PATH + "/input/input.csv")

    return CSV_DATA
