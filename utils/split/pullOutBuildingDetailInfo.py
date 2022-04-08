import utils.extract.detail.building_detail
import utils.extract.detail.shaping_building_info

def pull_out_buildingdetailinfo(AddressDataForFormatting, manipulated_others_tail):
    AddressDataForFormatting.building_detail_info = utils.extract.detail.building_detail.extract_building_detail(AddressDataForFormatting, manipulated_others_tail)

    # ビル情報のうちデータ散逸しているものを適切に統合
    utils.extract.detail.shaping_building_info.shaping_and_extracting_building_info(
        AddressDataForFormatting, manipulated_others_tail
    )