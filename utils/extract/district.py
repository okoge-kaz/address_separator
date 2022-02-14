def extract_district(non_town_address_data: list):
    """prefecture, city, townによって除かれたデータのうち数字が出現するまでのデータをとる"""
    districts: list = []
    others: list = []

    def extract_district(string: str):
        district_numbers: list = []
        for i in range(0, 10):
            district_numbers.append(str(i))
        # 数字が現れるまでを記録する
        for i in range(len(string)):
            if string[i] in district_numbers:
                return (string[0:i], string[i:])
        return ("", string)

    for district_data in non_town_address_data:
        district_tuple_data = extract_district(district_data)
        districts.append(district_tuple_data[0])
        others.append(district_tuple_data[1])
    return (districts, others)
