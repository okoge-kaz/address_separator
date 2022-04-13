import os
import re
from typing import Match, Union

import pandas as pd


def formart_for_output(splitted_address_data_dictionaries: dict[str, list[str]]) -> dict[str, list[str]]:
    """
    format for output: 出力するcsvファイルとして望ましい形に整形する

    Parameters
    ----------
    splitted_address_data_dictionaries : dict[str, list[str]]
        分割された住所データ

    Returns
    -------

    """
    res_splitted_address_data_dictionaries: dict[str, list[str]] = {}
    # 政令指定都市かどうかを判別するためのデータ
    CURRENT_PATH = os.getcwd()
    PATH: str = CURRENT_PATH + "/splitted_address_data_dictionaries/Ordinance_designated_city.csv"

    ORDINANCE_DISTRICTED_CITY_CSV: pd.DataFrame = pd.read_csv(PATH)
    # データをコピー
    res_splitted_address_data_dictionaries["original"] = splitted_address_data_dictionaries["original"]
    res_splitted_address_data_dictionaries["prefecture"] = splitted_address_data_dictionaries["prefecture"]

    # 最終出力結果に合わせて整形 市区町村郡
    address1: list = []
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] in list(ORDINANCE_DISTRICTED_CITY_CSV):
            # 政令指定都市ならば
            address1.append(
                splitted_address_data_dictionaries["city"][index] + splitted_address_data_dictionaries["town"][index]
            )
            splitted_address_data_dictionaries["town"][index] = ""
        elif re.search("郡$", splitted_address_data_dictionaries["city"][index]):
            # 郡ならば
            address1.append(
                splitted_address_data_dictionaries["city"][index] + splitted_address_data_dictionaries["town"][index]
            )
            splitted_address_data_dictionaries["town"][index] = ""
        else:
            address1.append(splitted_address_data_dictionaries["city"][index])
    res_splitted_address_data_dictionaries["address1"] = address1
    # 町域について
    address2: list = []
    for index in range(len(splitted_address_data_dictionaries["town"])):
        if re.search("[0-9 -]", splitted_address_data_dictionaries["town"][index]) or re.search(
            "[0-9 -]", splitted_address_data_dictionaries["district"][index]
        ):
            # 不正な文字が存在する caution
            address2.append(
                splitted_address_data_dictionaries["town"][index]
                + splitted_address_data_dictionaries["district"][index]
            )
        else:
            address2.append(
                splitted_address_data_dictionaries["town"][index]
                + splitted_address_data_dictionaries["district"][index]
            )
    res_splitted_address_data_dictionaries["address2"] = address2
    # 番地について
    address3: list = []
    for index in range(len(splitted_address_data_dictionaries["house_number"])):
        if re.search("(([0-9]+)-)* [0-9]+", splitted_address_data_dictionaries["house_number"][index]):
            address3.append(splitted_address_data_dictionaries["house_number"][index])
        else:
            # 不正な文字が存在 caution
            address3.append(splitted_address_data_dictionaries["house_number"][index])
    res_splitted_address_data_dictionaries["address3"] = address3
    # 建物名
    address4: list = []
    for index in range(len(splitted_address_data_dictionaries["building_info"])):
        if splitted_address_data_dictionaries["special_characters"][index]:
            # special_charactersのセルが空ではない caution
            address4.append(
                splitted_address_data_dictionaries["special_characters"][index]
                + splitted_address_data_dictionaries["building_info"][index]
            )
        else:
            # special_charactersが空
            address4.append(splitted_address_data_dictionaries["building_info"][index])
    res_splitted_address_data_dictionaries["address4"] = address4
    # 部屋番号
    address5: list = []
    for index in range(len(splitted_address_data_dictionaries["building_detail_info"])):
        address5.append(splitted_address_data_dictionaries["building_detail_info"][index])
    res_splitted_address_data_dictionaries["address5"] = address5
    # caution
    res_splitted_address_data_dictionaries["error1"] = splitted_address_data_dictionaries["error1"]
    res_splitted_address_data_dictionaries["error2"] = splitted_address_data_dictionaries["error2"]
    res_splitted_address_data_dictionaries["caution"] = splitted_address_data_dictionaries["caution"]
    # address4について
    for index in range(len(res_splitted_address_data_dictionaries["address4"])):
        if re.search("[0-9]+$", res_splitted_address_data_dictionaries["address4"][index]):
            match: Union[Match[str], None] = re.search(
                "[0-9]+$", res_splitted_address_data_dictionaries["address4"][index]
            )

            assert match is not None
            start: int = match.start()
            end: int = match.end()

            if res_splitted_address_data_dictionaries["address5"][index] == "":
                res_splitted_address_data_dictionaries["address5"][index] = res_splitted_address_data_dictionaries[
                    "address4"
                ][index][start:end]
                res_splitted_address_data_dictionaries["address4"][index] = res_splitted_address_data_dictionaries[
                    "address4"
                ][index][:start]
            else:
                res_splitted_address_data_dictionaries["caution"][index] += "CAUTION: address4に何らかの問題がある可能性があります。  "
    # address 4の - ハイフン除去
    for index in range(len(res_splitted_address_data_dictionaries["address4"])):
        if res_splitted_address_data_dictionaries["address4"][index] == "":
            continue
        if res_splitted_address_data_dictionaries["address4"][index][0] == "-":
            res_splitted_address_data_dictionaries["address4"][index] = res_splitted_address_data_dictionaries[
                "address4"
            ][index][1:]
        if res_splitted_address_data_dictionaries["address4"][index][-1] == "-":
            if re.search("[ア-ン]$", res_splitted_address_data_dictionaries["address4"][index][:-1]) is None:
                res_splitted_address_data_dictionaries["address4"][index] = res_splitted_address_data_dictionaries[
                    "address4"
                ][index][:-1]
            else:
                # タワーなどのカタカナが入った名詞かもしれないので
                res_splitted_address_data_dictionaries["address4"][index] = (
                    res_splitted_address_data_dictionaries["address4"][index][:-1] + "ー"
                )
    # address4の表記修正
    for index in range(len(res_splitted_address_data_dictionaries["address4"])):
        # タワー,センターなどの表記が破壊されてしまっている場合は修正する
        if res_splitted_address_data_dictionaries["address4"][index] == "":
            continue
        if re.search("センタ$", res_splitted_address_data_dictionaries["address4"][index]):

            match: Union[Match[str], None] = re.search(
                "センタ$", res_splitted_address_data_dictionaries["address4"][index]
            )

            assert match is not None
            start: int = match.start()

            res_splitted_address_data_dictionaries["address4"][index] = (
                res_splitted_address_data_dictionaries["address4"][index][:start] + "センター"
            )
        if re.search("タワ$", res_splitted_address_data_dictionaries["address4"][index]):

            match: Union[Match[str], None] = re.search(
                "タワ$", res_splitted_address_data_dictionaries["address4"][index]
            )
            assert match is not None
            start: int = match.start()

            res_splitted_address_data_dictionaries["address4"][index] = (
                res_splitted_address_data_dictionaries["address4"][index][:start] + "タワー"
            )
        if re.search("^ー*$", res_splitted_address_data_dictionaries["address4"][index]):
            # 空白が-に置換されたことで生じるーを消去
            res_splitted_address_data_dictionaries["address4"][index] = ""
    # invalid について
    for index in range(len(splitted_address_data_dictionaries["invalid"])):
        if splitted_address_data_dictionaries["invalid"][index] != "":
            res_splitted_address_data_dictionaries["error1"][
                index
            ] += "ERROR: データは、整形不可能な状態です。自動整形システムは正しく動作しません。この行の全ての結果を確認することを推奨します。  "
    # address3がなく、address4がある場合 caution
    for index in range(len(res_splitted_address_data_dictionaries["address4"])):
        if (
            res_splitted_address_data_dictionaries["address3"][index] == ""
            and res_splitted_address_data_dictionaries["address4"][index] != ""
        ):
            res_splitted_address_data_dictionaries["caution"][
                index
            ] += "CAUTION: address4の情報は本来あるべきではない場所にある可能性があります。  "
    # address4 or address5 に ? があったら caution
    for index in range(len(res_splitted_address_data_dictionaries["address4"])):
        if "?" in res_splitted_address_data_dictionaries["address4"][index]:
            res_splitted_address_data_dictionaries["caution"][
                index
            ] += "CAUTION: データには?が含まれており、文字コードに関わる何かしらの表示揺れがある可能性があります。  "
        elif "?" in res_splitted_address_data_dictionaries["address5"][index]:
            res_splitted_address_data_dictionaries["caution"][
                index
            ] += "CAUTION: データには?が含まれており、文字コードに関わる何かしらの表示揺れがある可能性があります。  "
    # address4 が空かつ address5も空でかつ、 address3に-が3つあり、かつ最後の数字が302のような形であったらそれをaddress5に移す
    for index in range(len(res_splitted_address_data_dictionaries["address4"])):
        if (
            res_splitted_address_data_dictionaries["address4"][index] == ""
            and res_splitted_address_data_dictionaries["address5"][index] == ""
        ):
            if re.search(
                "([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)", res_splitted_address_data_dictionaries["address3"][index]
            ):
                if re.search(
                    "([0-9]+)-([0-9]+)-([0-9]+)-([0-9]{3,})", res_splitted_address_data_dictionaries["address3"][index]
                ):
                    match: Union[Match[str], None] = re.search(
                        "-[0-9]+$", res_splitted_address_data_dictionaries["address3"][index]
                    )
                    assert match is not None
                    start: int = match.start()

                    # 3-5-4-809 の809の部分をaddress5に移行する
                    res_splitted_address_data_dictionaries["address5"][index] = res_splitted_address_data_dictionaries[
                        "address3"
                    ][index][start + 1 :]
                    res_splitted_address_data_dictionaries["address3"][index] = res_splitted_address_data_dictionaries[
                        "address3"
                    ][index][:start]
                else:
                    res_splitted_address_data_dictionaries["caution"][index] += "CAUTION: 番地の中に、部屋番号が含まれている可能性があります。 "
            elif re.search(
                "([0-9]+)-([0-9]+)-([1-9][0-1][0-9])", res_splitted_address_data_dictionaries["address3"][index]
            ):
                # 3-8-902 のような場合にcautionを出す
                res_splitted_address_data_dictionaries["caution"][index] += "CAUTION: 番地の中に、部屋番号が含まれている可能性があります。 "
            elif re.search(
                "([0-9]+)-([0-9]+)-([1-9][0-9][0-1][0-9])", res_splitted_address_data_dictionaries["address3"][index]
            ):
                # 3-8-902 のような場合にcautionを出す
                res_splitted_address_data_dictionaries["caution"][index] += "CAUTION: 番地の中に、部屋番号が含まれている可能性があります。"
    # 一宮, 三谷などの町域が不正に分割された場合にERROR
    for index in range(len(res_splitted_address_data_dictionaries["address3"])):
        if re.search("^[0-9]$", res_splitted_address_data_dictionaries["address3"][index]):
            # address3が数字一つ
            if (
                len(res_splitted_address_data_dictionaries["address4"][index]) == 1
                and res_splitted_address_data_dictionaries["address5"][index] != ""
            ):
                res_splitted_address_data_dictionaries["error2"][index] += "ERROR: 町域が不正に分割されている恐れがあります。 "
            else:
                res_splitted_address_data_dictionaries["caution"][index] = "CAUTION: 町域名に含まれる漢数字が不正に分割されている恐れがあります。 "
    # address5に1-6-10などのものがあったらerror
    for index in range(len(res_splitted_address_data_dictionaries["address5"])):
        if re.search("([0-9]+)+", res_splitted_address_data_dictionaries["address5"][index]):
            res_splitted_address_data_dictionaries["error2"][index] += "ERROR: address5の建物情報の箇所に番地と思しき情報が存在します"
    # アルファベット + ーについては消去
    for index in range(len(res_splitted_address_data_dictionaries["address4"])):
        if re.search("[A-Z]+ー$", res_splitted_address_data_dictionaries["address4"][index]):
            res_splitted_address_data_dictionaries["address4"][index] = res_splitted_address_data_dictionaries[
                "address4"
            ][index][:-1]
    # 返値
    return res_splitted_address_data_dictionaries
