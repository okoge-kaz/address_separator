from __future__ import annotations

from utils.extract.prefecture import extract_prefecture


def pull_out_prefecture_field(
    formatted_address_data_array: list[str], splittedAddressDataDictionaries: dict[str, list[str]]
) -> list[str]:
    """
    pull out prefecture field: 都道府県を抽出する

    Parameters
    ----------
    formatted_address_data_array : list[str]
        整形済みの住所データ

    splittedAddressDataDictionaries : dict[str, list[str]]
        分割済みの住所データ

    Returns
    -------
    non_prefecture_address_data_array: list[str]
        都道府県を抽出した残りの住所データ
    """

    prefecture_data_array: list[str] = []
    non_prefecture_address_data_array: list = []

    for non_prefecture_address in formatted_address_data_array:
        tuple_data: tuple = extract_prefecture(non_prefecture_address)

        prefecture_data_array.append(tuple_data[0])
        non_prefecture_address_data_array.append(tuple_data[1])

    splittedAddressDataDictionaries["prefecture"] = prefecture_data_array

    return non_prefecture_address_data_array
