from __future__ import annotations

import re


def shaping(splitted_address_data_dictionaries: dict[str, list[str]]):
    """分割等が終了したデータに対して、これらを出力用に整形する。
    特殊な名前の市町村等のデータについても、ここで整形作業を行う.
    """
    # データの最終整形 都市名のうち半角数字のものは漢字に直す
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] == "":
            continue
        if re.search("[1-9]", splitted_address_data_dictionaries["city"][index]) is not None:
            shaped: str = ""
            mapping_dictionary: dict = {
                "1": "一",
                "2": "二",
                "3": "三",
                "4": "四",
                "5": "五",
                "6": "六",
                "7": "七",
                "8": "八",
                "9": "九",
            }
            numbers: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for char in splitted_address_data_dictionaries["city"][index]:
                if char in numbers:
                    shaped += mapping_dictionary[char]
                else:
                    shaped += char
            splitted_address_data_dictionaries["city"][index] = shaped
        else:
            pass
    # 上記と同様のことをtownでもやる。ただし漢字+ひらがな+算用数字のときのみ
    for index in range(len(splitted_address_data_dictionaries["town"])):
        if splitted_address_data_dictionaries["town"][index] == "":
            continue
        if re.search("[1-9]", splitted_address_data_dictionaries["town"][index]) is not None:
            shaped: str = ""
            mapping_dictionary: dict = {
                "1": "一",
                "2": "二",
                "3": "三",
                "4": "四",
                "5": "五",
                "6": "六",
                "7": "七",
                "8": "八",
                "9": "九",
            }
            numbers: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for char in splitted_address_data_dictionaries["town"][index]:
                if char in numbers:
                    shaped += mapping_dictionary[char]
                else:
                    shaped += char
            # 一-町 -> 一番町に変える
            if re.search("[一-九]-町", shaped):
                start: int = re.search("[一-九]-町", shaped).start()
                shaped = shaped[: start + 1] + "番" + shaped[start + 2 :]

            splitted_address_data_dictionaries["town"][index] = shaped
        else:
            pass
    # city の先頭または末尾に-があったら除去
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] == "":
            continue
        if splitted_address_data_dictionaries["city"][index][0] == "-":
            splitted_address_data_dictionaries["city"][index] = splitted_address_data_dictionaries["city"][index][1:]
        if len(splitted_address_data_dictionaries["city"][index]) < 1:
            continue
        if splitted_address_data_dictionaries["city"][index][-1] == "-":
            splitted_address_data_dictionaries["city"][index] = splitted_address_data_dictionaries["city"][index][:-1]
    # town の先頭または末尾に-があったら除去
    for index in range(len(splitted_address_data_dictionaries["town"])):
        if splitted_address_data_dictionaries["town"][index] == "":
            continue
        if splitted_address_data_dictionaries["town"][index][0] == "-":
            splitted_address_data_dictionaries["town"][index] = splitted_address_data_dictionaries["town"][index][1:]
        if len(splitted_address_data_dictionaries["town"][index]) < 1:
            continue
        if splitted_address_data_dictionaries["town"][index][-1] == "-":
            splitted_address_data_dictionaries["town"][index] = splitted_address_data_dictionaries["town"][index][:-1]
    # district の先頭または末尾に-があったら除去
    for index in range(len(splitted_address_data_dictionaries["district"])):
        if splitted_address_data_dictionaries["district"][index] == "":
            continue
        if splitted_address_data_dictionaries["district"][index][0] == "-":
            splitted_address_data_dictionaries["district"][index] = splitted_address_data_dictionaries["district"][
                index
            ][1:]
        if len(splitted_address_data_dictionaries["district"][index]) < 1:
            continue
        if splitted_address_data_dictionaries["district"][index][-1] == "-":
            splitted_address_data_dictionaries["district"][index] = splitted_address_data_dictionaries["district"][
                index
            ][:-1]
    # 東京都 町田など、固有名詞に 市、町、区、町、村があるもの
    # 町田市
    for index in range(len(splitted_address_data_dictionaries["district"])):
        if splitted_address_data_dictionaries["district"][index] == "":
            continue
        if splitted_address_data_dictionaries["district"][index] == "田":
            if splitted_address_data_dictionaries["town"][index] == "":
                continue
            if splitted_address_data_dictionaries["town"][index][-1] == "町":
                splitted_address_data_dictionaries["town"][index] += "田"
                splitted_address_data_dictionaries["district"][index] = ""
            else:
                pass
        else:
            pass
    # 市川市
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] == "市" and re.search(
            "^川市", splitted_address_data_dictionaries["district"][index]
        ):
            start: int = re.search("^川市", splitted_address_data_dictionaries["district"][index]).start()
            end: int = re.search("^川市", splitted_address_data_dictionaries["district"][index]).end()
            if start != 0:
                print("something wrong")  # for debug
            splitted_address_data_dictionaries["city"][index] = "市川市"
            splitted_address_data_dictionaries["district"][index] = splitted_address_data_dictionaries["district"][
                index
            ][end:]

        elif splitted_address_data_dictionaries["district"][index] == "":
            # どこに残骸があるか不明なので
            if splitted_address_data_dictionaries["city"][index] == "市" and re.search(
                "^川市", splitted_address_data_dictionaries["town"][index]
            ):
                start: int = re.search("^川市", splitted_address_data_dictionaries["town"][index]).start()
                end: int = re.search("^川市", splitted_address_data_dictionaries["town"][index]).end()
                if start != 0:
                    print("something wrong")  # for debug
                splitted_address_data_dictionaries["city"][index] = "市川市"
                splitted_address_data_dictionaries["town"][index] = splitted_address_data_dictionaries["town"][index][
                    end:
                ]
    # 市原市
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] == "市" and re.search(
            "^原市", splitted_address_data_dictionaries["district"][index]
        ):
            start: int = re.search("^原市", splitted_address_data_dictionaries["district"][index]).start()
            end: int = re.search("^原市", splitted_address_data_dictionaries["district"][index]).end()
            if start != 0:
                print("something wrong")  # for debug
            splitted_address_data_dictionaries["city"][index] = "市原市"
            splitted_address_data_dictionaries["district"][index] = splitted_address_data_dictionaries["district"][
                index
            ][end:]

        elif splitted_address_data_dictionaries["district"][index] == "":
            # どこに残骸があるか不明なので
            if splitted_address_data_dictionaries["city"][index] == "市" and re.search(
                "^原市", splitted_address_data_dictionaries["town"][index]
            ):
                start: int = re.search("^原市", splitted_address_data_dictionaries["town"][index]).start()
                end: int = re.search("^原市", splitted_address_data_dictionaries["town"][index]).end()
                if start != 0:
                    print("something wrong")  # for debug
                splitted_address_data_dictionaries["city"][index] = "市原市"
                splitted_address_data_dictionaries["town"][index] = splitted_address_data_dictionaries["town"][index][
                    end:
                ]
    # 野々市市
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] == "野々市" and re.search(
            "^市", splitted_address_data_dictionaries["district"][index]
        ):
            start: int = re.search("^市", splitted_address_data_dictionaries["district"][index]).start()
            end: int = re.search("^市", splitted_address_data_dictionaries["district"][index]).end()
            if start != 0:
                print("something wrong")  # for debug
            splitted_address_data_dictionaries["city"][index] = "野々市市"
            splitted_address_data_dictionaries["district"][index] = splitted_address_data_dictionaries["district"][
                index
            ][end:]

        elif splitted_address_data_dictionaries["district"][index] == "":
            # どこに残骸があるか不明なので
            if splitted_address_data_dictionaries["city"][index] == "野々市" and re.search(
                "^市", splitted_address_data_dictionaries["town"][index]
            ):
                start: int = re.search("^市", splitted_address_data_dictionaries["town"][index]).start()
                end: int = re.search("^市", splitted_address_data_dictionaries["town"][index]).end()
                if start != 0:
                    print("something wrong")  # for debug
                splitted_address_data_dictionaries["city"][index] = "野々市市"
                splitted_address_data_dictionaries["town"][index] = splitted_address_data_dictionaries["town"][index][
                    end:
                ]
    # 四日市市
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] == "四日市" and re.search(
            "^市", splitted_address_data_dictionaries["district"][index]
        ):
            start: int = re.search("^市", splitted_address_data_dictionaries["district"][index]).start()
            end: int = re.search("^市", splitted_address_data_dictionaries["district"][index]).end()
            if start != 0:
                print("something wrong")  # for debug
            splitted_address_data_dictionaries["city"][index] = "四日市市"
            splitted_address_data_dictionaries["district"][index] = splitted_address_data_dictionaries["district"][
                index
            ][end:]

        elif splitted_address_data_dictionaries["district"][index] == "":
            # どこに残骸があるか不明なので
            if splitted_address_data_dictionaries["city"][index] == "四日市" and re.search(
                "^市", splitted_address_data_dictionaries["town"][index]
            ):
                start: int = re.search("^市", splitted_address_data_dictionaries["town"][index]).start()
                end: int = re.search("^市", splitted_address_data_dictionaries["town"][index]).end()
                if start != 0:
                    print("something wrong")  # for debug
                splitted_address_data_dictionaries["city"][index] = "四日市市"
                splitted_address_data_dictionaries["town"][index] = splitted_address_data_dictionaries["town"][index][
                    end:
                ]
    # 廿日市市
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] == "廿日市" and re.search(
            "^市", splitted_address_data_dictionaries["district"][index]
        ):
            start: int = re.search("^市", splitted_address_data_dictionaries["district"][index]).start()
            end: int = re.search("^市", splitted_address_data_dictionaries["district"][index]).end()
            if start != 0:
                print("something wrong")  # for debug
            splitted_address_data_dictionaries["city"][index] = "廿日市市"
            splitted_address_data_dictionaries["district"][index] = splitted_address_data_dictionaries["district"][
                index
            ][end:]

        elif splitted_address_data_dictionaries["district"][index] == "":
            # どこに残骸があるか不明なので
            if splitted_address_data_dictionaries["city"][index] == "廿日市" and re.search(
                "^市", splitted_address_data_dictionaries["town"][index]
            ):
                start: int = re.search("^市", splitted_address_data_dictionaries["town"][index]).start()
                end: int = re.search("^市", splitted_address_data_dictionaries["town"][index]).end()
                if start != 0:
                    print("something wrong")  # for debug
                splitted_address_data_dictionaries["city"][index] = "廿日市市"
                splitted_address_data_dictionaries["town"][index] = splitted_address_data_dictionaries["town"][index][
                    end:
                ]
    # 余市軍
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if splitted_address_data_dictionaries["city"][index] == "余市" and re.search(
            "^郡", splitted_address_data_dictionaries["district"][index]
        ):
            start: int = re.search("^郡", splitted_address_data_dictionaries["district"][index]).start()
            end: int = re.search("^郡", splitted_address_data_dictionaries["district"][index]).end()
            if start != 0:
                print("something wrong")  # for debug
            splitted_address_data_dictionaries["city"][index] = "余市郡"
            splitted_address_data_dictionaries["district"][index] = splitted_address_data_dictionaries["district"][
                index
            ][end:]

        elif splitted_address_data_dictionaries["district"][index] == "":
            # どこに残骸があるか不明なので
            if splitted_address_data_dictionaries["city"][index] == "余市" and re.search(
                "^郡", splitted_address_data_dictionaries["town"][index]
            ):
                start: int = re.search("^郡", splitted_address_data_dictionaries["town"][index]).start()
                end: int = re.search("^郡", splitted_address_data_dictionaries["town"][index]).end()
                if start != 0:
                    print("something wrong")  # for debug
                splitted_address_data_dictionaries["city"][index] = "余市郡"
                splitted_address_data_dictionaries["town"][index] = splitted_address_data_dictionaries["town"][index][
                    end:
                ]
        elif re.search("^[- 0-9 町 市]", splitted_address_data_dictionaries["district"][index]) is None:
            # どこに残骸があるか不明なので
            if splitted_address_data_dictionaries["city"][index] == "余市" and re.search(
                "^郡", splitted_address_data_dictionaries["town"][index]
            ):
                start: int = re.search("^郡", splitted_address_data_dictionaries["town"][index]).start()
                end: int = re.search("^郡", splitted_address_data_dictionaries["town"][index]).end()
                if start != 0:
                    print("something wrong")  # for debug
                splitted_address_data_dictionaries["city"][index] = "余市郡"
                splitted_address_data_dictionaries["town"][index] = splitted_address_data_dictionaries["town"][index][
                    end:
                ]
                if splitted_address_data_dictionaries["town"][index] == "" and re.search(
                    "[町]$", splitted_address_data_dictionaries["district"][index]
                ):
                    # 文字列の分解位置をずらす
                    splitted_address_data_dictionaries["town"][index] = splitted_address_data_dictionaries["district"][
                        index
                    ]
                    splitted_address_data_dictionaries["district"][index] = ""
    # 市貝町
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if re.search("-市$", splitted_address_data_dictionaries["city"][index]):
            start: int = re.search("-市$", splitted_address_data_dictionaries["city"][index]).start()
            end: int = re.search("-市$", splitted_address_data_dictionaries["city"][index]).end()
            if splitted_address_data_dictionaries["town"][index] == "貝町":
                splitted_address_data_dictionaries["town"][index] = "市貝町"
                splitted_address_data_dictionaries["city"][index] = splitted_address_data_dictionaries["city"][index][
                    :start
                ]
    # 市川三郷町
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if re.search("-市$", splitted_address_data_dictionaries["city"][index]):
            start: int = re.search("-市$", splitted_address_data_dictionaries["city"][index]).start()
            end: int = re.search("-市$", splitted_address_data_dictionaries["city"][index]).end()
            if splitted_address_data_dictionaries["town"][index] == "川3郷町":
                splitted_address_data_dictionaries["town"][index] = "市川三郷町"
                splitted_address_data_dictionaries["city"][index] = splitted_address_data_dictionaries["city"][index][
                    :start
                ]
            elif splitted_address_data_dictionaries["town"][index] == "川三郷町":
                splitted_address_data_dictionaries["town"][index] = "市川三郷町"
                splitted_address_data_dictionaries["city"][index] = splitted_address_data_dictionaries["city"][index][
                    :start
                ]
    # 市ケ坂町
    for index in range(len(splitted_address_data_dictionaries["city"])):
        if (
            splitted_address_data_dictionaries["city"][index] == "市"
            and splitted_address_data_dictionaries["town"][index] == "ケ坂町"
        ):
            splitted_address_data_dictionaries["city"][index] = "市ケ坂町"
            splitted_address_data_dictionaries["town"][index] = ""
