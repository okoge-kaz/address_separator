from utils.extract.prefecture import extract_prefecture


def pull_out_prefecture_field(
    formatted_address_data_array: list[str], AddressDataForFormatting) -> list[str]:
    """
    args: formatted_address_data_array: list[str], AddressDataForFormatting: dict[str, list[str]]
    return: non_prefecture_address_data: list[str]
    """

    prefecture_data_array: list[str] = []
    non_prefecture_address_data_array: list = []

    for non_prefecture_address in formatted_address_data_array:
        tuple_data: tuple = extract_prefecture(non_prefecture_address)

        prefecture_data_array.append(tuple_data[0])
        non_prefecture_address_data_array.append(tuple_data[1])

    AddressDataForFormatting.prefecture = prefecture_data_array

    return non_prefecture_address_data_array
