import re


def convert_japanese_style_number_to_alabic_number(address_data: str) -> str:
    """
    args: address_data: str (example: 東京都港区元麻布1-六-9)
    return: formatted_address_data: str (example: 東京都港区元麻布1-6-9)
    """

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

    response: str = ""

    for character in address_data:

        _formatted_character: str = ""
        _formatted_character += character

        if re.search("[０-９]", _formatted_character):
            response += MAPPING_DICTIONARY[_formatted_character]
        else:
            response += _formatted_character

    formatted_address_data: str = response

    return formatted_address_data
