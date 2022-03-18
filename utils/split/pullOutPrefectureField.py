from utils.extract.prefecture import extract_prefecture


def pull_out_prefecture_field(formatted_address_data_array: list[str]) -> tuple[list[str], list[str]]:
    """
    args: data: list[str]
    return: prefectures, non_prefecture_address_data: tuple(list[str],list[str])
    """

    prefecture_data_array: list[str] = []
    non_prefecture_address_data_array: list = []

    for non_prefecture_address in formatted_address_data_array:
        tuple_data: tuple = extract_prefecture(non_prefecture_address)

        prefecture_data_array.append(tuple_data[0])
        non_prefecture_address_data_array.append(tuple_data[1])

    return prefecture_data_array, non_prefecture_address_data_array
