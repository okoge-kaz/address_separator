from __future__ import annotations

from utils.extract.town import extract_town


def pull_out_town_field(non_city_address_data_array: list[str], AddressDataForFormatting) -> list[str]:
    """
    args: non_city_address_data_array: list[str], AddressDataForFormatting
    return: non_town_address_data_array: list[str]
    """
    town_data_tuple = extract_town(non_city_address_data_array)
    AddressDataForFormatting.town = town_data_tuple[0]

    non_town_address_data_array: list[str] = town_data_tuple[1]

    return non_town_address_data_array
