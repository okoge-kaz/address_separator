import re


def modify_special_place_name(AddressDataForOutput: dict[str, list[str]]) -> None:
    """
    args: AddressDataForOutput (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void

    各ケースごとに処理を行う
    地名が特殊であるために、うまく分割できなかったものを再整形している
    ルールベースなため、完全網羅は不可能

    """

    DATA_SIZE: int = len(AddressDataForOutput["address3"])

    # 一宮
    for index in range(DATA_SIZE):
        if (
            AddressDataForOutput["address3"][index] == "1"
            and AddressDataForOutput["address4"][index] == "宮"
        ):
            if AddressDataForOutput["address2"][index] != "":
                AddressDataForOutput["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                AddressDataForOutput["address2"][index] = "一宮"
                AddressDataForOutput["address3"][index] = AddressDataForOutput["address5"][index]
                AddressDataForOutput["address4"][index] = ""
                AddressDataForOutput["address5"][index] = ""

    # 一宮徳谷
    for index in range(DATA_SIZE):
        if (
            AddressDataForOutput["address3"][index] == "1"
            and AddressDataForOutput["address4"][index] == "宮徳谷"
        ):
            if AddressDataForOutput["address2"][index] != "":
                AddressDataForOutput["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                AddressDataForOutput["address2"][index] = "一宮徳谷"
                AddressDataForOutput["address3"][index] = AddressDataForOutput["address5"][index]
                AddressDataForOutput["address4"][index] = ""
                AddressDataForOutput["address5"][index] = ""

    # 五台山
    for index in range(DATA_SIZE):
        if (
            AddressDataForOutput["address3"][index] == "5"
            and AddressDataForOutput["address4"][index] == "台山"
        ):
            if AddressDataForOutput["address2"][index] != "":
                AddressDataForOutput["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                AddressDataForOutput["address2"][index] = "五台山"
                AddressDataForOutput["address3"][index] = AddressDataForOutput["address5"][index]
                AddressDataForOutput["address4"][index] = ""
                AddressDataForOutput["address5"][index] = ""

    # 五台山〜
    for index in range(DATA_SIZE):
        if AddressDataForOutput["address3"][index] == "5" and re.search(
            "^台山.+", AddressDataForOutput["address4"][index]
        ):
            if AddressDataForOutput["address2"][index] != "":
                AddressDataForOutput["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                AddressDataForOutput["address2"][index] = ""
                AddressDataForOutput["address3"][index] = ""
                AddressDataForOutput["address4"][index] = (
                    "五" + AddressDataForOutput["address4"][index]
                )

    # 三谷
    for index in range(DATA_SIZE):
        if (
            AddressDataForOutput["address3"][index] == "3"
            and AddressDataForOutput["address4"][index] == "谷"
        ):
            if AddressDataForOutput["address2"][index] != "":
                AddressDataForOutput["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                AddressDataForOutput["address2"][index] = "三谷"
                AddressDataForOutput["address3"][index] = AddressDataForOutput["address5"][index]
                AddressDataForOutput["address4"][index] = ""
                AddressDataForOutput["address5"][index] = ""

    # 三原
    for index in range(DATA_SIZE):
        if (
            AddressDataForOutput["address3"][index] == "3"
            and AddressDataForOutput["address4"][index] == "原"
        ):
            if AddressDataForOutput["address2"][index] != "":
                AddressDataForOutput["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                AddressDataForOutput["address2"][index] = "三原"
                AddressDataForOutput["address3"][index] = AddressDataForOutput["address5"][index]
                AddressDataForOutput["address4"][index] = ""
                AddressDataForOutput["address5"][index] = ""

    # 三重城
    for index in range(DATA_SIZE):
        if AddressDataForOutput["address3"][index] == "":
            continue
        if (
            re.search("^重城", AddressDataForOutput["address4"][index])
            and AddressDataForOutput["address3"][index][-1] == "3"
        ):
            if len(AddressDataForOutput["address3"][index]) < 2:
                continue
            AddressDataForOutput["address3"][index] = AddressDataForOutput["address3"][index][:-2]
            AddressDataForOutput["address4"][index] = "三" + AddressDataForOutput["address4"][index]

    # 町屋
    for index in range(DATA_SIZE):
        if (
            AddressDataForOutput["address1"][index] == "町"
            and AddressDataForOutput["address2"][index] == "屋"
        ):
            AddressDataForOutput["address2"][index] = "町屋"
            AddressDataForOutput["address1"][index] = ""
