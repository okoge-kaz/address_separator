import re


def convert_japanese_style_number_to_alabic_number(address_data: str) -> str:
    """
    args: address_data: str (example: 東京都港区元麻布1-六-9)
    return: formatted_address_data: str (example: 東京都港区元麻布1-6-9)
    """

    JAPANESE_STYLE_NUMBER: list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "〇"]
    MAPPING_DICTIONARY: dict = {
        "１": "1",
        "２": "2",
        "３": "3",
        "４": "4",
        "５": "5",
        "６": "6",
        "７": "7",
        "８": "8",
        "９": "9",
        "０": "0",
    }
    DICTIONARY_JAPANESE_STYLE_NUMBER: dict = {
        "一": "1",
        "二": "2",
        "三": "3",
        "四": "4",
        "五": "5",
        "六": "6",
        "七": "7",
        "八": "8",
        "九": "9",
        "十": "10",
        "〇": "0",
    }

    response: str = ""

    for character in address_data:

        _formatted_character: str = ""
        # if character in JAPANESE_STYLE_NUMBER:
        #     # 漢数字を算用数字に変換
        #     _formatted_character += DICTIONARY_JAPANESE_STYLE_NUMBER[character]
        # else:
        #     _formatted_character += character
        _formatted_character += character

        if re.search("[０-９]", _formatted_character):
            response += MAPPING_DICTIONARY[_formatted_character]
        else:
            response += _formatted_character

    formatted_address_data: str = response

    return formatted_address_data
