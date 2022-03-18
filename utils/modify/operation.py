from utils.modify.modifyBuildingDataFieldAfterSplit import modify_building_dat_field
from utils.modify.modifySpcialPlaceNameAfterSplit import modify_special_place_name


def post_process(splitedAddressDataDictionarys: dict[str, list[str]]):
    """
    args: splitedAddressDataDictionarys (すでに分割された住所データの辞書型, 出力用には整形していない)
    return: void
    """
    modify_special_place_name(splitedAddressDataDictionarys)
    modify_building_dat_field(splitedAddressDataDictionarys)
