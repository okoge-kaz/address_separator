import re


def hadle_miscellaneous_bugs(splitedAddressDataDictionarys: dict[str, list[str]]):
    """
    args: splitedAddressDataDictionarys (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void

    各ケースごとに処理を行う
    地名が特殊であるために、うまく分割できなかったものを再整形している
    ルールベースなため、完全網羅は不可能

    """

    # address2に-があったらerror
    for index in range(len(splitedAddressDataDictionarys["address2"])):
        if re.search("-", splitedAddressDataDictionarys["address2"][index]):
            splitedAddressDataDictionarys["error1"][
                index
            ] += "ERROR: address2に存在する情報は秩序だっていません。整形エラーが発生している可能性が高いです。  "

    # address5に~号 とあるがaddress4が空で、かつaddress3に-が2未満なとき
    for index in range(len(splitedAddressDataDictionarys["address5"])):
        if (
            re.search("^[0-9]+号$", splitedAddressDataDictionarys["address5"][index])
            and splitedAddressDataDictionarys["address4"][index] == ""
        ):
            if re.search("^[0-9]+(-[0-9]+)*$", splitedAddressDataDictionarys["address3"][index]):
                # address3が正常かどうか
                if re.search("^[0-9]+(-[0-9]+){2,}$", splitedAddressDataDictionarys["address3"][index]):
                    # ハイフンが2回以上
                    continue
                else:
                    # 2回未満
                    # ~号というものをaddress3に追加する(号を消して)
                    splitedAddressDataDictionarys["address3"][index] += (
                        "-" + splitedAddressDataDictionarys["address5"][index][:-1]
                    )
                    splitedAddressDataDictionarys["address5"][index] = ""
            else:
                splitedAddressDataDictionarys["error1"][index] += "ERROR: address3のデータ形式が不正です。 "

    # ()をはずした後の処理 数字
    for index in range(len(splitedAddressDataDictionarys["address4"])):
        if re.search("[0-9]+(ー[0-9]+)*", splitedAddressDataDictionarys["address4"][index]):
            if splitedAddressDataDictionarys["address5"][index] != "":
                splitedAddressDataDictionarys["caution"][index] += "CAUTION: address4にはaddress5にあるべきデータが存在するやもしれません。  "
                continue
            splitedAddressDataDictionarys["address5"][index] = re.sub(
                "ー", "-", splitedAddressDataDictionarys["address4"][index]
            )
            splitedAddressDataDictionarys["address4"][index] = ""

    # 番地がないデータの処理
    for index in range(len(splitedAddressDataDictionarys["address4"])):
        if (
            splitedAddressDataDictionarys["address4"][index] != ""
            and splitedAddressDataDictionarys["address3"][index] == ""
        ):
            # address4にある町域データと思しきものを移動
            if re.search("[a-z A-Z 0-9 - ?]", splitedAddressDataDictionarys["address4"][index]):
                # マンション名にありそうなものを除く
                continue
            if re.search(
                "地|事務所|会館|パーク|ハウス|ホーム|メール|コート|団地|ハイム|コーポ|メゾン|棟|グランド|株式会社|有限会社|（株）|ビル|北口店|南口店|西口店|東口店|組合|荘|建設|プラザ|パレス|サロン|レジデンス|レジデンシャル|ハイム|NPO|NGO|NPO|NGO|㈲|メゾン|ロイヤル|テーラー|亭",
                splitedAddressDataDictionarys["address4"][index],
            ):
                continue
            else:
                splitedAddressDataDictionarys["address2"][index] = (
                    splitedAddressDataDictionarys["address2"][index] + splitedAddressDataDictionarys["address4"][index]
                )
                splitedAddressDataDictionarys["address4"][index] = ""

    # address2に - が入っているパターン
    for index in range(len(splitedAddressDataDictionarys["address2"])):
        if re.search("-", splitedAddressDataDictionarys["address2"][index]):
            splitedAddressDataDictionarys["caution"][
                index
            ] += "CAUTION: 自動整形システムが推測によって分割している箇所があります。この行の分割が正しいか確認することを強く推奨します。 "
            # 西一-一八-一六-カモミ-ル西町 のようになっているはず
            mapping: dict = {
                "一": "1",
                "二": "2",
                "三": "3",
                "四": "4",
                "五": "5",
                "六": "6",
                "七": "7",
                "八": "8",
                "九": "9",
                "十": "10",
                "〇": "0",
            }
            japanese_numbers: list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "〇"]
            string: str = ""
            for id in range(len(splitedAddressDataDictionarys["address2"][index])):
                if splitedAddressDataDictionarys["address2"][index][id] in japanese_numbers:
                    string += mapping[splitedAddressDataDictionarys["address2"][index][id]]
                else:
                    string += splitedAddressDataDictionarys["address2"][index][id]

            # 分割作業
            if re.search("[0-9]+", string):
                # 数字がある
                address3_start: int = re.search("[0-9]+", string).start()
                address3_end: int = re.search("[0-9]+(-[0-9]+)*", string).end()
                # 数字で終わる
                if len(string) == re.search("[0-9]+(-[0-9]+)*", string).end():
                    if splitedAddressDataDictionarys["address3"][index] == "":
                        splitedAddressDataDictionarys["address2"][index] = string[:address3_start]
                        splitedAddressDataDictionarys["address3"][index] = string[address3_start:address3_end]
                    else:
                        splitedAddressDataDictionarys["address2"][index] = string[:address3_start]
                        splitedAddressDataDictionarys["address3"][index] = (
                            string[address3_start:address3_end] + splitedAddressDataDictionarys["address3"][index]
                        )
                else:
                    # 建物名らしきものが存在する
                    if splitedAddressDataDictionarys["address3"][index] == "":
                        # 番地情報が空
                        splitedAddressDataDictionarys["address2"][index] = string[:address3_start]
                        splitedAddressDataDictionarys["address3"][index] = string[address3_start:address3_end]
                        building_information_splitedAddressDataDictionarys: str = string[address3_end:]
                        if re.search("[0-9]", building_information_splitedAddressDataDictionarys):
                            # 建物名の情報に部屋番号が紛れ込んでいる
                            start_index: int = re.search(
                                "[0-9]", building_information_splitedAddressDataDictionarys
                            ).start()
                            splitedAddressDataDictionarys["address4"][
                                index
                            ] = building_information_splitedAddressDataDictionarys[:start_index]
                            # 先頭の-を削除
                            if (
                                splitedAddressDataDictionarys["address4"][index] != ""
                                and splitedAddressDataDictionarys["address4"][index][0] == "-"
                            ):
                                if len(splitedAddressDataDictionarys["address4"][index]) >= 2:
                                    splitedAddressDataDictionarys["address4"][index] = splitedAddressDataDictionarys[
                                        "address4"
                                    ][index][1:]
                            # address4の-をーに変更
                            splitedAddressDataDictionarys["address4"][index] = re.sub(
                                "-", "ー", splitedAddressDataDictionarys["address4"][index]
                            )
                            # address5
                            splitedAddressDataDictionarys["aadress5"][
                                index
                            ] = building_information_splitedAddressDataDictionarys[start_index:]
                        else:
                            # 建物情報のみ
                            splitedAddressDataDictionarys["address4"][
                                index
                            ] = building_information_splitedAddressDataDictionarys
                            # 先頭の-を削除
                            if (
                                splitedAddressDataDictionarys["address4"][index] != ""
                                and splitedAddressDataDictionarys["address4"][index][0] == "-"
                            ):
                                if len(splitedAddressDataDictionarys["address4"][index]) >= 2:
                                    splitedAddressDataDictionarys["address4"][index] = splitedAddressDataDictionarys[
                                        "address4"
                                    ][index][1:]
                            # address4の-をーに変更
                            splitedAddressDataDictionarys["address4"][index] = re.sub(
                                "-", "ー", splitedAddressDataDictionarys["address4"][index]
                            )
                    else:
                        # 番地情報に数字がある
                        # 建物情報の可能性が高いのでaddress5に移す
                        splitedAddressDataDictionarys["address5"][index] = splitedAddressDataDictionarys["address3"][
                            index
                        ]
                        splitedAddressDataDictionarys["address2"][index] = string[:address3_start]
                        splitedAddressDataDictionarys["address3"][index] = string[address3_start:address3_end]
                        splitedAddressDataDictionarys["address4"][index] = string[address3_end:]
                        # 先頭の-を削除
                        if (
                            splitedAddressDataDictionarys["address4"][index] != ""
                            and splitedAddressDataDictionarys["address4"][index][0] == "-"
                        ):
                            if len(splitedAddressDataDictionarys["address4"][index]) >= 2:
                                splitedAddressDataDictionarys["address4"][index] = splitedAddressDataDictionarys[
                                    "address4"
                                ][index][1:]
                        # address4の-をーに変更
                        splitedAddressDataDictionarys["address4"][index] = re.sub(
                            "-", "ー", splitedAddressDataDictionarys["address4"][index]
                        )
            else:
                continue

    # address1に - が入っているパターン
    for index in range(len(splitedAddressDataDictionarys["address1"])):
        if re.search("-", splitedAddressDataDictionarys["address1"][index]):
            splitedAddressDataDictionarys["caution"][
                index
            ] += "CAUTION: 自動整形システムが推測によって分割している箇所があります。この行の分割が正しいか確認することを強く推奨します。 "
            # 羽若町四九三-一-市 のようになっているはず
            mapping: dict = {
                "一": "1",
                "二": "2",
                "三": "3",
                "四": "4",
                "五": "5",
                "六": "6",
                "七": "7",
                "八": "8",
                "九": "9",
                "十": "10",
                "〇": "0",
            }
            japanese_numbers: list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "〇"]
            string: str = ""
            for id in range(len(splitedAddressDataDictionarys["address1"][index])):
                if splitedAddressDataDictionarys["address1"][index][id] in japanese_numbers:
                    string += mapping[splitedAddressDataDictionarys["address1"][index][id]]
                else:
                    string += splitedAddressDataDictionarys["address1"][index][id]
            # 分割作業
            if re.search("[0-9]+", string):
                # 数字がある
                regular_expression_search_result = re.search("[0-9]+", string)
                address3_start: int = re.search("[0-9]+", string).start()
                address3_end: int = re.search("[0-9]+(-[0-9]+)*", string).end()
                # 数字で終わる
                if len(string) == re.search("[0-9]+(-[0-9]+)*", string).end():
                    if splitedAddressDataDictionarys["address3"][index] == "":
                        splitedAddressDataDictionarys["address1"][index] = string[:address3_start]
                        splitedAddressDataDictionarys["address3"][index] = string[address3_start:address3_end]
                    else:
                        splitedAddressDataDictionarys["address1"][index] = string[:address3_start]
                        splitedAddressDataDictionarys["address3"][index] = (
                            string[address3_start:address3_end] + splitedAddressDataDictionarys["address3"][index]
                        )
                else:
                    # 建物名らしきものが存在する
                    if splitedAddressDataDictionarys["address3"][index] == "":
                        # 番地情報が空
                        splitedAddressDataDictionarys["address1"][index] = string[:address3_start]
                        splitedAddressDataDictionarys["address3"][index] = string[address3_start:address3_end]
                        building_information_splitedAddressDataDictionarys: str = string[address3_end:]
                        if re.search("[0-9]", building_information_splitedAddressDataDictionarys):
                            # 建物名の情報に部屋番号が紛れ込んでいる
                            start_index: int = re.search(
                                "[0-9]", building_information_splitedAddressDataDictionarys
                            ).start()
                            splitedAddressDataDictionarys["address4"][
                                index
                            ] = building_information_splitedAddressDataDictionarys[:start_index]
                            # 先頭の-を削除
                            if (
                                splitedAddressDataDictionarys["address4"][index] != ""
                                and splitedAddressDataDictionarys["address4"][index][0] == "-"
                            ):
                                if len(splitedAddressDataDictionarys["address4"][index]) >= 2:
                                    splitedAddressDataDictionarys["address4"][index] = splitedAddressDataDictionarys[
                                        "address4"
                                    ][index][1:]
                            # address4の-をーに変更
                            splitedAddressDataDictionarys["address4"][index] = re.sub(
                                "-", "ー", splitedAddressDataDictionarys["address4"][index]
                            )
                            # address5
                            splitedAddressDataDictionarys["aadress5"][
                                index
                            ] = building_information_splitedAddressDataDictionarys[start_index:]
                        else:
                            # 建物情報のみ
                            splitedAddressDataDictionarys["address4"][
                                index
                            ] = building_information_splitedAddressDataDictionarys
                            # 先頭の-を削除
                            if (
                                splitedAddressDataDictionarys["address4"][index] != ""
                                and splitedAddressDataDictionarys["address4"][index][0] == "-"
                            ):
                                if len(splitedAddressDataDictionarys["address4"][index]) >= 2:
                                    splitedAddressDataDictionarys["address4"][index] = splitedAddressDataDictionarys[
                                        "address4"
                                    ][index][1:]
                            # address4の-をーに変更
                            splitedAddressDataDictionarys["address4"][index] = re.sub(
                                "-", "ー", splitedAddressDataDictionarys["address4"][index]
                            )
                    else:
                        # 番地情報に数字がある
                        # 建物情報の可能性が高いのでaddress5に移す
                        splitedAddressDataDictionarys["address5"][index] = splitedAddressDataDictionarys["address3"][
                            index
                        ]
                        splitedAddressDataDictionarys["address1"][index] = string[:address3_start]
                        splitedAddressDataDictionarys["address3"][index] = string[address3_start:address3_end]
                        splitedAddressDataDictionarys["address4"][index] = string[address3_end:]
                        # 先頭の-を削除
                        if (
                            splitedAddressDataDictionarys["address4"][index] != ""
                            and splitedAddressDataDictionarys["address4"][index][0] == "-"
                        ):
                            if len(splitedAddressDataDictionarys["address4"][index]) >= 2:
                                splitedAddressDataDictionarys["address4"][index] = splitedAddressDataDictionarys[
                                    "address4"
                                ][index][1:]
                        # address4の-をーに変更
                        splitedAddressDataDictionarys["address4"][index] = re.sub(
                            "-", "ー", splitedAddressDataDictionarys["address4"][index]
                        )
            else:
                continue
