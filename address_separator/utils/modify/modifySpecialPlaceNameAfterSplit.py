from __future__ import annotations

import re


def modify_special_place_name(splitted_address_data_dictionaries: dict[str, list[str]]) -> None:
    """
    args: splitted_address_data_dictionaries (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void

    各ケースごとに処理を行う
    地名が特殊であるために、うまく分割できなかったものを再整形している
    ルールベースなため、完全網羅は不可能

    """

    DATA_SIZE: int = len(splitted_address_data_dictionaries["address3"])

    # 一宮
    for index in range(DATA_SIZE):
        if (
            splitted_address_data_dictionaries["address3"][index] == "1"
            and splitted_address_data_dictionaries["address4"][index] == "宮"
        ):
            if splitted_address_data_dictionaries["address2"][index] != "":
                splitted_address_data_dictionaries["error1"][
                    index
                ] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitted_address_data_dictionaries["address2"][index] = "一宮"
                splitted_address_data_dictionaries["address3"][index] = splitted_address_data_dictionaries["address5"][
                    index
                ]
                splitted_address_data_dictionaries["address4"][index] = ""
                splitted_address_data_dictionaries["address5"][index] = ""

    # 一宮徳谷
    for index in range(DATA_SIZE):
        if (
            splitted_address_data_dictionaries["address3"][index] == "1"
            and splitted_address_data_dictionaries["address4"][index] == "宮徳谷"
        ):
            if splitted_address_data_dictionaries["address2"][index] != "":
                splitted_address_data_dictionaries["error1"][
                    index
                ] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitted_address_data_dictionaries["address2"][index] = "一宮徳谷"
                splitted_address_data_dictionaries["address3"][index] = splitted_address_data_dictionaries["address5"][
                    index
                ]
                splitted_address_data_dictionaries["address4"][index] = ""
                splitted_address_data_dictionaries["address5"][index] = ""

    # 五台山
    for index in range(DATA_SIZE):
        if (
            splitted_address_data_dictionaries["address3"][index] == "5"
            and splitted_address_data_dictionaries["address4"][index] == "台山"
        ):
            if splitted_address_data_dictionaries["address2"][index] != "":
                splitted_address_data_dictionaries["error1"][
                    index
                ] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitted_address_data_dictionaries["address2"][index] = "五台山"
                splitted_address_data_dictionaries["address3"][index] = splitted_address_data_dictionaries["address5"][
                    index
                ]
                splitted_address_data_dictionaries["address4"][index] = ""
                splitted_address_data_dictionaries["address5"][index] = ""

    # 五台山〜
    for index in range(DATA_SIZE):
        if splitted_address_data_dictionaries["address3"][index] == "5" and re.search(
            "^台山.+", splitted_address_data_dictionaries["address4"][index]
        ):
            if splitted_address_data_dictionaries["address2"][index] != "":
                splitted_address_data_dictionaries["error1"][
                    index
                ] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitted_address_data_dictionaries["address2"][index] = ""
                splitted_address_data_dictionaries["address3"][index] = ""
                splitted_address_data_dictionaries["address4"][index] = (
                    "五" + splitted_address_data_dictionaries["address4"][index]
                )

    # 三谷
    for index in range(DATA_SIZE):
        if (
            splitted_address_data_dictionaries["address3"][index] == "3"
            and splitted_address_data_dictionaries["address4"][index] == "谷"
        ):
            if splitted_address_data_dictionaries["address2"][index] != "":
                splitted_address_data_dictionaries["error1"][
                    index
                ] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitted_address_data_dictionaries["address2"][index] = "三谷"
                splitted_address_data_dictionaries["address3"][index] = splitted_address_data_dictionaries["address5"][
                    index
                ]
                splitted_address_data_dictionaries["address4"][index] = ""
                splitted_address_data_dictionaries["address5"][index] = ""

    # 三原
    for index in range(DATA_SIZE):
        if (
            splitted_address_data_dictionaries["address3"][index] == "3"
            and splitted_address_data_dictionaries["address4"][index] == "原"
        ):
            if splitted_address_data_dictionaries["address2"][index] != "":
                splitted_address_data_dictionaries["error1"][
                    index
                ] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                splitted_address_data_dictionaries["address2"][index] = "三原"
                splitted_address_data_dictionaries["address3"][index] = splitted_address_data_dictionaries["address5"][
                    index
                ]
                splitted_address_data_dictionaries["address4"][index] = ""
                splitted_address_data_dictionaries["address5"][index] = ""

    # 三重城
    for index in range(DATA_SIZE):
        if splitted_address_data_dictionaries["address3"][index] == "":
            continue
        if (
            re.search("^重城", splitted_address_data_dictionaries["address4"][index])
            and splitted_address_data_dictionaries["address3"][index][-1] == "3"
        ):
            if len(splitted_address_data_dictionaries["address3"][index]) < 2:
                continue
            splitted_address_data_dictionaries["address3"][index] = splitted_address_data_dictionaries["address3"][
                index
            ][:-2]
            splitted_address_data_dictionaries["address4"][index] = (
                "三" + splitted_address_data_dictionaries["address4"][index]
            )

    # 町屋
    for index in range(DATA_SIZE):
        if (
            splitted_address_data_dictionaries["address1"][index] == "町"
            and splitted_address_data_dictionaries["address2"][index] == "屋"
        ):
            splitted_address_data_dictionaries["address2"][index] = "町屋"
            splitted_address_data_dictionaries["address1"][index] = ""
