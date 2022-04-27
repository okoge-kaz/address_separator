import os

import pandas as pd


def create_output_data(formated_dictionary_data: dict, relative_path: str = "/output/output.csv") -> None:
    """
    create output file: 出力ファイルの作成

    Parameters
    ----------
    formated_dictionary_data : dict
        整形済みの辞書データ
    Relative_PATH : str
        相対パス

    Returns
    -------
        void
    """
    CURRENT_PATH: str = os.getcwd()
    PATH = CURRENT_PATH + relative_path

    output_data: pd.DataFrame = pd.DataFrame(formated_dictionary_data)

    output_data.to_csv(PATH, encoding="utf-8_sig")
