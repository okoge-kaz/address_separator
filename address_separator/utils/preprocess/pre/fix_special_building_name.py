import re


def escape_special_building_name(address_data: str, special_building_name: str) -> str:
    # 丁目ビル,丁目ビルディング
    if special_building_name + "ビル" in address_data:
        address_data = re.sub(special_building_name + "ビル", "escape_special_building_nameビル", address_data)
    # 丁目センター
    if special_building_name + "センター" in address_data:
        address_data = re.sub(special_building_name + "センター", "escape_special_building_nameセンター", address_data)
    # 丁目ホール
    if special_building_name + "ホール" in address_data:
        address_data = re.sub(special_building_name + "ホール", "escape_special_building_nameホール", address_data)
    # 丁目会館
    if special_building_name + "会館" in address_data:
        address_data = re.sub(special_building_name + "会館", "escape_special_building_name会館", address_data)
    # 丁目劇場
    if special_building_name + "劇場" in address_data:
        address_data = re.sub(special_building_name + "劇場", "escape_special_building_name劇場", address_data)
    return address_data


def rename_special_building_name(address_data: str, special_building_name: str) -> str:
    if "escape_special_building_name" in address_data:
        address_data = re.sub("escape_special_building_name", special_building_name, address_data)

    return address_data
