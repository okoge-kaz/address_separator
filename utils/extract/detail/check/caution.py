import re


def caution(AddressDataForFormatting, munipulated_others_tail: list, caution: list) -> None:
    """
    args: (AddressDataForFormatting, munipulated_others_tail: list, caution: list)
    return: void
    不適切な形で分割されていると思われるデータを検知し、cautionを出す。一部データ整形機能も持つ
    エラー文は、文字列を結合させていく方式で連結していく。
    """
    # others_tail内部の半角-を全角に直す
    def replace_half_hypen_with_full_width_hypen(string: str):
        res: str = ""
        for char in string:
            if char == "-":
                res = res + "ー"
            else:
                res = res + char
        return res

    for i in range(len(munipulated_others_tail)):
        munipulated_others_tail[i] = replace_half_hypen_with_full_width_hypen(munipulated_others_tail[i])

    AddressDataForFormatting.building_info = munipulated_others_tail
    AddressDataForFormatting.building_detail_info = AddressDataForFormatting.building_detail_info
    AddressDataForFormatting.error1 = caution
    AddressDataForFormatting.error2 = [""] * len(caution)
    AddressDataForFormatting.caution = [""] * len(caution)
    # caution: CAUTION, error1 深刻なエラー, error2 普通のエラー
    """ビル情報の列にビルの詳細情報の断片と思われるデータが存在するとき"""
    for index in range(len(AddressDataForFormatting.building_info)):
        if re.search("(^号)|(^号館)", AddressDataForFormatting.building_info[index]) is not None:
            AddressDataForFormatting.caution[
                index
            ] += "CAUTION: address4のデータは、address5にあるべきはずのデータを含んでいる場合があります。周辺のデータ分割が正しいかどうか確認することを推奨します.  "
        else:
            pass
    # cityにおかしなところがないか調査
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", AddressDataForFormatting.city[index]) is None:
            # 日本語が見つからない
            AddressDataForFormatting.error1[index] += "ERROR: address1のデータには不正な文字列が含まれています。  "
        else:
            pass
    # townにおかしなところがないか調査
    for index in range(len(AddressDataForFormatting.town)):
        if AddressDataForFormatting.town[index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", AddressDataForFormatting.town[index]) is None:
            # 日本語が見つからない
            AddressDataForFormatting.error1[index] += "ERROR: address1または、address2のデータには不正な文字列が含まれています。  "
        else:
            pass
    # districtにおかしなところがないか調査
    for index in range(len(AddressDataForFormatting.district)):
        if AddressDataForFormatting.district[index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", AddressDataForFormatting.district[index]) is None:
            # 日本語が見つからない
            AddressDataForFormatting.error1[index] += "ERROR: address2のデータには不正な文字列が含まれています。  "
        else:
            pass
    for index in range(len(AddressDataForFormatting.house_number)):
        if AddressDataForFormatting.house_number[index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", AddressDataForFormatting.house_number[index]) is not None:
            # 日本語が見つかった
            AddressDataForFormatting.error1[index] += "ERROR: address3のデータには不正な文字列が含まれています。  "
        else:
            pass
    for index in range(len(AddressDataForFormatting.special_characters)):
        if AddressDataForFormatting.house_number[index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", AddressDataForFormatting.special_characters[index]) is not None:
            # 日本語が見つかった
            AddressDataForFormatting.caution[index] += "CAUTION: address4のデータには不正な文字列が含まれています。  "
        else:
            pass
    for index in range(len(AddressDataForFormatting.original)):
        if AddressDataForFormatting.original[index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", AddressDataForFormatting.original[index]) is None:
            # 日本語が見つからない
            AddressDataForFormatting.error1[index] += "ERROR: 入力された元データに何らかの問題があります。入力されたデータを確認してください。  "
        else:
            pass
    # 不正なデータを検出
    for index in range(len(AddressDataForFormatting.town)):
        if AddressDataForFormatting.town[index] == "":
            continue
        if re.search("[0-9]+", AddressDataForFormatting.town[index]) is not None:
            # 半角算用数字がある
            AddressDataForFormatting.error1[index] += "ERROR: address1のデータには存在しないはずのアラビア数字が含まれています。  "
        else:
            pass
    for index in range(len(AddressDataForFormatting.district)):
        if AddressDataForFormatting.district[index] == "":
            continue
        if re.search("[一-十]{2,}", AddressDataForFormatting.district[index]) is not None:
            # 日本語数字が2回以上続く、地名の可能性もあるが、高確率番地
            AddressDataForFormatting.error1[index] += "CAUTION: address2のデータには不正な文字列が含まれている可能性があります。  "
        else:
            pass
    # building_info が空なのに building_detail_infoが空ではなかったらcaution
    for index in range(len(AddressDataForFormatting.building_info)):
        if AddressDataForFormatting.building_info[index] == "" and AddressDataForFormatting.building_detail_info[index] != "":
            AddressDataForFormatting.caution[index] += "CAUTION: address4と、address5のデータには不正な文字列が含まれている可能性があります。両方について確認することを推奨します。  "
    # 都道府県名が空欄ならcaution
    for index in range(len(AddressDataForFormatting.prefecture)):
        if AddressDataForFormatting.prefecture[index] == "":
            AddressDataForFormatting.error2[
                index
            ] += "ERROR: prefectureの列の情報がありません。元データに都道府県情報が欠落している可能性があります。入力されたデータ形式は、自動チェック機構が推奨する形式ではありません。  "
