import re


def shaping(data: dict, munipulated_others_tail: list, cation: list):
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
    data['cation'] = cation

    # cationについて
    for index in range(len(data['building_info'])):
        if re.search('(^号)|(^号館)', data["building_info"][index]) is not None:
            data['cation'][index] = True
        else:
            pass
    # 不正なデータを検出
