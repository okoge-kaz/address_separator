import re


def shaping_and_extracting_building_info(AddressDataForFormatting, manipulated_others_tail: list) -> None:
    """
    args: (AddressDataForFormatting, manipulated_others_tail: list)
    return: void
    ビル名、建物名など、building_infoに含まれる。または、building_detail_infoに含まれるデータを抽出、整形する
    """

    # '-(([0-9 A-Z])+)号$' のような情報を抽出する

    def extract_building_detail_info_from_others_tail(index: int, string: str):
        if re.search(string, manipulated_others_tail[index]) is not None:
            match = re.search(string, manipulated_others_tail[index])
            assert match is not None
            start: int = match.start()
            end: int = match.end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            AddressDataForFormatting.building_detail_info[index] = (
                building_info + AddressDataForFormatting.building_detail_info[index]
            )
        else:
            pass

    def eliminate_last_hyphen(index: int):
        """最後が-のものを取り除く"""
        if re.search("-$", manipulated_others_tail[index]) is not None:
            match = re.search("-$", manipulated_others_tail[index])
            assert match is not None
            start: int = match.start()
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
        else:
            pass

    for index in range(len(manipulated_others_tail)):
        # 501号のようなかたちを検出しbuilding_detail_infoにデータを付け替える
        extract_building_detail_info_from_others_tail(index, "[0-9]+号$")
        # 401のようなかたちを検出しbuilding_detail_infoにデータを付け替える
        extract_building_detail_info_from_others_tail(index, "(([0-9]+)-)*[0-9]+$")
        # 45号館のようなかたちを検出しbuilding_detail_infoにデータを付け替える
        extract_building_detail_info_from_others_tail(index, "[0-9]+号館$")
        # C号のようなかたちを検出しbuilding_detail_infoにデータを付け替える
        extract_building_detail_info_from_others_tail(index, "-[A-Z]号$")
        # C館のようなかたちを検出しbuilding_detail_infoにデータを付け替える
        extract_building_detail_info_from_others_tail(index, "[A-Z]館$")
        # 45号館のようなかたちを検出しbuilding_detail_infoにデータを付け替える
        extract_building_detail_info_from_others_tail(index, "[0-9]+号室$")
        # 45Fのようなかたちを検出しbuilding_detail_infoにデータを付け替える
        extract_building_detail_info_from_others_tail(index, "[0-9]+F$")
        # 45階のようなかたちを検出しbuilding_detail_infoにデータを付け替える
        extract_building_detail_info_from_others_tail(index, "[0-9]+階$")
        # 最後が-のものを取り除く
        eliminate_last_hyphen(index)
