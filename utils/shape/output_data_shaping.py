import re


import pandas as pd


def shape(data: dict):
    '''出力するcsvファイルとして望ましい形に整形する'''
    res_data: dict = {}
    # 政令指定都市かどうかを判別するためのデータ
    PATH = 'data/Ordinance_designated_city.csv'
    Ordinance_designated_city_csv = pd.read_csv(PATH)
    # データをコピー
    res_data['original'] = data['original']
    res_data['prefecture'] = data['prefecture']
    # 最終出力結果に合わせて整形 市区町村郡
    address1: list = []
    for index in range(len(data['city'])):
        if data['city'][index] in list(Ordinance_designated_city_csv):
            # 政令指定都市ならば
            address1.append(data['city'][index] + data['town'][index])
            data['town'][index] = ''
        elif re.search('郡$', data['city'][index]):
            # 郡ならば
            address1.append(data['city'][index] + data['town'][index])
            data['town'][index] = ''
        else:
            address1.append(data['city'][index])
    res_data['address1'] = address1
    # 町域について
    address2: list = []
    for index in range(len(data['town'])):
        if re.search('[0-9 -]', data['town'][index]) or re.search('[0-9 -]', data['district'][index]):
            # 不正な文字が存在する caution
            address2.append(data['town'][index] + data['district'][index])
        else:
            address2.append(data['town'][index] + data['district'][index])
    res_data['address2'] = address2
    # 番地について
    address3: list = []
    for index in range(len(data['house_number'])):
        if re.search('(([0-9]+)-)* [0-9]+', data['house_number'][index]):
            address3.append(data['house_number'][index])
        else:
            # 不正な文字が存在 caution
            address3.append(data['house_number'][index])
    res_data['address3'] = address3
    # 建物名
    address4: list = []
    for index in range(len(data['building_info'])):
        if data['special_characters'][index]:
            # special_charactersのセルが空ではない caution
            address4.append(data['special_characters'][index] + data['building_info'][index])
        else:
            # special_charactersが空
            address4.append(data['building_info'][index])
    res_data['address4'] = address4
    # 部屋番号
    address5: list = []
    for index in range(len(data['building_detail_info'])):
        address5.append(data['building_detail_info'][index])
    res_data['address5'] = address5
    # caution
    res_data['caution'] = data['caution']
    # address4について
    for index in range(len(res_data['address4'])):
        if re.search('[0-9]+$', res_data['address4'][index]):
            start: int = re.search('[0-9]+$', res_data['address4'][index]).start()
            end: int = re.search('[0-9]+$', res_data['address4'][index]).end()
            if res_data['address5'][index] == '':
                res_data['address5'][index] = res_data['address4'][index][start:end]
                res_data['address4'][index] = res_data['address4'][index][:start]
            else:
                res_data['caution'][index] += "CAUTION: address4's column's cell is something wrong.  "
    # address 4の - ハイフン除去
    for index in range(len(res_data['address4'])):
        if res_data['address4'][index] == '':
            continue
        if res_data['address4'][index][0] == '-':
            res_data['address4'][index] = res_data['address4'][index][1:]
        if res_data['address4'][index][-1] == '-':
            res_data['address4'][index] = res_data['address4'][index][:-1]
    # 返値
    return res_data
