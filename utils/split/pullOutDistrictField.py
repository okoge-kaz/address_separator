from __future__ import annotations

from utils.extract.district import extract_district


def pull_out_district_field(non_town_address_data_array: list[str], AddressDataForFormatting) -> list[str]:
    """
    args: non_town_address_data_array: list[str], AddressDataForFormatting
    return: others: list[str]
    """
    district_data_tuple = extract_district(non_town_address_data_array)
    AddressDataForFormatting.district = district_data_tuple[0]

    others: list[str] = district_data_tuple[1]

    return others
