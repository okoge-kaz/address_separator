from __future__ import annotations

import re


def reshape_exceptional_address_address_data_array(address_data_array: list[str]) -> None:
    """
    args: 住所データ
    return: void, 配列データ自体を修正する
    """

    ADDRESS_ARRAY_SIZE: int = len(address_data_array)

    # ‐ -> - 変換
    for index in range(ADDRESS_ARRAY_SIZE):
        address_data_array[index] = re.sub("‐", "-", address_data_array[index])

    # ｰ -> - 変換
    for index in range(ADDRESS_ARRAY_SIZE):
        address_data_array[index] = re.sub("ｰ", "-", address_data_array[index])

    # 文字化け関連
    for index in range(ADDRESS_ARRAY_SIZE):
        # アパ-ト
        address_data_array[index] = re.sub("アパ-ト", "アパート", address_data_array[index])
        # コ-ポ
        address_data_array[index] = re.sub("コ-ポ", "コーポ", address_data_array[index])
        # フラワ-
        address_data_array[index] = re.sub("フラワ-", "フラワー", address_data_array[index])
        # ベリ-ズコ-ト
        address_data_array[index] = re.sub("ベリ-ズコ-ト", "ベリーズコート", address_data_array[index])
        # パ-クハイム
        address_data_array[index] = re.sub("パ-クハイム", "パークハイム", address_data_array[index])
        # パ-クハウス
        address_data_array[index] = re.sub("パ-クハウス", "パークハウス", address_data_array[index])
        # テ-ラ-
        address_data_array[index] = re.sub("テ-ラ-", "テーラー", address_data_array[index])

    # -が2回連続する箇所を-に直す
    for index in range(ADDRESS_ARRAY_SIZE):
        address_data_array[index] = re.sub("-{1,}", "-", address_data_array[index])

    # -の を -に置換する
    for index in range(ADDRESS_ARRAY_SIZE):
        if re.search("-の[0-9]+", address_data_array[index]):
            address_data_array[index] = re.sub("-の", "-", address_data_array[index])
        if re.search("[0-9]+の[0-9]+", address_data_array[index]):
            shaped_string: str = ""
            for id in range(len(address_data_array[index])):
                if address_data_array[index][id] == "の" and id > 0 and id + 1 < len(address_data_array[index]):
                    if (
                        "0" <= address_data_array[index][id - 1]
                        and address_data_array[index][id - 1] <= "9"
                        and address_data_array[index][id + 1] >= "0"
                        and address_data_array[index][id + 1] <= "9"
                    ):
                        # 〜の〜 前後が数字であるとき
                        shaped_string += "-"
                    else:
                        shaped_string += address_data_array[index][id]
                else:
                    shaped_string += address_data_array[index][id]
            address_data_array[index] = shaped_string
