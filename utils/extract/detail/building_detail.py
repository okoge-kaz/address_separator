import re


def extract_building_detail(AddressDataForFormatting) -> list:
    """
    args: AddressDataForFormatting
    return: building_detail_info: list
    special_chractersのなかの F のみ抽出
    """
    building_detail_info: list = []

    def find_F(string: str) -> bool:
        """
        args: string: str
        return: bool
        special_charactersに存在するFという文字単体を検知する
        """
        if string == "F":
            return True
        else:
            return False

    def cutting_number_from_last(index: int) -> None:
        """
        args: index: int
        rturn: void
        上記の関数と同時に使用する。8Fのように、建物の階数情報のみを抽出する
        """
        if re.search("-([0-9]+)$", AddressDataForFormatting.house_number[index]) is None:
            print("something wrong1")  # for debug
        else:

            start: int = 0
            end: int = 0

            regular_expression_start = re.search("-([0-9]+)$", AddressDataForFormatting.house_number[index])
            if regular_expression_start is not None:
                start = regular_expression_start.start()

            regular_expression_end = re.search("-([0-9]+)$", AddressDataForFormatting.house_number[index])
            if regular_expression_end is not None:
                end = regular_expression_end.end()

            if end != len(AddressDataForFormatting.house_number[index]):
                print("index which driven by regular expression is something wrong.")  # for debug
            # start+1 にしているのは-{数字}Fとなっているので - を除いている
            building_detail_info.append(AddressDataForFormatting.house_number[index][start + 1 : end] + "F")
            AddressDataForFormatting.house_number[index] = AddressDataForFormatting.house_number[index][:start]

    for i in range(len(AddressDataForFormatting.special_characters)):
        if find_F(AddressDataForFormatting.special_characters[i]):
            # 空白に変える
            AddressDataForFormatting.special_characters[i] = ""
            # special_charactersから数字をfetch
            cutting_number_from_last(i)
        else:
            building_detail_info.append("")
    return building_detail_info
