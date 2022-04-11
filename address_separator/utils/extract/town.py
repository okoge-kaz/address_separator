def extract_town(non_city_address_data: list):
    """
    市町村よりさらに細かな地区行政区分を文字列から取得する
    """
    towns: list = []
    non_town_address_data: list = []

    for town_address_data in non_city_address_data:
        if "区" in town_address_data:
            index: int = town_address_data.find("区")
            towns.append(town_address_data[0 : index + 1])
            if len(town_address_data) > index + 1:
                # avoid index out of range error
                non_town_address_data.append(town_address_data[index + 1 :])
            else:
                non_town_address_data.append("")
        elif "郡" in town_address_data:
            index: int = town_address_data.find("郡")
            towns.append(town_address_data[0 : index + 1])
            if len(town_address_data) > index + 1:
                non_town_address_data.append(town_address_data[index + 1 :])
            else:
                non_town_address_data.append("")
        elif "町" in town_address_data:
            index: int = town_address_data.find("町")
            towns.append(town_address_data[0 : index + 1])
            if len(town_address_data) > index + 1:
                non_town_address_data.append(town_address_data[index + 1 :])
            else:
                non_town_address_data.append("")
        elif "村" in town_address_data:
            index: int = town_address_data.find("村")
            towns.append(town_address_data[0 : index + 1])
            if len(town_address_data) > index + 1:
                non_town_address_data.append(town_address_data[index + 1 :])
            else:
                non_town_address_data.append("")
        else:
            towns.append("")
            non_town_address_data.append(town_address_data)
    return (towns, non_town_address_data)
