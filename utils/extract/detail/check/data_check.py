import os
import re

import pandas as pd


def data_check(AddressDataForFormatting) -> None:
    """
    args: AddressDataForFormatting
    return: void
    総務省のデータから実在する市町村であるかどうか調べる
    """
    Current_Path = os.getcwd()
    PATH = Current_Path + "/data/administrative_district.csv"
    administrative_data_csv: pd.DataFrame = pd.read_csv(PATH)
    for index in range(len(AddressDataForFormatting.prefecture)):
        prefecture: str = AddressDataForFormatting.prefecture[index]
        if prefecture == "":
            continue
        if AddressDataForFormatting.city[index] in list(administrative_data_csv[prefecture]):
            pass
        elif re.search("郡", AddressDataForFormatting.city[index]):
            continue
        else:
            AddressDataForFormatting.error1[index] += "ERROR: address1の列の情報が不正です。自動整形過程で何らかの問題が発生しました。  "
    # 政令指定都市に関してはさらに詳しくチェック
    CHECH_PATH = "data/Ordinance_designated_city.csv"
    Ordinance_designated_city_csv: pd.DataFrame = pd.read_csv(CHECH_PATH)
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] in list(Ordinance_designated_city_csv.columns):
            city_name = AddressDataForFormatting.city[index]
            if AddressDataForFormatting.town[index] in list(Ordinance_designated_city_csv[city_name]):
                pass
            else:
                AddressDataForFormatting.error1[index] += "ERROR: address2の列の情報が不正です。自動整形過程で何らかの問題が発生しました。  "
