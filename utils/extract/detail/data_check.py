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
            data['caution'][index] = True
