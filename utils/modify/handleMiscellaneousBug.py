import re


def handle_miscellaneous_bugs(splittedAddressDataDictionaries: dict[str, list[str]]):
    """
    args: splittedAddressDataDictionaries (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void

    各ケースごとに処理を行う
    地名が特殊であるために、うまく分割できなかったものを再整形している
    ルールベースなため、完全網羅は不可能

    """

    # address2に-があったらerror
    for index in range(len(splittedAddressDataDictionaries["address2"])):
        if re.search("-", splittedAddressDataDictionaries["address2"][index]):
            splittedAddressDataDictionaries["error1"][
                index
            ] += "ERROR: address2に存在する情報は秩序だっていません。整形エラーが発生している可能性が高いです。  "

    # address5に~号 とあるがaddress4が空で、かつaddress3に-が2未満なとき
    for index in range(len(splittedAddressDataDictionaries["address5"])):
        if (
            re.search("^[0-9]+号$", splittedAddressDataDictionaries["address5"][index])
            and splittedAddressDataDictionaries["address4"][index] == ""
        ):
            if re.search("^[0-9]+(-[0-9]+)*$", splittedAddressDataDictionaries["address3"][index]):
                # address3が正常かどうか
                if re.search("^[0-9]+(-[0-9]+){2,}$", splittedAddressDataDictionaries["address3"][index]):
                    # ハイフンが2回以上
                    continue
                else:
                    # 2回未満
                    # ~号というものをaddress3に追加する(号を消して)
                    splittedAddressDataDictionaries["address3"][index] += (
                        "-" + splittedAddressDataDictionaries["address5"][index][:-1]
                    )
                    splittedAddressDataDictionaries["address5"][index] = ""
            else:
                splittedAddressDataDictionaries["error1"][index] += "ERROR: address3のデータ形式が不正です。 "

    # ()をはずした後の処理 数字
    for index in range(len(splittedAddressDataDictionaries["address4"])):
        if re.search("[0-9]+(ー[0-9]+)*", splittedAddressDataDictionaries["address4"][index]):
            if splittedAddressDataDictionaries["address5"][index] != "":
                splittedAddressDataDictionaries["caution"][index] += "CAUTION: address4にはaddress5にあるべきデータが存在するやもしれません。  "
                continue
            splittedAddressDataDictionaries["address5"][index] = re.sub(
                "ー", "-", splittedAddressDataDictionaries["address4"][index]
            )
            splittedAddressDataDictionaries["address4"][index] = ""

    # 番地がないデータの処理
    for index in range(len(splittedAddressDataDictionaries["address4"])):
        if (
            splittedAddressDataDictionaries["address4"][index] != ""
            and splittedAddressDataDictionaries["address3"][index] == ""
        ):
            # address4にある町域データと思しきものを移動
            if re.search("[a-z A-Z 0-9 - ?]", splittedAddressDataDictionaries["address4"][index]):
                # マンション名にありそうなものを除く
                continue
            if re.search(
                "地|事務所|会館|パーク|ハウス|ホーム|メール|コート|団地|ハイム|コーポ|メゾン|棟|グランド|株式会社|有限会社|（株）|ビル|北口店|南口店|西口店|東口店|組合|荘|建設|プラザ|パレス|サロン|レジデンス|レジデンシャル|ハイム|NPO|NGO|NPO|NGO|㈲|メゾン|ロイヤル|テーラー|亭",
                splittedAddressDataDictionaries["address4"][index],
            ):
                continue
            else:
                splittedAddressDataDictionaries["address2"][index] = (
                    splittedAddressDataDictionaries["address2"][index] + splittedAddressDataDictionaries["address4"][index]
                )
                splittedAddressDataDictionaries["address4"][index] = ""
