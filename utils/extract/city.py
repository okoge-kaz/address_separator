def extract_city(non_prefacture_address_data: list):
    cities: list = []
    non_city_address_data: list = []

    for city_address_data in non_prefacture_address_data:
        if "市" in city_address_data:
            index: int = city_address_data.find("市")
            cities.append(city_address_data[0: index + 1])
            if len(city_address_data) > index + 1:
                # index out of rangeを避けるため
                non_city_address_data.append(city_address_data[index + 1:])
        elif "区" in city_address_data:
            index: int = city_address_data.find("区")
            cities.append(city_address_data[0:index + 1])
            if len(city_address_data) > index + 1:
                # index out of rangeを避けるため
                non_city_address_data.append(city_address_data[index + 1:])
        elif "郡" in city_address_data:
            index: int = city_address_data.find("郡")
            cities.append(city_address_data[0:index + 1])
            if len(city_address_data) > index + 1:
                # index out of rangeを避けるため
                non_city_address_data.append(city_address_data[index + 1:])
        elif "町" in city_address_data:
            index: int = city_address_data.find("町")
            cities.append(city_address_data[0:index + 1])
            if len(city_address_data) > index + 1:
                # index out of rangeを避けるため
                non_city_address_data.append(city_address_data[index + 1:])
        elif "村" in city_address_data:
            index: int = city_address_data.find("村")
            cities.append(city_address_data[0:index + 1])
            if len(city_address_data) > index + 1:
                # index out of rangeを避けるため
                non_city_address_data.append(city_address_data[index + 1:])
        else:
            cities.append("")
            non_city_address_data.append(city_address_data)
    return (cities, non_city_address_data)
