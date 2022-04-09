from __future__ import annotations

from utils.extract.house_number import extract_house_number


def pull_out_housenumber_invalid_field(others: list[str], AddressDataForFormatting) -> list[str]:
    """
    args: others: list[str], AddressDataForFormatting
    return: others_tail: list[str]
    """

    house_number_data_tuple = extract_house_number(others)
    AddressDataForFormatting.invalid = house_number_data_tuple[0]
    AddressDataForFormatting.house_number = house_number_data_tuple[1]

    others_tail: list[str] = house_number_data_tuple[2]

    return others_tail
