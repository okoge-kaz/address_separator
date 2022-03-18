import re


def modify_special_place_name(splitedAddressDataDictionarys: dict[str, list[str]]):
    """
    args: splitedAddressDataDictionarys (すでに分割された住所データの辞書型)
    return: void

    各ケースごとに処理を行う
    地名が特殊であるために、うまく分割できなかったものを再整形している
    ルールベースなため、完全網羅は不可能

    """

    DATA_SIZE: int = len(splitedAddressDataDictionarys["address3"])

    # 一宮
    for index in range(DATA_SIZE):
        if (
            splitedAddressDataDictionarys["address3"][index] == "1"
            and splitedAddressDataDictionarys["address4"][index] == "宮"
        ):
            if splitedAddressDataDictionarys["address2"][index] != "":
                splitedAddressDataDictionarys["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitedAddressDataDictionarys["address2"][index] = "一宮"
                splitedAddressDataDictionarys["address3"][index] = splitedAddressDataDictionarys["address5"][index]
                splitedAddressDataDictionarys["address4"][index] = ""
                splitedAddressDataDictionarys["address5"][index] = ""

    # 一宮徳谷
    for index in range(DATA_SIZE):
        if (
            splitedAddressDataDictionarys["address3"][index] == "1"
            and splitedAddressDataDictionarys["address4"][index] == "宮徳谷"
        ):
            if splitedAddressDataDictionarys["address2"][index] != "":
                splitedAddressDataDictionarys["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitedAddressDataDictionarys["address2"][index] = "一宮徳谷"
                splitedAddressDataDictionarys["address3"][index] = splitedAddressDataDictionarys["address5"][index]
                splitedAddressDataDictionarys["address4"][index] = ""
                splitedAddressDataDictionarys["address5"][index] = ""

    # 五台山
    for index in range(DATA_SIZE):
        if (
            splitedAddressDataDictionarys["address3"][index] == "5"
            and splitedAddressDataDictionarys["address4"][index] == "台山"
        ):
            if splitedAddressDataDictionarys["address2"][index] != "":
                splitedAddressDataDictionarys["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitedAddressDataDictionarys["address2"][index] = "五台山"
                splitedAddressDataDictionarys["address3"][index] = splitedAddressDataDictionarys["address5"][index]
                splitedAddressDataDictionarys["address4"][index] = ""
                splitedAddressDataDictionarys["address5"][index] = ""

    # 五台山〜
    for index in range(DATA_SIZE):
        if splitedAddressDataDictionarys["address3"][index] == "5" and re.search(
            "^台山.+", splitedAddressDataDictionarys["address4"][index]
        ):
            if splitedAddressDataDictionarys["address2"][index] != "":
                splitedAddressDataDictionarys["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitedAddressDataDictionarys["address2"][index] = ""
                splitedAddressDataDictionarys["address3"][index] = ""
                splitedAddressDataDictionarys["address4"][index] = (
                    "五" + splitedAddressDataDictionarys["address4"][index]
                )

    # 三谷
    for index in range(DATA_SIZE):
        if (
            splitedAddressDataDictionarys["address3"][index] == "3"
            and splitedAddressDataDictionarys["address4"][index] == "谷"
        ):
            if splitedAddressDataDictionarys["address2"][index] != "":
                splitedAddressDataDictionarys["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitedAddressDataDictionarys["address2"][index] = "三谷"
                splitedAddressDataDictionarys["address3"][index] = splitedAddressDataDictionarys["address5"][index]
                splitedAddressDataDictionarys["address4"][index] = ""
                splitedAddressDataDictionarys["address5"][index] = ""

    # 三原
    for index in range(DATA_SIZE):
        if (
            splitedAddressDataDictionarys["address3"][index] == "3"
            and splitedAddressDataDictionarys["address4"][index] == "原"
        ):
            if splitedAddressDataDictionarys["address2"][index] != "":
                splitedAddressDataDictionarys["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitedAddressDataDictionarys["address2"][index] = "三原"
                splitedAddressDataDictionarys["address3"][index] = splitedAddressDataDictionarys["address5"][index]
                splitedAddressDataDictionarys["address4"][index] = ""
                splitedAddressDataDictionarys["address5"][index] = ""

    # 三重城
    for index in range(DATA_SIZE):
        if splitedAddressDataDictionarys["address3"][index] == "":
            continue
        if (
            re.search("^重城", splitedAddressDataDictionarys["address4"][index])
            and splitedAddressDataDictionarys["address3"][index][-1] == "3"
        ):
            if len(splitedAddressDataDictionarys["address3"][index]) < 2:
                continue
            splitedAddressDataDictionarys["address3"][index] = splitedAddressDataDictionarys["address3"][index][:-2]
            splitedAddressDataDictionarys["address4"][index] = "三" + splitedAddressDataDictionarys["address4"][index]

    # 町屋
    for index in range(DATA_SIZE):
        if (
            splitedAddressDataDictionarys["address1"][index] == "町"
            and splitedAddressDataDictionarys["address2"][index] == "屋"
        ):
            splitedAddressDataDictionarys["address2"][index] = "町屋"
            splitedAddressDataDictionarys["address1"][index] = ""
