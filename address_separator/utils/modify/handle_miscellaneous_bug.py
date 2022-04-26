import re


def handle_miscellaneous_bugs(splitted_address_data_dictionaries: dict[str, list[str]]) -> None:
    """
    args: splitted_address_data_dictionaries (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void

    各ケースごとに処理を行う
    地名が特殊であるために、うまく分割できなかったものを再整形している
    ルールベースなため、完全網羅は不可能

    """

    # address2に-があったらerror
    for index in range(len(splitted_address_data_dictionaries["address2"])):
        if re.search("-", splitted_address_data_dictionaries["address2"][index]):
            splitted_address_data_dictionaries["error1"][
                index
            ] += "ERROR: address2に存在する情報は秩序だっていません。整形エラーが発生している可能性が高いです。  "

    # address5に~号 とあるがaddress4が空で、かつaddress3に-が2未満なとき
    for index in range(len(splitted_address_data_dictionaries["address5"])):
        if (
            re.search("^[0-9]+号$", splitted_address_data_dictionaries["address5"][index])
            and splitted_address_data_dictionaries["address4"][index] == ""
        ):
            if re.search("^[0-9]+(-[0-9]+)*$", splitted_address_data_dictionaries["address3"][index]):
                # address3が正常かどうか
                if re.search("^[0-9]+(-[0-9]+){2,}$", splitted_address_data_dictionaries["address3"][index]):
                    # ハイフンが2回以上
                    continue
                else:
                    # 2回未満
                    # ~号というものをaddress3に追加する(号を消して)
                    splitted_address_data_dictionaries["address3"][index] += (
                        "-" + splitted_address_data_dictionaries["address5"][index][:-1]
                    )
                    splitted_address_data_dictionaries["address5"][index] = ""
            else:
                splitted_address_data_dictionaries["error1"][index] += "ERROR: address3のデータ形式が不正です。 "

    # ()をはずした後の処理 数字
    for index in range(len(splitted_address_data_dictionaries["address4"])):
        if re.search("[0-9]+(ー[0-9]+)*", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"][index] != "":
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4にはaddress5にあるべきデータが存在するやもしれません。  "
                continue
            splitted_address_data_dictionaries["address5"][index] = re.sub(
                "ー", "-", splitted_address_data_dictionaries["address4"][index]
            )
            splitted_address_data_dictionaries["address4"][index] = ""

    # 番地がないデータの処理
    for index in range(len(splitted_address_data_dictionaries["address4"])):
        if (
            splitted_address_data_dictionaries["address4"][index] != ""
            and splitted_address_data_dictionaries["address3"][index] == ""
        ):
            # address4にある町域データと思しきものを移動
            if re.search("[a-z A-Z 0-9 - ?]", splitted_address_data_dictionaries["address4"][index]):
                # マンション名にありそうなものを除く
                continue
            if re.search(
                "地|事務所|会館|パーク|ハウス|ホーム|メール|コート|団地|ハイム|コーポ|メゾン|棟|グランド|株式会社|有限会社|（株）|ビル|北口店|南口店|西口店|東口店|組合|荘|建設|プラザ|パレス|サロン|レジデンス|レジデンシャル|ハイム|NPO|NGO|NPO|NGO|㈲|メゾン|ロイヤル|テーラー|亭",
                splitted_address_data_dictionaries["address4"][index],
            ):
                continue
            else:
                splitted_address_data_dictionaries["address2"][index] = (
                    splitted_address_data_dictionaries["address2"][index]
                    + splitted_address_data_dictionaries["address4"][index]
                )
                splitted_address_data_dictionaries["address4"][index] = ""
