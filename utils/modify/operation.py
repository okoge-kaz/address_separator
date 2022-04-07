from utils.modify.handleMiscellaneousBug import handle_miscellaneous_bugs
from utils.modify.modifyBuildingDataFieldAfterSplit import modify_building_dat_field
from utils.modify.modifySpecialPlaceNameAfterSplit import modify_special_place_name
from utils.modify.reSplitByEveryFieldAfterSplit import re_split_by_every_fields


def post_process(AddressDataForOutput: dict[str, list[str]]) -> None:
    """
    args: AddressDataForOutput (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void
    """
    modify_special_place_name(AddressDataForOutput)
    modify_building_dat_field(AddressDataForOutput)
    handle_miscellaneous_bugs(AddressDataForOutput)
    re_split_by_every_fields(AddressDataForOutput)
