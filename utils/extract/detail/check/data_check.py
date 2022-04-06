import os
import re

import pandas as pd


def data_check(data: dict) -> None:
    """
    args: data: dict
    return: void
    総務省のデータから実在する市町村であるかどうか調べる
    """
    Current_Path = os.getcwd()
    PATH = Current_Path + "/data/administrative_district.csv"
    administrative_data_csv: pd.DataFrame = pd.read_csv(PATH)
    for index in range(len(data["prefecture"])):
        prefecture: str = data["prefecture"][index]
        if prefecture == "":
            continue
        if data["city"][index] in list(administrative_data_csv[prefecture]):
            pass
        elif re.search("郡", data["city"][index]):
            continue
        else:
            data["error1"][index] += "ERROR: address1の列の情報が不正です。自動整形過程で何らかの問題が発生しました。  "
    # 政令指定都市に関してはさらに詳しくチェック
    CHECH_PATH = "data/Ordinance_designated_city.csv"
    Ordinance_designated_city_csv: pd.DataFrame = pd.read_csv(CHECH_PATH)
    for index in range(len(data["city"])):
        if data["city"][index] in list(Ordinance_designated_city_csv.columns):
            city_name = data["city"][index]
            if data["town"][index] in list(Ordinance_designated_city_csv[city_name]):
                pass
            else:
                data["error1"][index] += "ERROR: address2の列の情報が不正です。自動整形過程で何らかの問題が発生しました。  "
