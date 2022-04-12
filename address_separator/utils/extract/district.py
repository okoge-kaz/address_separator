from __future__ import annotations

from utils.split.pullOutDistrictField import pull_out_district_field


def extract_district(non_town_address_data_list: list[str]) -> tuple[list[str], list[str]]:
    """
    extract district: 市区町村を抽出する(prefecture, city, townによって除かれたデータのうち数字が出現するまでのデータをとる)

    Parameters
    ----------
    non_town_address_data : list[str]
        都道府県を抽出した残りの住所データ

    Returns
    -------

    """
    districts_data_list: list[str] = []
    other_address_data_list: list[str] = []

    for non_town_address_data in non_town_address_data_list:

        district_tuple_data = pull_out_district_field(non_town_address_data)

        districts_data_list.append(district_tuple_data[0])
        other_address_data_list.append(district_tuple_data[1])

    return (districts_data_list, other_address_data_list)
