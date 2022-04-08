import pandas as pd
import utils.extract.detail.building_detail
import utils.extract.detail.check.caution
import utils.extract.detail.check.check
import utils.extract.detail.check.data_check
import utils.extract.detail.manipulate
import utils.extract.detail.shaping
import utils.extract.detail.shaping_building_info
import utils.extract.district
from utils.dataclass.HomemadeClass import make_DataclassForFormatting
from utils.split.pullOutCityField import pull_out_city_field
from utils.split.pullOutPrefectureField import pull_out_prefecture_field
from utils.split.pullOutTownField import pull_out_town_field
from utils.split.pullOutDistrictField import pull_out_district_field
from utils.split.pullOutHouseNumberAndInvalidField import pull_out_housenumber_invalid_field

def split_by_address_field(formatted_address_data_array: list[str], CSV_DATA: pd.DataFrame):
    """
    args: CSV_DATA: pd.DataFrame
    return: AddressDataForFormatting

    整形作業を行う。ここでは、出力形式とは異なり独自の形での分割となっている。
    分割の形は以下の通り

        original,prefecture,city,town,district,invalid,house_number,
        special_characters,building_detail_info,building_info,
        error1,error2,caution

    """

    AddressDataForFormatting = make_DataclassForFormatting()

    # 分割処理を施す前のデータも事前に格納しておく
    AddressDataForFormatting.original = CSV_DATA["address"].to_list()

    non_prefecture_address_data_array: list[str] = pull_out_prefecture_field(
        formatted_address_data_array, AddressDataForFormatting
    )

    non_city_address_data_array: list[str] = pull_out_city_field(
        non_prefecture_address_data_array, AddressDataForFormatting
    )

    non_town_address_data_array: list[str] = pull_out_town_field(
        non_city_address_data_array, AddressDataForFormatting
    )

    others: list[str] = pull_out_district_field(
        non_town_address_data_array, AddressDataForFormatting
    )

    others_tail: list[str] = pull_out_housenumber_invalid_field(
        others, AddressDataForFormatting
    )

    # check 不正なデータが存在しないかどうかを確認
    caution: list = utils.extract.detail.check.check.check(AddressDataForFormatting)

    # データ整形＋分裂してしまったデータを統合整理
    manipulated_others_tail: list = utils.extract.detail.manipulate.manipulate(AddressDataForFormatting, others_tail)

    # ビルや建物情報の詳細を取得
    AddressDataForFormatting.building_detail_info = utils.extract.detail.building_detail.extract_building_detail(AddressDataForFormatting)

    # ビル情報のうちデータ散逸しているものを適切に統合
    utils.extract.detail.shaping_building_info.shaping_and_extracting_building_info(
        AddressDataForFormatting, manipulated_others_tail
    )

    # others_tail内のデータを整形
    utils.extract.detail.shaping.shaping(AddressDataForFormatting)

    # caution
    utils.extract.detail.check.caution.caution(AddressDataForFormatting, manipulated_others_tail, caution)

    return AddressDataForFormatting
