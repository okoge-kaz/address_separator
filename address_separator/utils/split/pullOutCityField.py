from utils.extract.city import extract_city


def pull_out_city_field(
    non_prefecture_address_data_array: list[str], splittedAddressDataDictionaries: dict[str, list[str]]
) -> list[str]:
    """
    pull out city field: 市区町村を抽出する

    Parameters
    ----------
    non_prefecture_address_data_array : list[str]
        都道府県を抽出した残りの住所データ
    splittedAddressDataDictionaries : dict[str, list[str]]
        分割済みの住所データ

    Returns
    -------
    non_prefecture_address_data_array: list[str]
        市区町村を抽出した残りの住所データ
    """
    city_data_tuple = extract_city(non_prefecture_address_data_array)
    splittedAddressDataDictionaries["city"] = city_data_tuple[0]

    non_city_address_data_array: list[str] = city_data_tuple[1]

    return non_city_address_data_array
