def pull_out_district_field(non_town_address_data: str) -> tuple[str, str]:
    """_summary_

    Args:
        non_town_address_data (str):

    Returns:
        tuple[str, str]:
    """
    DISTRICT_NUMBERS: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    # 数字が現れるまでを記録する

    for index in range(len(non_town_address_data)):
        if non_town_address_data[index] in DISTRICT_NUMBERS:
            return (non_town_address_data[0:index], non_town_address_data[index:])

    return ("", non_town_address_data)
