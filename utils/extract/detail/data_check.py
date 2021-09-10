import pandas as pd


def data_check(data: dict):
    '''総務省のデータから実在する市町村であるかどうか調べる'''
    PATH = 'data/administrative_district.csv'
    administrative_data_csv = pd.read_csv(PATH)
    for index in range(len(data['prefacture'])):
        prefacture: str = data['prefacture'][index]
        if prefacture == "":
            continue
        if data['city'][index] in list(administrative_data_csv[prefacture]):
            pass
        else:
            data['caution'][index] += "VALUE ERROR: The address1 column's cell is INVALID. Address1 column's data is something wrong. "
    CHECH_PATH = 'data/Ordinance_designated_city.csv'
    Ordinance_designated_city_csv = pd.read_csv(CHECH_PATH)
    print(list(Ordinance_designated_city_csv.columns))
    for index in range(len(data['city'])):
        if data['city'][index] in list(Ordinance_designated_city_csv.columns):
            city_name = data['city'][index]
            if data['town'][index] in list(Ordinance_designated_city_csv[city_name]):
                pass
            else:
                data['caution'][index] += "VALUE ERROR: The address2 column's cell is INVALID. address2 data is something wrong. "
