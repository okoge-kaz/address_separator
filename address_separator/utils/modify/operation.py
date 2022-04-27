from utils.modify.handle_miscellaneous_bug import handle_miscellaneous_bugs
from utils.modify.modify_building_data_field_after_split import modify_building_dat_field
from utils.modify.modify_special_place_name_after_split import modify_special_place_name
from utils.modify.resplit_by_every_field_after_split import re_split_by_every_fields


def post_process(splittedAddressDataDictionaries: dict[str, list[str]]):
    """
    args: splittedAddressDataDictionaries (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void
    """
    modify_special_place_name(splittedAddressDataDictionaries)
    modify_building_dat_field(splittedAddressDataDictionaries)
    handle_miscellaneous_bugs(splittedAddressDataDictionaries)
    re_split_by_every_fields(splittedAddressDataDictionaries)
