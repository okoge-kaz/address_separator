from __future__ import annotations

import re


def extract_building_detail(splitted_address_data_dictionaries: dict[str, list[str]]):
    # special_chractersのなかの F のみ抽出
    building_detail_info: list = []

    def find_F(string: str):
        """special_charactersに存在するFという文字単体を検知する"""
        if string == "F":
            return True
        else:
            return False

    def cutting_number_from_last(index: int):
        """上記の関数と同時に使用する。8Fのように、建物の階数情報のみを抽出する"""
        if re.search("-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index]) is None:
            print("something wrong1")  # for debug
        else:

            start: int = 0
            end: int = 0

            regular_expression_start = re.search(
                "-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index]
            )
            if regular_expression_start is not None:
                start = regular_expression_start.start()

            regular_expression_end = re.search("-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index])
            if regular_expression_end is not None:
                end = regular_expression_end.end()

            if end != len(splitted_address_data_dictionaries["house_number"][index]):
                print("index which driven by regular expression is something wrong.")  # for debug
            # start+1 にしているのは-{数字}Fとなっているので - を除いている
            building_detail_info.append(
                splitted_address_data_dictionaries["house_number"][index][start + 1 : end] + "F"
            )
            splitted_address_data_dictionaries["house_number"][index] = splitted_address_data_dictionaries[
                "house_number"
            ][index][:start]

    for i in range(len(splitted_address_data_dictionaries["special_characters"])):
        if find_F(splitted_address_data_dictionaries["special_characters"][i]):
            # 空白に変える
            splitted_address_data_dictionaries["special_characters"][i] = ""
            # special_charactersから数字をfetch
            cutting_number_from_last(i)
        else:
            building_detail_info.append("")
    return building_detail_info
