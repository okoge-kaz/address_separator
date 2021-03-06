from __future__ import annotations

import re


def shaping_and_extracting_building_info(
    splitted_address_data_dictionaries: dict[str, list[str]], manipulated_others_tail: list
):
    """ビル名、建物名など、building_infoに含まれる。または、building_detail_infoに含まれるデータを抽出、整形する"""

    def find_kai(string: str):
        """階という文字単体が配列manipulated_others_tailに存在する場合検知する"""
        if string == "階":
            return True
        else:
            return False

    def cutting_number_from_last2(index: int):
        """上記の関数と同時に使用する。8階のように、建物の階数情報のみを抽出する"""
        if re.search("-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index]) is None:
            print(index)  # for debug
            print(re.search("-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index]))
            print(splitted_address_data_dictionaries["house_number"][index])
            print("something wrong1")  # for debug
        else:
            start: int = re.search("-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index]).start()
            end: int = re.search("-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index]).end()
            if end != len(splitted_address_data_dictionaries["house_number"][index]):
                print("somethin wrong2")  # for debug
            # start+1 にしているのは-{数字}階となっているので - を除いている
            splitted_address_data_dictionaries["building_detail_info"][index] = (
                splitted_address_data_dictionaries["house_number"][index][start + 1 : end] + "階"
            )
            splitted_address_data_dictionaries["house_number"][index] = splitted_address_data_dictionaries[
                "house_number"
            ][index][:start]

    for i in range(len(manipulated_others_tail)):
        if find_kai(manipulated_others_tail[i]):
            # 空白に変える
            manipulated_others_tail[i] = ""
            # special_charactersから数字をfetch
            cutting_number_from_last2(i)
        else:
            pass

    def find_gou(string: str):
        """号という文字単体が配列manipulated_others_tailに存在する場合検知する"""
        if string == "号":
            return True
        else:
            return False

    def cutting_number_from_last3(index: int):
        """上記の関数と同時に使用する。8号のように、建物の階数情報のみを抽出する"""
        if re.search("-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index]) is None:
            print(index)
            print(re.search("-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index]))
            print(splitted_address_data_dictionaries["house_number"][index])
            print("something wrong1")  # for debug
        else:
            start: int = re.search("-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index]).start()
            end: int = re.search("-([0-9]+)$", splitted_address_data_dictionaries["house_number"][index]).end()
            if end != len(splitted_address_data_dictionaries["house_number"][index]):
                print("somethin wrong2")  # for debug
            # start+1 にしているのは-{数字}階となっているので - を除いている
            splitted_address_data_dictionaries["building_detail_info"][index] = (
                splitted_address_data_dictionaries["house_number"][index][start + 1 : end] + "号"
            )
            splitted_address_data_dictionaries["house_number"][index] = splitted_address_data_dictionaries[
                "house_number"
            ][index][:start]

    for i in range(len(manipulated_others_tail)):
        if find_gou(manipulated_others_tail[i]):
            # 空白に変える
            manipulated_others_tail[i] = ""
            # special_charactersから数字をfetch
            cutting_number_from_last3(i)
        else:
            pass

    # '-(([0-9 A-Z])+)号$' のような情報を抽出する

    def extract_building_detail_info_from_others_tail_1(index: int):
        """501号のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[0-9]+号$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[0-9]+号$", manipulated_others_tail[index]).start()
            end: int = re.search("[0-9]+号$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            splitted_address_data_dictionaries["building_detail_info"][index] = (
                building_info + splitted_address_data_dictionaries["building_detail_info"][index]
            )
        else:
            pass

    def extract_building_detail_info_from_others_tail_2(index: int):
        """401のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("(([0-9]+)-)*[0-9]+$", manipulated_others_tail[index]) is not None:
            start: int = re.search("(([0-9]+)-)*[0-9]+$", manipulated_others_tail[index]).start()
            end: int = re.search("(([0-9]+)-)*[0-9]+$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            splitted_address_data_dictionaries["building_detail_info"][index] = (
                building_info + splitted_address_data_dictionaries["building_detail_info"][index]
            )
        else:
            pass

    def extract_building_detail_info_from_others_tail_3(index: int):
        """45号館のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[0-9]+号館$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[0-9]+号館$", manipulated_others_tail[index]).start()
            end: int = re.search("[0-9]+号館$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            splitted_address_data_dictionaries["building_detail_info"][index] = (
                building_info + splitted_address_data_dictionaries["building_detail_info"][index]
            )
        else:
            pass

    def extract_building_detail_info_from_others_tail_4(index: int):
        """C号のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("-[A-Z]号$", manipulated_others_tail[index]) is not None:
            start: int = re.search("-[A-Z]号$", manipulated_others_tail[index]).start()
            end: int = re.search("-[A-Z]号$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            splitted_address_data_dictionaries["building_detail_info"][index] = (
                building_info + splitted_address_data_dictionaries["building_detail_info"][index]
            )
        else:
            pass

    def extract_building_detail_info_from_others_tail_5(index: int):
        """C館のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[A-Z]館$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[A-Z]館$", manipulated_others_tail[index]).start()
            end: int = re.search("[A-Z]館$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            splitted_address_data_dictionaries["building_detail_info"][index] = (
                building_info + splitted_address_data_dictionaries["building_detail_info"][index]
            )
        else:
            pass

    def extract_building_detail_info_from_others_tail_6(index: int):
        """45号館のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[0-9]+号室$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[0-9]+号室$", manipulated_others_tail[index]).start()
            end: int = re.search("[0-9]+号室$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            splitted_address_data_dictionaries["building_detail_info"][index] = (
                building_info + splitted_address_data_dictionaries["building_detail_info"][index]
            )
        else:
            pass

    def extract_building_detail_info_from_others_tail_7(index: int):
        """45Fのようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[0-9]+F$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[0-9]+F$", manipulated_others_tail[index]).start()
            end: int = re.search("[0-9]+F$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            splitted_address_data_dictionaries["building_detail_info"][index] = (
                building_info + splitted_address_data_dictionaries["building_detail_info"][index]
            )
        else:
            pass

    def extract_building_detail_info_from_others_tail_8(index: int):
        """45階のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[0-9]+階$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[0-9]+階$", manipulated_others_tail[index]).start()
            end: int = re.search("[0-9]+階$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            splitted_address_data_dictionaries["building_detail_info"][index] = (
                building_info + splitted_address_data_dictionaries["building_detail_info"][index]
            )
        else:
            pass

    def extract_building_detail_info_from_others_tail_9(index: int):
        """最後が-のものを取り除く"""
        if re.search("-$", manipulated_others_tail[index]) is not None:
            start: int = re.search("-$", manipulated_others_tail[index]).start()
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
        else:
            pass

    for index in range(len(manipulated_others_tail)):
        extract_building_detail_info_from_others_tail_1(index)
        extract_building_detail_info_from_others_tail_2(index)
        extract_building_detail_info_from_others_tail_3(index)
        extract_building_detail_info_from_others_tail_4(index)
        extract_building_detail_info_from_others_tail_5(index)
        extract_building_detail_info_from_others_tail_6(index)
        extract_building_detail_info_from_others_tail_7(index)
        extract_building_detail_info_from_others_tail_8(index)
        extract_building_detail_info_from_others_tail_9(index)
