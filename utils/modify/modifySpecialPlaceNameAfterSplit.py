import re


def modify_special_place_name(splittedAddressDataDictionaries: dict[str, list[str]]) -> None:
    """
    args: splittedAddressDataDictionaries (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void

    各ケースごとに処理を行う
    地名が特殊であるために、うまく分割できなかったものを再整形している
    ルールベースなため、完全網羅は不可能

    """

    DATA_SIZE: int = len(splittedAddressDataDictionaries["address3"])

    # 一宮
    for index in range(DATA_SIZE):
        if (
            splittedAddressDataDictionaries["address3"][index] == "1"
            and splittedAddressDataDictionaries["address4"][index] == "宮"
        ):
            if splittedAddressDataDictionaries["address2"][index] != "":
                splittedAddressDataDictionaries["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splittedAddressDataDictionaries["address2"][index] = "一宮"
                splittedAddressDataDictionaries["address3"][index] = splittedAddressDataDictionaries["address5"][index]
                splittedAddressDataDictionaries["address4"][index] = ""
                splittedAddressDataDictionaries["address5"][index] = ""

    # 一宮徳谷
    for index in range(DATA_SIZE):
        if (
            splittedAddressDataDictionaries["address3"][index] == "1"
            and splittedAddressDataDictionaries["address4"][index] == "宮徳谷"
        ):
            if splittedAddressDataDictionaries["address2"][index] != "":
                splittedAddressDataDictionaries["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splittedAddressDataDictionaries["address2"][index] = "一宮徳谷"
                splittedAddressDataDictionaries["address3"][index] = splittedAddressDataDictionaries["address5"][index]
                splittedAddressDataDictionaries["address4"][index] = ""
                splittedAddressDataDictionaries["address5"][index] = ""

    # 五台山
    for index in range(DATA_SIZE):
        if (
            splittedAddressDataDictionaries["address3"][index] == "5"
            and splittedAddressDataDictionaries["address4"][index] == "台山"
        ):
            if splittedAddressDataDictionaries["address2"][index] != "":
                splittedAddressDataDictionaries["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splittedAddressDataDictionaries["address2"][index] = "五台山"
                splittedAddressDataDictionaries["address3"][index] = splittedAddressDataDictionaries["address5"][index]
                splittedAddressDataDictionaries["address4"][index] = ""
                splittedAddressDataDictionaries["address5"][index] = ""

    # 五台山〜
    for index in range(DATA_SIZE):
        if splittedAddressDataDictionaries["address3"][index] == "5" and re.search(
            "^台山.+", splittedAddressDataDictionaries["address4"][index]
        ):
            if splittedAddressDataDictionaries["address2"][index] != "":
                splittedAddressDataDictionaries["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splittedAddressDataDictionaries["address2"][index] = ""
                splittedAddressDataDictionaries["address3"][index] = ""
                splittedAddressDataDictionaries["address4"][index] = (
                    "五" + splittedAddressDataDictionaries["address4"][index]
                )

    # 三谷
    for index in range(DATA_SIZE):
        if (
            splittedAddressDataDictionaries["address3"][index] == "3"
            and splittedAddressDataDictionaries["address4"][index] == "谷"
        ):
            if splittedAddressDataDictionaries["address2"][index] != "":
                splittedAddressDataDictionaries["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splittedAddressDataDictionaries["address2"][index] = "三谷"
                splittedAddressDataDictionaries["address3"][index] = splittedAddressDataDictionaries["address5"][index]
                splittedAddressDataDictionaries["address4"][index] = ""
                splittedAddressDataDictionaries["address5"][index] = ""

    # 三原
    for index in range(DATA_SIZE):
        if (
            splittedAddressDataDictionaries["address3"][index] == "3"
            and splittedAddressDataDictionaries["address4"][index] == "原"
        ):
            if splittedAddressDataDictionaries["address2"][index] != "":
                splittedAddressDataDictionaries["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splittedAddressDataDictionaries["address2"][index] = "三原"
                splittedAddressDataDictionaries["address3"][index] = splittedAddressDataDictionaries["address5"][index]
                splittedAddressDataDictionaries["address4"][index] = ""
                splittedAddressDataDictionaries["address5"][index] = ""

    # 三重城
    for index in range(DATA_SIZE):
        if splittedAddressDataDictionaries["address3"][index] == "":
            continue
        if (
            re.search("^重城", splittedAddressDataDictionaries["address4"][index])
            and splittedAddressDataDictionaries["address3"][index][-1] == "3"
        ):
            if len(splittedAddressDataDictionaries["address3"][index]) < 2:
                continue
            splittedAddressDataDictionaries["address3"][index] = splittedAddressDataDictionaries["address3"][index][:-2]
            splittedAddressDataDictionaries["address4"][index] = "三" + splittedAddressDataDictionaries["address4"][index]

    # 町屋
    for index in range(DATA_SIZE):
        if (
            splittedAddressDataDictionaries["address1"][index] == "町"
            and splittedAddressDataDictionaries["address2"][index] == "屋"
        ):
            splittedAddressDataDictionaries["address2"][index] = "町屋"
            splittedAddressDataDictionaries["address1"][index] = ""
