import os
import re

import pandas as pd


def data_check(splitted_address_data_dictionaries: dict[str, list[str]]):
    """
    総務省のデータから実在する市町村であるかどうか調べる
    """
    Current_Path = os.getcwd()
    PATH = Current_Path + "/data/administrative_district.csv"
    administrative_data_csv: pd.DataFrame = pd.read_csv(PATH)
    for index in range(len(splitted_address_data_dictionaries["prefecture"])):
        prefecture: str = splitted_address_data_dictionaries["prefecture"][index]
        if prefecture == "":
            continue
        if splitted_address_data_dictionaries["city"][index] in list(administrative_data_csv[prefecture]):
            pass
        elif re.search("郡", splitted_address_data_dictionaries["city"][index]):
            continue
        else:
            splitted_address_data_dictionaries["error1"][index] += "ERROR: address1の列の情報が不正です。自動整形過程で何らかの問題が発生しました。  "
    # 政令指定都市に関してはさらに詳しくチェック
    CHECH_PATH = "data/Ordinance_designated_city.csv"
    Ordinance_designated_city_csv: pd.DataFrame = pd.read_csv(CHECH_PATH)
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] in list(Ordinance_designated_city_csv.columns):
            city_name = splitted_address_data_dictionaries["city"][index]
            if splitted_address_data_dictionaries["town"][index] in list(Ordinance_designated_city_csv[city_name]):
                pass
            else:
                splitted_address_data_dictionaries["error1"][index] += "ERROR: address2の列の情報が不正です。自動整形過程で何らかの問題が発生しました。  "
