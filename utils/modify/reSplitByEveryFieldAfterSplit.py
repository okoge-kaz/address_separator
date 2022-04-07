import re

from utils.modify.modifyExceptionAddressExpression import modify_exception_case_address2


def re_split_by_every_fields(AddressDataForOutput: dict[str, list[str]]) -> None:
    """
    args: AddressDataForOutput (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void

    address1またはaddress2 の箇所が、屋一-三八-二二-二0二-エステスクエア町 のようになってしまったものを再整形する。(再分割)

    address2に - が入っているパターン
    具体例: 屋一-三八-二二-二0二-エステスクエア町

    address1に - が入っているパターン

    """

    DATA_SIZE = len(AddressDataForOutput["address2"])

    for index in range(DATA_SIZE):
        if re.search("-", AddressDataForOutput["address2"][index]):

            AddressDataForOutput["caution"][
                index
            ] += "CAUTION: 自動整形システムが推測によって分割している箇所があります。この行の分割が正しいか確認することを強く推奨します。 "
            # 西一-一八-一六-カモミ-ル西町 のようになっているはず

            MAPPING_JAPANESE_STYLE_NUMBER_TO_ALABIC_NUMBER: dict = {
                "一": "1",
                "二": "2",
                "三": "3",
                "四": "4",
                "五": "5",
                "六": "6",
                "七": "7",
                "八": "8",
                "九": "9",
                "十": "10",
                "〇": "0",
            }

            JAPANESE_STYLE_NUMBERS: list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "〇"]

            re_formated_address2_data_field: str = ""
            for address2_data_field_character in AddressDataForOutput["address2"][index]:
                """
                address2 の fieldに入っている文字列を char ごとに走査して、漢数字を算用数字に変換する
                """
                if address2_data_field_character in JAPANESE_STYLE_NUMBERS:
                    re_formated_address2_data_field += MAPPING_JAPANESE_STYLE_NUMBER_TO_ALABIC_NUMBER[
                        address2_data_field_character
                    ]
                else:
                    re_formated_address2_data_field += address2_data_field_character

            # 再分割作業

            if re.search("[0-9]+", re_formated_address2_data_field):
                # 数字がある
                address3_start: int = re.search("[0-9]+", re_formated_address2_data_field).start()
                address3_end: int = re.search("[0-9]+(-[0-9]+)*", re_formated_address2_data_field).end()
                # 数字で終わる
                if (
                    len(re_formated_address2_data_field)
                    == re.search("[0-9]+(-[0-9]+)*", re_formated_address2_data_field).end()
                ):
                    if AddressDataForOutput["address3"][index] == "":
                        AddressDataForOutput["address2"][index] = re_formated_address2_data_field[
                            :address3_start
                        ]
                        AddressDataForOutput["address3"][index] = re_formated_address2_data_field[
                            address3_start:address3_end
                        ]
                    else:
                        AddressDataForOutput["address2"][index] = re_formated_address2_data_field[
                            :address3_start
                        ]
                        AddressDataForOutput["address3"][index] = (
                            re_formated_address2_data_field[address3_start:address3_end]
                            + AddressDataForOutput["address3"][index]
                        )
                else:
                    # 建物名らしきものが存在する
                    if AddressDataForOutput["address3"][index] == "":
                        # 番地情報が空
                        AddressDataForOutput["address2"][index] = re_formated_address2_data_field[
                            :address3_start
                        ]
                        AddressDataForOutput["address3"][index] = re_formated_address2_data_field[
                            address3_start:address3_end
                        ]
                        building_information_AddressDataForOutput: str = re_formated_address2_data_field[
                            address3_end:
                        ]
                        if re.search("[0-9]", building_information_AddressDataForOutput):
                            # 建物名の情報に部屋番号が紛れ込んでいる
                            start_index: int = re.search(
                                "[0-9]", building_information_AddressDataForOutput
                            ).start()
                            AddressDataForOutput["address4"][
                                index
                            ] = building_information_AddressDataForOutput[:start_index]
                            # 先頭の-を削除
                            if (
                                AddressDataForOutput["address4"][index] != ""
                                and AddressDataForOutput["address4"][index][0] == "-"
                            ):
                                if len(AddressDataForOutput["address4"][index]) >= 2:
                                    AddressDataForOutput["address4"][index] = AddressDataForOutput[
                                        "address4"
                                    ][index][1:]
                            # address4の-をーに変更
                            AddressDataForOutput["address4"][index] = re.sub(
                                "-", "ー", AddressDataForOutput["address4"][index]
                            )
                            # address5
                            AddressDataForOutput["address5"][
                                index
                            ] = building_information_AddressDataForOutput[start_index:]
                        else:
                            # 建物情報のみ
                            AddressDataForOutput["address4"][
                                index
                            ] = building_information_AddressDataForOutput
                            # 先頭の-を削除
                            if (
                                AddressDataForOutput["address4"][index] != ""
                                and AddressDataForOutput["address4"][index][0] == "-"
                            ):
                                if len(AddressDataForOutput["address4"][index]) >= 2:
                                    AddressDataForOutput["address4"][index] = AddressDataForOutput[
                                        "address4"
                                    ][index][1:]
                            # address4の-をーに変更
                            AddressDataForOutput["address4"][index] = re.sub(
                                "-", "ー", AddressDataForOutput["address4"][index]
                            )
                    else:
                        # 番地情報に数字がある
                        # 建物情報の可能性が高いのでaddress5に移す
                        AddressDataForOutput["address5"][index] = AddressDataForOutput["address3"][
                            index
                        ]
                        AddressDataForOutput["address2"][index] = re_formated_address2_data_field[
                            :address3_start
                        ]
                        AddressDataForOutput["address3"][index] = re_formated_address2_data_field[
                            address3_start:address3_end
                        ]
                        AddressDataForOutput["address4"][index] = re_formated_address2_data_field[
                            address3_end:
                        ]
                        # 先頭の-を削除
                        if (
                            AddressDataForOutput["address4"][index] != ""
                            and AddressDataForOutput["address4"][index][0] == "-"
                        ):
                            if len(AddressDataForOutput["address4"][index]) >= 2:
                                AddressDataForOutput["address4"][index] = AddressDataForOutput[
                                    "address4"
                                ][index][1:]
                        # address4の-をーに変更
                        AddressDataForOutput["address4"][index] = re.sub(
                            "-", "ー", AddressDataForOutput["address4"][index]
                        )

            # 例外ケース処理
            modify_exception_case_address2(AddressDataForOutput, index)

    # address1に - が入っているパターン
    for index in range(DATA_SIZE):
        if re.search("-", AddressDataForOutput["address1"][index]):

            AddressDataForOutput["caution"][
                index
            ] += "CAUTION: 自動整形システムが推測によって分割している箇所があります。この行の分割が正しいか確認することを強く推奨します。 "

            # 羽若町四九三-一-市 のようになっているはず
            MAPPING_JAPANESE_STYLE_NUMBER_TO_ALABIC_NUMBER: dict = {
                "一": "1",
                "二": "2",
                "三": "3",
                "四": "4",
                "五": "5",
                "六": "6",
                "七": "7",
                "八": "8",
                "九": "9",
                "十": "10",
                "〇": "0",
            }

            JAPANESE_STYLE_NUMBERS: list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "〇"]

            re_formated_address1_data_field: str = ""

            AddressDataForOutput["address1"][index] += AddressDataForOutput["address2"][index]
            AddressDataForOutput["address2"][index] = ""

            for id in range(len(AddressDataForOutput["address1"][index])):
                if AddressDataForOutput["address1"][index][id] in JAPANESE_STYLE_NUMBERS:
                    re_formated_address1_data_field += MAPPING_JAPANESE_STYLE_NUMBER_TO_ALABIC_NUMBER[
                        AddressDataForOutput["address1"][index][id]
                    ]
                else:
                    re_formated_address1_data_field += AddressDataForOutput["address1"][index][id]

            # 分割作業
            if re.search("[0-9]+", re_formated_address1_data_field):
                # 数字がある
                regular_expression_search_result = re.search("[0-9]+", re_formated_address1_data_field)
                address3_start: int = re.search("[0-9]+", re_formated_address1_data_field).start()
                address3_end: int = re.search("[0-9]+(-[0-9]+)*", re_formated_address1_data_field).end()
                # 数字で終わる
                if (
                    len(re_formated_address1_data_field)
                    == re.search("[0-9]+(-[0-9]+)*", re_formated_address1_data_field).end()
                ):
                    if AddressDataForOutput["address3"][index] == "":
                        AddressDataForOutput["address1"][index] = re_formated_address1_data_field[
                            :address3_start
                        ]
                        AddressDataForOutput["address3"][index] = re_formated_address1_data_field[
                            address3_start:address3_end
                        ]
                    else:
                        AddressDataForOutput["address1"][index] = re_formated_address1_data_field[
                            :address3_start
                        ]
                        AddressDataForOutput["address3"][index] = (
                            re_formated_address1_data_field[address3_start:address3_end]
                            + AddressDataForOutput["address3"][index]
                        )
                else:
                    # 建物名らしきものが存在する
                    if AddressDataForOutput["address3"][index] == "":
                        # 番地情報が空
                        AddressDataForOutput["address1"][index] = re_formated_address1_data_field[
                            :address3_start
                        ]
                        AddressDataForOutput["address3"][index] = re_formated_address1_data_field[
                            address3_start:address3_end
                        ]
                        building_information_AddressDataForOutput: str = re_formated_address1_data_field[
                            address3_end:
                        ]
                        if re.search("[0-9]", building_information_AddressDataForOutput):
                            # 建物名の情報に部屋番号が紛れ込んでいる
                            start_index: int = re.search(
                                "[0-9]", building_information_AddressDataForOutput
                            ).start()
                            AddressDataForOutput["address4"][
                                index
                            ] = building_information_AddressDataForOutput[:start_index]
                            # 先頭の-を削除
                            if (
                                AddressDataForOutput["address4"][index] != ""
                                and AddressDataForOutput["address4"][index][0] == "-"
                            ):
                                if len(AddressDataForOutput["address4"][index]) >= 2:
                                    AddressDataForOutput["address4"][index] = AddressDataForOutput[
                                        "address4"
                                    ][index][1:]
                            # address4の-をーに変更
                            AddressDataForOutput["address4"][index] = re.sub(
                                "-", "ー", AddressDataForOutput["address4"][index]
                            )
                            # address5
                            AddressDataForOutput["address5"][
                                index
                            ] = building_information_AddressDataForOutput[start_index:]
                        else:
                            # 建物情報のみ
                            AddressDataForOutput["address4"][
                                index
                            ] = building_information_AddressDataForOutput
                            # 先頭の-を削除
                            if (
                                AddressDataForOutput["address4"][index] != ""
                                and AddressDataForOutput["address4"][index][0] == "-"
                            ):
                                if len(AddressDataForOutput["address4"][index]) >= 2:
                                    AddressDataForOutput["address4"][index] = AddressDataForOutput[
                                        "address4"
                                    ][index][1:]
                            # address4の-をーに変更
                            AddressDataForOutput["address4"][index] = re.sub(
                                "-", "ー", AddressDataForOutput["address4"][index]
                            )
                    else:
                        # 番地情報に数字がある
                        # 建物情報の可能性が高いのでaddress5に移す
                        AddressDataForOutput["address5"][index] = AddressDataForOutput["address3"][
                            index
                        ]
                        AddressDataForOutput["address1"][index] = re_formated_address1_data_field[
                            :address3_start
                        ]
                        AddressDataForOutput["address3"][index] = re_formated_address1_data_field[
                            address3_start:address3_end
                        ]
                        AddressDataForOutput["address4"][index] = re_formated_address1_data_field[
                            address3_end:
                        ]
                        # 先頭の-を削除
                        if (
                            AddressDataForOutput["address4"][index] != ""
                            and AddressDataForOutput["address4"][index][0] == "-"
                        ):
                            if len(AddressDataForOutput["address4"][index]) >= 2:
                                AddressDataForOutput["address4"][index] = AddressDataForOutput[
                                    "address4"
                                ][index][1:]
                        # address4の-をーに変更
                        AddressDataForOutput["address4"][index] = re.sub(
                            "-", "ー", AddressDataForOutput["address4"][index]
                        )

                # 移動処理
                AddressDataForOutput["address2"][index] = AddressDataForOutput["address1"][index]
                AddressDataForOutput["address1"][index] = ""
            else:
                continue
