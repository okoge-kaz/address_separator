def extract_city(non_prefecture_address_data: list):
    """市、区、群、町、村の順で文字列を探索し、分割する。
    if文の順番が 市->区->郡->町->村であるのは、分割パターンの都合上最もうまくいくように
    """
    cities: list = []
    non_city_address_data: list = []

    for city_address_data in non_prefecture_address_data:
        if "市" in city_address_data:
            index: int = city_address_data.find("市")
            cities.append(city_address_data[0 : index + 1])
            if len(city_address_data) > index + 1:
                # avoid index out of range error
                non_city_address_data.append(city_address_data[index + 1 :])
            else:
                non_city_address_data.append("")
        elif "区" in city_address_data:
            index: int = city_address_data.find("区")
            cities.append(city_address_data[0 : index + 1])
            if len(city_address_data) > index + 1:
                non_city_address_data.append(city_address_data[index + 1 :])
            else:
                non_city_address_data.append("")
        elif "郡" in city_address_data:
            index: int = city_address_data.find("郡")
            cities.append(city_address_data[0 : index + 1])
            if len(city_address_data) > index + 1:
                non_city_address_data.append(city_address_data[index + 1 :])
            else:
                non_city_address_data.append("")
        elif "町" in city_address_data:
            index: int = city_address_data.find("町")
            cities.append(city_address_data[0 : index + 1])
            if len(city_address_data) > index + 1:
                non_city_address_data.append(city_address_data[index + 1 :])
            else:
                non_city_address_data.append("")
        elif "村" in city_address_data:
            index: int = city_address_data.find("村")
            cities.append(city_address_data[0 : index + 1])
            if len(city_address_data) > index + 1:
                non_city_address_data.append(city_address_data[index + 1 :])
            else:
                non_city_address_data.append("")
        else:
            cities.append("")
            non_city_address_data.append(city_address_data)
    return (cities, non_city_address_data)
