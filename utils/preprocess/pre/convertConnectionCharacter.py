import re


def convertConnectionCharacter(address_data: str) -> str:
    """
    args: address_data: str (example: 東京都港区元麻布1 6/9)
    return: formatted_address_data: str (example: 東京都港区元麻布1-6-9)
    """
    address_data = re.sub(" ", "-", address_data)
    address_data = re.sub("　", "-", address_data)
    address_data = re.sub("\t", "-", address_data)
    # 日本語で数字をつなぐ際に出現しうる
    address_data = re.sub("−", "-", address_data)
    address_data = re.sub("─", "-", address_data)
    address_data = re.sub("—", "-", address_data)
    # 改行を半角スペースで置き換える
    address_data = re.sub("\n", "-", address_data)
    # 正規表現で/を-に置き換える
    formatted_address_data = re.sub("/", "-", address_data)
    return formatted_address_data
