import re


def caution(
    splitted_address_data_dictionaries: dict[str, list[str]], manipulated_others_tail: list[str], caution: list[str]
):
    """
    不適切な形で分割されていると思われるデータを検知し、cautionを出す。一部データ整形機能も持つ
    エラー文は、文字列を結合させていく方式で連結していく。
    """
    # others_tail内部の半角-を全角に直す
    def replace_half_hyphen_with_full_width_hyphen(string: str):
        res: str = ""
        for char in string:
            if char == "-":
                res = res + "ー"
            else:
                res = res + char
        return res

    for index in range(len(manipulated_others_tail)):
        manipulated_others_tail[index] = replace_half_hyphen_with_full_width_hyphen(manipulated_others_tail[index])

    splitted_address_data_dictionaries["building_info"] = manipulated_others_tail
    splitted_address_data_dictionaries["building_detail_info"] = splitted_address_data_dictionaries[
        "building_detail_info"
    ]
    splitted_address_data_dictionaries["error1"] = caution
    splitted_address_data_dictionaries["error2"] = [""] * len(caution)
    splitted_address_data_dictionaries["caution"] = [""] * len(caution)
    # caution: CAUTION, error1 深刻なエラー, error2 普通のエラー
    """ビル情報の列にビルの詳細情報の断片と思われるデータが存在するとき"""
    for index in range(len(splitted_address_data_dictionaries["building_info"])):
        if re.search("(^号)|(^号館)", splitted_address_data_dictionaries["building_info"][index]) is not None:
            splitted_address_data_dictionaries["caution"][
                index
            ] += "CAUTION: address4のデータは、address5にあるべきはずのデータを含んでいる場合があります。周辺のデータ分割が正しいかどうか確認することを推奨します.  "
        else:
            pass
    # cityにおかしなところがないか調査
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", splitted_address_data_dictionaries["city"][index]) is None:
            # 日本語が見つからない
            splitted_address_data_dictionaries["error1"][index] += "ERROR: address1のデータには不正な文字列が含まれています。  "
        else:
            pass
    # townにおかしなところがないか調査
    for index in range(len(splitted_address_data_dictionaries["town"])):
        if splitted_address_data_dictionaries["town"][index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", splitted_address_data_dictionaries["town"][index]) is None:
            # 日本語が見つからない
            splitted_address_data_dictionaries["error1"][index] += "ERROR: address1または、address2のデータには不正な文字列が含まれています。  "
        else:
            pass
    # districtにおかしなところがないか調査
    for index in range(len(splitted_address_data_dictionaries["district"])):
        if splitted_address_data_dictionaries["district"][index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", splitted_address_data_dictionaries["district"][index]) is None:
            # 日本語が見つからない
            splitted_address_data_dictionaries["error1"][index] += "ERROR: address2のデータには不正な文字列が含まれています。  "
        else:
            pass
    for index in range(len(splitted_address_data_dictionaries["house_number"])):
        if splitted_address_data_dictionaries["house_number"][index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", splitted_address_data_dictionaries["house_number"][index]) is not None:
            # 日本語が見つかった
            splitted_address_data_dictionaries["error1"][index] += "ERROR: address3のデータには不正な文字列が含まれています。  "
        else:
            pass
    for index in range(len(splitted_address_data_dictionaries["special_characters"])):
        if splitted_address_data_dictionaries["house_number"][index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", splitted_address_data_dictionaries["special_characters"][index]) is not None:
            # 日本語が見つかった
            splitted_address_data_dictionaries["caution"][index] += "CAUTION: address4のデータには不正な文字列が含まれています。  "
        else:
            pass
    for index in range(len(splitted_address_data_dictionaries["original"])):
        if splitted_address_data_dictionaries["original"][index] == "":
            continue
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+", splitted_address_data_dictionaries["original"][index]) is None:
            # 日本語が見つからない
            splitted_address_data_dictionaries["error1"][index] += "ERROR: 入力された元データに何らかの問題があります。入力されたデータを確認してください。  "
        else:
            pass
    # 不正なデータを検出
    for index in range(len(splitted_address_data_dictionaries["town"])):
        if splitted_address_data_dictionaries["town"][index] == "":
            continue
        if re.search("[0-9]+", splitted_address_data_dictionaries["town"][index]) is not None:
            # 半角算用数字がある
            splitted_address_data_dictionaries["error1"][index] += "ERROR: address1のデータには存在しないはずのアラビア数字が含まれています。  "
        else:
            pass
    for index in range(len(splitted_address_data_dictionaries["district"])):
        if splitted_address_data_dictionaries["district"][index] == "":
            continue
        if re.search("[一-十]{2,}", splitted_address_data_dictionaries["district"][index]) is not None:
            # 日本語数字が2回以上続く、地名の可能性もあるが、高確率番地
            splitted_address_data_dictionaries["error1"][index] += "CAUTION: address2のデータには不正な文字列が含まれている可能性があります。  "
        else:
            pass
    # building_info が空なのに building_detail_infoが空ではなかったらcaution
    for index in range(len(splitted_address_data_dictionaries["building_info"])):
        if (
            splitted_address_data_dictionaries["building_info"][index] == ""
            and splitted_address_data_dictionaries["building_detail_info"][index] != ""
        ):
            splitted_address_data_dictionaries["caution"][
                index
            ] += "CAUTION: address4と、address5のデータには不正な文字列が含まれている可能性があります。両方について確認することを推奨します。  "
    # 都道府県名が空欄ならcaution
    for index in range(len(splitted_address_data_dictionaries["prefecture"])):
        if splitted_address_data_dictionaries["prefecture"][index] == "":
            splitted_address_data_dictionaries["error2"][
                index
            ] += "ERROR: prefectureの列の情報がありません。元データに都道府県情報が欠落している可能性があります。入力されたデータ形式は、自動チェック機構が推奨する形式ではありません。  "
