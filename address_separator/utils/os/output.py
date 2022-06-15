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

    en_output_data: pd.DataFrame = pd.DataFrame(formated_dictionary_data)
    # 列名を日本語に変更
    jp_output_data: pd.DataFrame = en_output_data.rename(
        columns={
            "original": "元データ",
            "prefecture": "都道府県",
            "address1": "市や特別区",
            "address2": "町村、区および字",
            "address3": "番地",
            "address4": "建物名",
            "address5": "建物情報",
            "error1": "深刻な警告",
            "error2": "警告",
            "caution": "注意",
        }
    )

    jp_output_data.to_csv(PATH, encoding="utf-8_sig")
