import re


def shaping_and_extracting_building_info(AddressDataForFormatting, manipulated_others_tail: list) -> None:
    """
    args: (AddressDataForFormatting, manipulated_others_tail: list)
    return: void
    ビル名、建物名など、building_infoに含まれる。または、building_detail_infoに含まれるデータを抽出、整形する
    """

    # '-(([0-9 A-Z])+)号$' のような情報を抽出する

    def extract_building_detail_info_from_others_tail_1(index: int):
        """501号のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[0-9]+号$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[0-9]+号$", manipulated_others_tail[index]).start()
            end: int = re.search("[0-9]+号$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            AddressDataForFormatting.building_detail_info[index] = building_info + AddressDataForFormatting.building_detail_info[index]
        else:
            pass

    def extract_building_detail_info_from_others_tail_2(index: int):
        """401のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("(([0-9]+)-)*[0-9]+$", manipulated_others_tail[index]) is not None:
            start: int = re.search("(([0-9]+)-)*[0-9]+$", manipulated_others_tail[index]).start()
            end: int = re.search("(([0-9]+)-)*[0-9]+$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            AddressDataForFormatting.building_detail_info[index] = building_info + AddressDataForFormatting.building_detail_info[index]
        else:
            pass

    def extract_building_detail_info_from_others_tail_3(index: int):
        """45号館のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[0-9]+号館$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[0-9]+号館$", manipulated_others_tail[index]).start()
            end: int = re.search("[0-9]+号館$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            AddressDataForFormatting.building_detail_info[index] = building_info + AddressDataForFormatting.building_detail_info[index]
        else:
            pass

    def extract_building_detail_info_from_others_tail_4(index: int):
        """C号のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("-[A-Z]号$", manipulated_others_tail[index]) is not None:
            start: int = re.search("-[A-Z]号$", manipulated_others_tail[index]).start()
            end: int = re.search("-[A-Z]号$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            AddressDataForFormatting.building_detail_info[index] = building_info + AddressDataForFormatting.building_detail_info[index]
        else:
            pass

    def extract_building_detail_info_from_others_tail_5(index: int):
        """C館のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[A-Z]館$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[A-Z]館$", manipulated_others_tail[index]).start()
            end: int = re.search("[A-Z]館$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            AddressDataForFormatting.building_detail_info[index] = building_info + AddressDataForFormatting.building_detail_info[index]
        else:
            pass

    def extract_building_detail_info_from_others_tail_6(index: int):
        """45号館のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[0-9]+号室$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[0-9]+号室$", manipulated_others_tail[index]).start()
            end: int = re.search("[0-9]+号室$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            AddressDataForFormatting.building_detail_info[index] = building_info + AddressDataForFormatting.building_detail_info[index]
        else:
            pass

    def extract_building_detail_info_from_others_tail_7(index: int):
        """45Fのようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[0-9]+F$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[0-9]+F$", manipulated_others_tail[index]).start()
            end: int = re.search("[0-9]+F$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            AddressDataForFormatting.building_detail_info[index] = building_info + AddressDataForFormatting.building_detail_info[index]
        else:
            pass

    def extract_building_detail_info_from_others_tail_8(index: int):
        """45階のようなかたちを検出しbuilding_detail_infoにデータを付け替える"""
        if re.search("[0-9]+階$", manipulated_others_tail[index]) is not None:
            start: int = re.search("[0-9]+階$", manipulated_others_tail[index]).start()
            end: int = re.search("[0-9]+階$", manipulated_others_tail[index]).end()
            # ここ順番注意
            building_info = manipulated_others_tail[index][start:end]
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
            # 順番に注意
            AddressDataForFormatting.building_detail_info[index] = building_info + AddressDataForFormatting.building_detail_info[index]
        else:
            pass

    def extract_building_detail_info_from_others_tail_9(index: int):
        """最後が-のものを取り除く"""
        if re.search("-$", manipulated_others_tail[index]) is not None:
            start: int = re.search("-$", manipulated_others_tail[index]).start()
            manipulated_others_tail[index] = manipulated_others_tail[index][:start]
        else:
            pass

    for index in range(len(manipulated_others_tail)):
        extract_building_detail_info_from_others_tail_1(index)
        extract_building_detail_info_from_others_tail_2(index)
        extract_building_detail_info_from_others_tail_3(index)
        extract_building_detail_info_from_others_tail_4(index)
        extract_building_detail_info_from_others_tail_5(index)
        extract_building_detail_info_from_others_tail_6(index)
        extract_building_detail_info_from_others_tail_7(index)
        extract_building_detail_info_from_others_tail_8(index)
        extract_building_detail_info_from_others_tail_9(index)
