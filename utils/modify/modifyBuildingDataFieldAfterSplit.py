import re


def modify_building_dat_field(AddressDataForOutput: dict[str, list[str]]) -> None:
    """
    args: splittedAddressAddressDataForOutputDictionaries (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void

    各ケースごとに処理を行う
    """

    DATA_SIZE: int = len(AddressDataForOutput["address4"])

    # マンション名らしくないもの
    for index in range(DATA_SIZE):
        if re.search("^.[0-9]+.$", AddressDataForOutput["address4"][index]):
            AddressDataForOutput["caution"][index] += "CAUTION: address4の値が不適切な可能性があります。  "

    # address4が号のみのとき
    for index in range(DATA_SIZE):
        if AddressDataForOutput["address4"][index] == "号":
            AddressDataForOutput["address4"][index] = ""
            AddressDataForOutput["caution"][index] += "CAUTION: address4の'号'は意味をなさないと判断され、削除されました。  "

    # 番地らしきものがaddress4に紛れ込んでいないかどうか
    for index in range(DATA_SIZE):
        if re.search("[0-9]+ー", AddressDataForOutput["address4"][index]):
            AddressDataForOutput["caution"][index] += "CAUTION: address4に番地の残骸が含まれている場合があります。  "

    # address4に単独で 棟 とあったら
    for index in range(DATA_SIZE):
        if (
            AddressDataForOutput["address3"][index] != ""
            and AddressDataForOutput["address4"][index] == "棟"
        ):
            if re.search("-[0-9]+$", AddressDataForOutput["address3"][index]):
                regular_expression_search_result = re.search(
                    "-[0-9]+$", AddressDataForOutput["address3"][index]
                )

                if regular_expression_search_result is not None:
                    start: int = regular_expression_search_result.start()

                    AddressDataForOutput["address5"][index] = (
                        AddressDataForOutput["address3"][index][start + 1 :]
                        + "棟"
                        + AddressDataForOutput["address5"][index]
                    )
                    AddressDataForOutput["address3"][index] = AddressDataForOutput["address3"][
                        index
                    ][:start]
                    AddressDataForOutput["address4"][index] = ""

    # address4に単独で 号棟 とあったら
    for index in range(DATA_SIZE):
        if (
            AddressDataForOutput["address3"][index] != ""
            and AddressDataForOutput["address4"][index] == "号棟"
        ):
            if re.search("-[0-9]+$", AddressDataForOutput["address3"][index]):
                regular_expression_search_result = re.search(
                    "-[0-9]+$", AddressDataForOutput["address3"][index]
                )

                if regular_expression_search_result is not None:
                    start: int = regular_expression_search_result.start()

                    AddressDataForOutput["address5"][index] = (
                        AddressDataForOutput["address3"][index][start + 1 :]
                        + "号棟"
                        + AddressDataForOutput["address5"][index]
                    )
                    AddressDataForOutput["address3"][index] = AddressDataForOutput["address3"][
                        index
                    ][:start]
                    AddressDataForOutput["address4"][index] = ""

    # address4に単独で 号室 とあったら
    for index in range(DATA_SIZE):
        if (
            AddressDataForOutput["address3"][index] != ""
            and AddressDataForOutput["address4"][index] == "号室"
        ):
            if re.search("-[0-9]+$", AddressDataForOutput["address3"][index]):
                regular_expression_search_result = re.search(
                    "-[0-9]+$", AddressDataForOutput["address3"][index]
                )

                if regular_expression_search_result is not None:
                    start: int = regular_expression_search_result.start()
                    AddressDataForOutput["address5"][index] = (
                        AddressDataForOutput["address3"][index][start + 1 :]
                        + "号室"
                        + AddressDataForOutput["address5"][index]
                    )
                    AddressDataForOutput["address3"][index] = AddressDataForOutput["address3"][
                        index
                    ][:start]
                    AddressDataForOutput["address4"][index] = ""

    # address4に〜号室があるとき
    for index in range(DATA_SIZE):
        # 902号室のようなもの
        if re.search("^[0-9]+号室$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"] != "":
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""
        # c号室のようなもの
        elif re.search("^[a-z]号室$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"] != "":
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""
        # C号室のようなもの
        elif re.search("^[A-Z]号室$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"] != "":
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""

    # address4の先頭のーを除去
    for index in range(DATA_SIZE):
        if AddressDataForOutput["address4"][index] == "ー":
            AddressDataForOutput["address4"][index] = AddressDataForOutput["address4"][index][1:]

    # address4に 号室だけがあるとき
    for index in range(DATA_SIZE):
        if AddressDataForOutput["address4"][index] == "号室":
            if re.search("-[0-9]+", AddressDataForOutput["address3"][index]):
                regular_expression_search_result = re.search(
                    "-[0-9]+", AddressDataForOutput["address3"][index]
                )

                if regular_expression_search_result is not None:
                    start: int = regular_expression_search_result.start()
                    if AddressDataForOutput["address5"] != "":
                        AddressDataForOutput["caution"][
                            index
                        ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                        continue
                    AddressDataForOutput["address5"][index] = (
                        AddressDataForOutput["address3"][index][start + 1 :] + "号室"
                    )
                    AddressDataForOutput["address4"][index] = ""
                    AddressDataForOutput["address3"][index] = AddressDataForOutput["address3"][
                        index
                    ][:start]

    # address4にある()のようなデータのかっこをはずし、適切な位置へ
    for index in range(DATA_SIZE):
        if re.search("^\\(.+\\)$", AddressDataForOutput["address4"][index]):
            AddressDataForOutput["address4"][index] = AddressDataForOutput["address4"][index][1:-1]
        # 3桁以上の数字
        if re.search("^[0-9]{3,}$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"][index] != "":
                # address5が空ではない
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""
        # 3F
        elif re.search("^[0-9]F$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"][index] != "":
                # address5が空ではない
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""
        # 3階
        elif re.search("^[0-9]階$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"][index] != "":
                # address5が空ではない
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""
        # c号室(半角)
        elif re.search("^[a-z]号室$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"][index] != "":
                # address5が空ではない
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""
        # c号室（全角)
        elif re.search("^[a-z]号室$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"][index] != "":
                # address5が空ではない
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""
        # 204号室
        elif re.search("^[0-9]+号室$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"][index] != "":
                # address5が空ではない
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""
        # C号室(半角)
        elif re.search("^[A-Z]号室$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"][index] != "":
                # address5が空ではない
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""
        # C号室(全角)
        elif re.search("^[A-Z]号室$", AddressDataForOutput["address4"][index]):
            if AddressDataForOutput["address5"][index] != "":
                # address5が空ではない
                AddressDataForOutput["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            AddressDataForOutput["address5"][index] = AddressDataForOutput["address4"][index]
            AddressDataForOutput["address4"][index] = ""

    # address4の先頭に の[数字]ー があったとき
    for index in range(DATA_SIZE):
        if re.search("^の[0-9]+ー", AddressDataForOutput["address4"][index]):
            regular_expression_search_result = re.search("^の[0-9]+ー", AddressDataForOutput["address4"][index])

            if regular_expression_search_result is not None:
                end: int = regular_expression_search_result.end()
                AddressDataForOutput["address3"][index] += AddressDataForOutput["address4"][index][
                    1 : end - 1
                ]
                AddressDataForOutput["address4"][index] = AddressDataForOutput["address4"][index][
                    end:
                ]

    # address4に # が単独であったら
    for index in range(DATA_SIZE):
        if AddressDataForOutput["address4"][index] == "#":
            AddressDataForOutput["caution"][index] += "CAUTION: address4の'#'は意味をなさないかもしれません。  "

    # address4の先頭の ー を消去
    for index in range(DATA_SIZE):
        if AddressDataForOutput["address4"][index] == "":
            continue
        if (
            AddressDataForOutput["address4"][index][0] == "ー"
            and len(AddressDataForOutput["address4"][index]) >= 1
        ):
            AddressDataForOutput["address4"][index] = AddressDataForOutput["address4"][index][1:]
