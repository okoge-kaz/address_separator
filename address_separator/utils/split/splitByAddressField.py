from __future__ import annotations

import pandas as pd
import utils.extract.detail.building_detail
import utils.extract.detail.check.caution
import utils.extract.detail.check.check
import utils.extract.detail.check.data_check
import utils.extract.detail.house_number
import utils.extract.detail.manipulate
import utils.extract.detail.shaping
import utils.extract.detail.shaping_building_info
import utils.extract.district
from utils.split.pullOutCityField import pull_out_city_field
from utils.split.pullOutPrefectureField import pull_out_prefecture_field
from utils.split.pullOutTownField import pull_out_town_field


def split_by_address_field(formatted_address_data_array: list[str], CSV_DATA: pd.DataFrame) -> dict[str, list[str]]:
    """
    args: CSV_DATA: pd.DataFrame
    return: splittedAddressDataDictionaries: dict[str, list[str]]

    整形作業を行う。ここでは、出力形式とは異なり独自の形での分割となっている。
    分割の形は以下の通り

        original,prefecture,city,town,district,invalid,house_number,
        special_characters,building_detail_info,building_info,
        error1,error2,caution

    """

    splitted_address_data_dictionaries: dict[str, list[str]] = {}

    # 分割処理を施す前のデータも事前に格納しておく
    splitted_address_data_dictionaries["original"] = CSV_DATA["address"].to_list()

    non_prefecture_address_data_array: list[str] = pull_out_prefecture_field(
        formatted_address_data_array, splitted_address_data_dictionaries
    )

    non_city_address_data_array: list[str] = pull_out_city_field(
        non_prefecture_address_data_array, splitted_address_data_dictionaries
    )

    non_town_address_data: list[str] = pull_out_town_field(
        non_city_address_data_array, splitted_address_data_dictionaries
    )

    district_data = utils.extract.district.extract_district(non_town_address_data)
    splitted_address_data_dictionaries["district"] = district_data[0]
    others: list = district_data[1]

    # 番地をいれる
    house_number_data = utils.extract.detail.house_number.operation(others)
    others_head: list = house_number_data[0]
    house_numbers: list = house_number_data[1]
    others_tail: list = house_number_data[2]
    splitted_address_data_dictionaries["invalid"] = others_head
    splitted_address_data_dictionaries["house_number"] = house_numbers

    # check 不正なデータが存在しないかどうかを確認
    caution: list = utils.extract.detail.check.check.check(splitted_address_data_dictionaries)

    # データ整形＋分裂してしまったデータを統合整理
    manipulated_others_tail = utils.extract.detail.manipulate.manipulate(
        splitted_address_data_dictionaries, others_tail
    )

    # ビルや建物情報の詳細を取得
    splitted_address_data_dictionaries[
        "building_detail_info"
    ] = utils.extract.detail.building_detail.extract_building_detail(splitted_address_data_dictionaries)

    # ビル情報のうちデータ散逸しているものを適切に統合
    utils.extract.detail.shaping_building_info.shaping_and_extracting_building_info(
        splitted_address_data_dictionaries, manipulated_others_tail
    )

    # others_tail内のデータを整形
    utils.extract.detail.shaping.shaping(splitted_address_data_dictionaries)

    # caution
    utils.extract.detail.check.caution.caution(splitted_address_data_dictionaries, manipulated_others_tail, caution)

    return splitted_address_data_dictionaries
