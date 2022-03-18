from utils.extract.city import extract_city


def pull_out_city_field(
    non_prefecture_address_data_array: list[str], splitedAddressDataDictionarys: dict[str, list[str]]
) -> list[str]:
    """
    args: non_prefecture_address_data_array: list[str], splitedAddressDataDictionarys: dict[str, list[str]]
    return: non_city_address_data_array: list[str]
    """
    city_data_tuple = extract_city(non_prefecture_address_data_array)
    splitedAddressDataDictionarys["city"] = city_data_tuple[0]

    non_city_address_data_array: list[str] = city_data_tuple[1]

    return non_city_address_data_array
