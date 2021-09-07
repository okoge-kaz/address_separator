import re


def caution(data: dict, munipulated_others_tail: list, caution: list):
    '''不適切な形で分割されていると思われるデータを検知し、cautionを出す。一部データ整形機能も持つ'''
    # others_tail内部の半角-を全角に直す
    def replace_half_hypen_with_full_width_hypen(string: str):
        res: str = ""
        for char in string:
            if char == '-':
                res = res + 'ー'
            else:
                res = res + char
        return res

    for i in range(len(munipulated_others_tail)):
        munipulated_others_tail[i] = replace_half_hypen_with_full_width_hypen(
            munipulated_others_tail[i])

    data['building_info'] = munipulated_others_tail
    data['building_detail_info'] = data['building_detail_info']
    data['caution'] = caution

    '''ビル情報の列にビルの詳細情報の断片と思われるデータが存在するとき'''
    for index in range(len(data['building_info'])):
        if re.search('(^号)|(^号館)', data["building_info"][index]) is not None:
            data['caution'][index] = True
        else:
            pass
    # cityにおかしなところがないか調査
    for index in range(len(data['city'])):
        if data['city'][index] == "":
            continue
        if re.search('[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+', data['city'][index]) is None:
            # 日本語が見つからない
            data['caution'][index] = True
        else:
            pass
    # townにおかしなところがないか調査
    for index in range(len(data['town'])):
        if data['town'][index] == "":
            continue
        if re.search('[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+', data['town'][index]) is None:
            # 日本語が見つからない
            data['caution'][index] = True
        else:
            pass
    # districtにおかしなところがないか調査
    for index in range(len(data['district'])):
        if data['district'][index] == "":
            continue
        if re.search('[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+', data['district'][index]) is None:
            # 日本語が見つからない
            data['caution'][index] = True
        else:
            pass
    for index in range(len(data['house_number'])):
        if data['house_number'][index] == "":
            continue
        if re.search('[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+', data['house_number'][index]) is not None:
            # 日本語が見つかった
            data['caution'][index] = True
        else:
            pass
    for index in range(len(data['special_characters'])):
        if data['house_number'][index] == "":
            continue
        if re.search('[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+', data['special_characters'][index]) is not None:
            # 日本語が見つかった
            data['caution'][index] = True
        else:
            pass
    for index in range(len(data['original'])):
        if data['original'][index] == "":
            continue
        if re.search('[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+', data['original'][index]) is None:
            # 日本語が見つからない
            data['caution'][index] = True
        else:
            pass
    # 不正なデータを検出
    for index in range(len(data['town'])):
        if data['town'][index] == "":
            continue
        if re.search('[0-9]+', data['town'][index]) is not None:
            # 半角算用数字がある
            data['caution'][index] = True
        else:
            pass
    for index in range(len(data['district'])):
        if data['district'][index] == "":
            continue
        if re.search('[一-十]{2,}', data['district'][index]) is not None:
            # 日本語数字が2回以上続く、地名の可能性もあるが、高確率番地
            data['caution'][index] = True
        else:
            pass
    # building_info が空なのに building_detail_infoが空ではなかったらcaution
    for index in range(len(data['building_info'])):
        if data['building_info'][index] == '' and data['building_detail_info'][index] != '':
            data['caution'][index] = True
    # 都道府県名が空欄ならcaution
    