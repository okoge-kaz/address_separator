import re

from utils.preprocess.pre.convert_connection_character import convert_connection_character
from utils.preprocess.pre.convert_japanese_style_number_to_alabic_number import convert_japanese_style_number_to_alabic_number


def process_japanese_style_address_expression(address_data: str) -> str:
    """
    args: 住所文字列 (example: 東京都港区元麻布1丁目6番地)
    return: 変換後の住所文字列 (example: 東京都港区元麻布1-6)

    detail: 丁目, 番, 番地 という日本語表現を - に変換する処理を行う
    """
    if "丁目" in address_data:
        address_data = re.sub("丁目", "-", address_data)
    if "番地" in address_data:
        address_data = re.sub("番地", "-", address_data)
    if "番" in address_data:
        address_data = re.sub("番", "-", address_data)
    if "の" in address_data:

        while re.search("[0-9 ０-９]+の[0-9 ０-９]", address_data) is not None:
            """
            address_data: str 内部に全角、半角を問わず 〜の〜 という表現が存在する限りwhileループを回す
            """
            start: int = 0
            end: int = 0

            regular_expression_start = re.search("[0-9 ０-９]+の[0-9 ０-９]", address_data)
            if regular_expression_start is not None:
                start = regular_expression_start.start()

            regular_expression_end = re.search("[0-9 ０-９]+の[0-9 ０-９]", address_data)
            if regular_expression_end is not None:
                end = regular_expression_end.end()

            res: str = ""
            res += address_data[:start]
            for index in range(start, end):
                if address_data[index] == "の":
                    res += "-"
                else:
                    if re.search("[０-９]", address_data[index]) is not None:
                        mapping_dictionary: dict = {
                            "１": "1",
                            "２": "2",
                            "３": "3",
                            "４": "4",
                            "５": "5",
                            "６": "6",
                            "７": "7",
                            "８": "8",
                            "９": "9",
                            "０": "10",
                        }
                        res += mapping_dictionary[address_data[index]]
                    else:
                        res += address_data[index]
            res += address_data[end:]
            address_data = res

    formatted_address_data = address_data.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))

    # 文字列の最終部に存在する - を削除する
    if len(formatted_address_data) > 0:
        """
        avoid potential bug: if formatted_address_data's length is 0: then index out of range occurs
        """
        if formatted_address_data[-1] == "-":
            formatted_address_data = formatted_address_data[0:-1]

    # つなぎ文字を - に変換
    formatted_address_data = convert_connection_character(formatted_address_data)

    # 漢数字 と 全角数字を変換
    formatted_address_data = convert_japanese_style_number_to_alabic_number(formatted_address_data)

    formatted_address_data = re.sub("ー", "-", formatted_address_data)

    return formatted_address_data
