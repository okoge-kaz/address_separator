from utils.extract.town import extract_town


def pull_out_town_field(
    non_city_address_data_array: list[str], splittedAddressDataDictionaries: dict[str, list[str]]
) -> list[str]:
    """
    pull out town field: 市区町村を抽出する

    Parameters
    ----------
    non_city_address_data_array : list[str]
        都道府県を抽出した残りの住所データ
    splittedAddressDataDictionaries : dict[str, list[str]]
        分割済みの住所データ

    Returns
    -------
    non_city_address_data_array: list[str]
        市区町村を抽出した残りの住所データ
    """
    town_data_tuple: tuple[list[str], list[str]] = extract_town(non_city_address_data_array)
    splittedAddressDataDictionaries["town"] = town_data_tuple[0]

    non_town_address_data_array: list[str] = town_data_tuple[1]

    return non_town_address_data_array
