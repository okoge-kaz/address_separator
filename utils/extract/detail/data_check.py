import re

import pandas as pd


def data_check(data: dict):
    '''総務省のデータから実在する市町村であるかどうか調べる'''
    PATH = 'data/administrative_district.csv'
    administrative_data_csv = pd.read_csv(PATH)
    for index in range(len(data['prefecture'])):
        prefecture: str = data['prefecture'][index]
        if prefecture == "":
            continue
        if data['city'][index] in list(administrative_data_csv[prefecture]):
            pass
        elif re.search('郡', data['city'][index]):
            continue
        else:
            data['caution'][index] += "VALUE ERROR: The address1 column's cell is INVALID. Address1 column's data is something wrong.  "
    # 政令指定都市に関してはさらに詳しくチェック
    CHECH_PATH = 'data/Ordinance_designated_city.csv'
    Ordinance_designated_city_csv = pd.read_csv(CHECH_PATH)
    for index in range(len(data['city'])):
        if data['city'][index] in list(Ordinance_designated_city_csv.columns):
            city_name = data['city'][index]
            if data['town'][index] in list(Ordinance_designated_city_csv[city_name]):
                pass
            else:
                data['caution'][index] += "VALUE ERROR: The address2 column's cell is INVALID. Address2 data is something wrong.  "
