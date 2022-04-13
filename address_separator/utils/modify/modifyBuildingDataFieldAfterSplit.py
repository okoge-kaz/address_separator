import re


def modify_building_dat_field(splitted_address_data_dictionaries: dict[str, list[str]]) -> None:
    """
    args: splittedAddresssplitted_address_data_dictionariesDictionaries (すでに分割された住所データの辞書型, 出力用には整形済み)
    return: void

    各ケースごとに処理を行う
    """

    DATA_SIZE: int = len(splitted_address_data_dictionaries["address4"])

    # マンション名らしくないもの
    for index in range(DATA_SIZE):
        if re.search("^.[0-9]+.$", splitted_address_data_dictionaries["address4"][index]):
            splitted_address_data_dictionaries["caution"][index] += "CAUTION: address4の値が不適切な可能性があります。  "

    # address4が号のみのとき
    for index in range(DATA_SIZE):
        if splitted_address_data_dictionaries["address4"][index] == "号":
            splitted_address_data_dictionaries["address4"][index] = ""
            splitted_address_data_dictionaries["caution"][index] += "CAUTION: address4の'号'は意味をなさないと判断され、削除されました。  "

    # 番地らしきものがaddress4に紛れ込んでいないかどうか
    for index in range(DATA_SIZE):
        if re.search("[0-9]+ー", splitted_address_data_dictionaries["address4"][index]):
            splitted_address_data_dictionaries["caution"][index] += "CAUTION: address4に番地の残骸が含まれている場合があります。  "

    # address4に単独で 棟 とあったら
    for index in range(DATA_SIZE):
        if (
            splitted_address_data_dictionaries["address3"][index] != ""
            and splitted_address_data_dictionaries["address4"][index] == "棟"
        ):
            if re.search("-[0-9]+$", splitted_address_data_dictionaries["address3"][index]):
                regular_expression_search_result = re.search(
                    "-[0-9]+$", splitted_address_data_dictionaries["address3"][index]
                )

                if regular_expression_search_result is not None:
                    start: int = regular_expression_search_result.start()

                    splitted_address_data_dictionaries["address5"][index] = (
                        splitted_address_data_dictionaries["address3"][index][start + 1 :]
                        + "棟"
                        + splitted_address_data_dictionaries["address5"][index]
                    )
                    splitted_address_data_dictionaries["address3"][index] = splitted_address_data_dictionaries["address3"][
                        index
                    ][:start]
                    splitted_address_data_dictionaries["address4"][index] = ""

    # address4に単独で 号棟 とあったら
    for index in range(DATA_SIZE):
        if (
            splitted_address_data_dictionaries["address3"][index] != ""
            and splitted_address_data_dictionaries["address4"][index] == "号棟"
        ):
            if re.search("-[0-9]+$", splitted_address_data_dictionaries["address3"][index]):
                regular_expression_search_result = re.search(
                    "-[0-9]+$", splitted_address_data_dictionaries["address3"][index]
                )

                if regular_expression_search_result is not None:
                    start: int = regular_expression_search_result.start()

                    splitted_address_data_dictionaries["address5"][index] = (
                        splitted_address_data_dictionaries["address3"][index][start + 1 :]
                        + "号棟"
                        + splitted_address_data_dictionaries["address5"][index]
                    )
                    splitted_address_data_dictionaries["address3"][index] = splitted_address_data_dictionaries["address3"][
                        index
                    ][:start]
                    splitted_address_data_dictionaries["address4"][index] = ""

    # address4に単独で 号室 とあったら
    for index in range(DATA_SIZE):
        if (
            splitted_address_data_dictionaries["address3"][index] != ""
            and splitted_address_data_dictionaries["address4"][index] == "号室"
        ):
            if re.search("-[0-9]+$", splitted_address_data_dictionaries["address3"][index]):
                regular_expression_search_result = re.search(
                    "-[0-9]+$", splitted_address_data_dictionaries["address3"][index]
                )

                if regular_expression_search_result is not None:
                    start: int = regular_expression_search_result.start()
                    splitted_address_data_dictionaries["address5"][index] = (
                        splitted_address_data_dictionaries["address3"][index][start + 1 :]
                        + "号室"
                        + splitted_address_data_dictionaries["address5"][index]
                    )
                    splitted_address_data_dictionaries["address3"][index] = splitted_address_data_dictionaries["address3"][
                        index
                    ][:start]
                    splitted_address_data_dictionaries["address4"][index] = ""

    # address4に〜号室があるとき
    for index in range(DATA_SIZE):
        # 902号室のようなもの
        if re.search("^[0-9]+号室$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"] != "":
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""
        # c号室のようなもの
        elif re.search("^[a-z]号室$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"] != "":
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""
        # C号室のようなもの
        elif re.search("^[A-Z]号室$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"] != "":
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""

    # address4の先頭のーを除去
    for index in range(DATA_SIZE):
        if splitted_address_data_dictionaries["address4"][index] == "ー":
            splitted_address_data_dictionaries["address4"][index] = splitted_address_data_dictionaries["address4"][index][1:]

    # address4に 号室だけがあるとき
    for index in range(DATA_SIZE):
        if splitted_address_data_dictionaries["address4"][index] == "号室":
            if re.search("-[0-9]+", splitted_address_data_dictionaries["address3"][index]):
                regular_expression_search_result = re.search(
                    "-[0-9]+", splitted_address_data_dictionaries["address3"][index]
                )

                if regular_expression_search_result is not None:
                    start: int = regular_expression_search_result.start()
                    if splitted_address_data_dictionaries["address5"] != "":
                        splitted_address_data_dictionaries["caution"][
                            index
                        ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                        continue
                    splitted_address_data_dictionaries["address5"][index] = (
                        splitted_address_data_dictionaries["address3"][index][start + 1 :] + "号室"
                    )
                    splitted_address_data_dictionaries["address4"][index] = ""
                    splitted_address_data_dictionaries["address3"][index] = splitted_address_data_dictionaries["address3"][
                        index
                    ][:start]

    # address4にある()のようなデータのかっこをはずし、適切な位置へ
    for index in range(DATA_SIZE):
        if re.search("^\\(.+\\)$", splitted_address_data_dictionaries["address4"][index]):
            splitted_address_data_dictionaries["address4"][index] = splitted_address_data_dictionaries["address4"][index][1:-1]
        # 3桁以上の数字
        if re.search("^[0-9]{3,}$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"][index] != "":
                # address5が空ではない
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""
        # 3F
        elif re.search("^[0-9]F$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"][index] != "":
                # address5が空ではない
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""
        # 3階
        elif re.search("^[0-9]階$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"][index] != "":
                # address5が空ではない
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""
        # c号室(半角)
        elif re.search("^[a-z]号室$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"][index] != "":
                # address5が空ではない
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""
        # c号室（全角)
        elif re.search("^[a-z]号室$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"][index] != "":
                # address5が空ではない
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""
        # 204号室
        elif re.search("^[0-9]+号室$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"][index] != "":
                # address5が空ではない
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""
        # C号室(半角)
        elif re.search("^[A-Z]号室$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"][index] != "":
                # address5が空ではない
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""
        # C号室(全角)
        elif re.search("^[A-Z]号室$", splitted_address_data_dictionaries["address4"][index]):
            if splitted_address_data_dictionaries["address5"][index] != "":
                # address5が空ではない
                splitted_address_data_dictionaries["caution"][
                    index
                ] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            splitted_address_data_dictionaries["address5"][index] = splitted_address_data_dictionaries["address4"][index]
            splitted_address_data_dictionaries["address4"][index] = ""

    # address4の先頭に の[数字]ー があったとき
    for index in range(DATA_SIZE):
        if re.search("^の[0-9]+ー", splitted_address_data_dictionaries["address4"][index]):
            regular_expression_search_result = re.search("^の[0-9]+ー", splitted_address_data_dictionaries["address4"][index])

            if regular_expression_search_result is not None:
                end: int = regular_expression_search_result.end()
                splitted_address_data_dictionaries["address3"][index] += splitted_address_data_dictionaries["address4"][index][
                    1 : end - 1
                ]
                splitted_address_data_dictionaries["address4"][index] = splitted_address_data_dictionaries["address4"][index][
                    end:
                ]

    # address4に # が単独であったら
    for index in range(DATA_SIZE):
        if splitted_address_data_dictionaries["address4"][index] == "#":
            splitted_address_data_dictionaries["caution"][index] += "CAUTION: address4の'#'は意味をなさないかもしれません。  "

    # address4の先頭の ー を消去
    for index in range(DATA_SIZE):
        if splitted_address_data_dictionaries["address4"][index] == "":
            continue
        if (
            splitted_address_data_dictionaries["address4"][index][0] == "ー"
            and len(splitted_address_data_dictionaries["address4"][index]) >= 1
        ):
            splitted_address_data_dictionaries["address4"][index] = splitted_address_data_dictionaries["address4"][index][1:]
