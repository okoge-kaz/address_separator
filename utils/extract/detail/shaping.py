import re


def shaping(data: dict, munipulated_others_tail: list, caution: list):
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

    # cautionについて
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
    for index in range(len(data['town'])):
        if data['town'][index] == "":
            continue
        if re.search('[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+', data['town'][index]) is None:
            # 日本語が見つからない
            data['caution'][index] = True
        else:
            pass
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
