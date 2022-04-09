import re


def shaping(AddressDataForFormatting) -> None:
    """
    args: AddressDataForFormatting
    return: void
    分割等が終了したデータに対して、これらを出力用に整形する。
    特殊な名前の市町村等のデータについても、ここで整形作業を行う.
    """
    # データの最終整形 都市名のうち半角数字のものは漢字に直す
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] == "":
            continue
        if re.search("[1-9]", AddressDataForFormatting.city[index]) is not None:
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
            for char in AddressDataForFormatting.city[index]:
                if char in numbers:
                    shaped += mapping_dictionary[char]
                else:
                    shaped += char
            AddressDataForFormatting.city[index] = shaped
        else:
            pass
    # 上記と同様のことをtownでもやる。ただし漢字+ひらがな+算用数字のときのみ
    for index in range(len(AddressDataForFormatting.town)):
        if AddressDataForFormatting.town[index] == "":
            continue
        if re.search("[1-9]", AddressDataForFormatting.town[index]) is not None:
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
            for char in AddressDataForFormatting.town[index]:
                if char in numbers:
                    shaped += mapping_dictionary[char]
                else:
                    shaped += char
            # 一-町 -> 一番町に変える
            if re.search("[一-九]-町", shaped):
                match = re.search("[一-九]-町", shaped)
                assert match is not None
                start: int = match.start()
                shaped = shaped[: start + 1] + "番" + shaped[start + 2 :]

            AddressDataForFormatting.town[index] = shaped
        else:
            pass
    # city の先頭または末尾に-があったら除去
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] == "":
            continue
        if AddressDataForFormatting.city[index][0] == "-":
            AddressDataForFormatting.city[index] = AddressDataForFormatting.city[index][1:]
        if len(AddressDataForFormatting.city[index]) < 1:
            continue
        if AddressDataForFormatting.city[index][-1] == "-":
            AddressDataForFormatting.city[index] = AddressDataForFormatting.city[index][:-1]
    # town の先頭または末尾に-があったら除去
    for index in range(len(AddressDataForFormatting.town)):
        if AddressDataForFormatting.town[index] == "":
            continue
        if AddressDataForFormatting.town[index][0] == "-":
            AddressDataForFormatting.town[index] = AddressDataForFormatting.town[index][1:]
        if len(AddressDataForFormatting.town[index]) < 1:
            continue
        if AddressDataForFormatting.town[index][-1] == "-":
            AddressDataForFormatting.town[index] = AddressDataForFormatting.town[index][:-1]
    # district の先頭または末尾に-があったら除去
    for index in range(len(AddressDataForFormatting.district)):
        if AddressDataForFormatting.district[index] == "":
            continue
        if AddressDataForFormatting.district[index][0] == "-":
            AddressDataForFormatting.district[index] = AddressDataForFormatting.district[index][1:]
        if len(AddressDataForFormatting.district[index]) < 1:
            continue
        if AddressDataForFormatting.district[index][-1] == "-":
            AddressDataForFormatting.district[index] = AddressDataForFormatting.district[index][:-1]
    # 東京都 町田など、固有名詞に 市、町、区、町、村があるもの
    # 町田市
    for index in range(len(AddressDataForFormatting.district)):
        if AddressDataForFormatting.district[index] == "":
            continue
        if AddressDataForFormatting.district[index] == "田":
            if AddressDataForFormatting.town[index] == "":
                continue
            if AddressDataForFormatting.town[index][-1] == "町":
                AddressDataForFormatting.town[index] += "田"
                AddressDataForFormatting.district[index] = ""
            else:
                pass
        else:
            pass
    # 市川市
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] == "市" and re.search("^川市", AddressDataForFormatting.district[index]):
            match = re.search("^川市", AddressDataForFormatting.district[index])
            assert match is not None
            start: int = match.start()
            end: int = match.end()
            if start != 0:
                print("something wrong")  # for debug
            AddressDataForFormatting.city[index] = "市川市"
            AddressDataForFormatting.district[index] = AddressDataForFormatting.district[index][end:]

        elif AddressDataForFormatting.district[index] == "":
            # どこに残骸があるか不明なので
            if AddressDataForFormatting.city[index] == "市" and re.search("^川市", AddressDataForFormatting.town[index]):
                match = re.search("^川市", AddressDataForFormatting.town[index])
                assert match is not None
                start: int = match.start()
                end: int = match.end()
                if start != 0:
                    print("something wrong")  # for debug
                AddressDataForFormatting.city[index] = "市川市"
                AddressDataForFormatting.town[index] = AddressDataForFormatting.town[index][end:]
    # 市原市
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] == "市" and re.search("^原市", AddressDataForFormatting.district[index]):
            match = re.search("^原市", AddressDataForFormatting.district[index])
            assert match is not None
            start: int = match.start()
            end: int = match.end()
            if start != 0:
                print("something wrong")  # for debug
            AddressDataForFormatting.city[index] = "市原市"
            AddressDataForFormatting.district[index] = AddressDataForFormatting.district[index][end:]

        elif AddressDataForFormatting.district[index] == "":
            # どこに残骸があるか不明なので
            if AddressDataForFormatting.city[index] == "市" and re.search("^原市", AddressDataForFormatting.town[index]):
                match = re.search("^原市", AddressDataForFormatting.town[index])
                assert match is not None
                start: int = match.start()
                end: int = match.end()
                if start != 0:
                    print("something wrong")  # for debug
                AddressDataForFormatting.city[index] = "市原市"
                AddressDataForFormatting.town[index] = AddressDataForFormatting.town[index][end:]
    # 野々市市
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] == "野々市" and re.search("^市", AddressDataForFormatting.district[index]):
            match = re.search("^市", AddressDataForFormatting.district[index])
            assert match is not None
            start: int = match.start()
            end: int = match.end()
            if start != 0:
                print("something wrong")  # for debug
            AddressDataForFormatting.city[index] = "野々市市"
            AddressDataForFormatting.district[index] = AddressDataForFormatting.district[index][end:]

        elif AddressDataForFormatting.district[index] == "":
            # どこに残骸があるか不明なので
            if AddressDataForFormatting.city[index] == "野々市" and re.search("^市", AddressDataForFormatting.town[index]):
                match = re.search("^市", AddressDataForFormatting.town[index])
                assert match is not None
                start: int = match.start()
                end: int = match.end()
                if start != 0:
                    print("something wrong")  # for debug
                AddressDataForFormatting.city[index] = "野々市市"
                AddressDataForFormatting.town[index] = AddressDataForFormatting.town[index][end:]
    # 四日市市
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] == "四日市" and re.search("^市", AddressDataForFormatting.district[index]):
            match = re.search("^市", AddressDataForFormatting.district[index])
            assert match is not None
            start: int = match.start()
            end: int = match.end()
            if start != 0:
                print("something wrong")  # for debug
            AddressDataForFormatting.city[index] = "四日市市"
            AddressDataForFormatting.district[index] = AddressDataForFormatting.district[index][end:]

        elif AddressDataForFormatting.district[index] == "":
            # どこに残骸があるか不明なので
            if AddressDataForFormatting.city[index] == "四日市" and re.search("^市", AddressDataForFormatting.town[index]):
                match = re.search("^市", AddressDataForFormatting.town[index])
                assert match is not None
                start: int = match.start()
                end: int = match.end()
                if start != 0:
                    print("something wrong")  # for debug
                AddressDataForFormatting.city[index] = "四日市市"
                AddressDataForFormatting.town[index] = AddressDataForFormatting.town[index][end:]
    # 廿日市市
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] == "廿日市" and re.search("^市", AddressDataForFormatting.district[index]):
            match = re.search("^市", AddressDataForFormatting.district[index])
            assert match is not None
            start: int = match.start()
            end: int = match.end()
            if start != 0:
                print("something wrong")  # for debug
            AddressDataForFormatting.city[index] = "廿日市市"
            AddressDataForFormatting.district[index] = AddressDataForFormatting.district[index][end:]

        elif AddressDataForFormatting.district[index] == "":
            # どこに残骸があるか不明なので
            if AddressDataForFormatting.city[index] == "廿日市" and re.search("^市", AddressDataForFormatting.town[index]):
                match = re.search("^市", AddressDataForFormatting.town[index])
                assert match is not None
                start: int = match.start()
                end: int = match.end()
                if start != 0:
                    print("something wrong")  # for debug
                AddressDataForFormatting.city[index] = "廿日市市"
                AddressDataForFormatting.town[index] = AddressDataForFormatting.town[index][end:]
    # 余市軍
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] == "余市" and re.search("^郡", AddressDataForFormatting.district[index]):
            match = re.search("^郡", AddressDataForFormatting.district[index])
            assert match is not None
            start: int = match.start()
            end: int = match.end()
            if start != 0:
                print("something wrong")  # for debug
            AddressDataForFormatting.city[index] = "余市郡"
            AddressDataForFormatting.district[index] = AddressDataForFormatting.district[index][end:]

        elif AddressDataForFormatting.district[index] == "":
            # どこに残骸があるか不明なので
            if AddressDataForFormatting.city[index] == "余市" and re.search("^郡", AddressDataForFormatting.town[index]):
                match = re.search("^郡", AddressDataForFormatting.town[index])
                assert match is not None
                start: int = match.start()
                end: int = match.end()
                if start != 0:
                    print("something wrong")  # for debug
                AddressDataForFormatting.city[index] = "余市郡"
                AddressDataForFormatting.town[index] = AddressDataForFormatting.town[index][end:]
        elif re.search("^[- 0-9 町 市]", AddressDataForFormatting.district[index]) is None:
            # どこに残骸があるか不明なので
            if AddressDataForFormatting.city[index] == "余市" and re.search("^郡", AddressDataForFormatting.town[index]):
                match = re.search("^郡", AddressDataForFormatting.town[index])
                assert match is not None
                start: int = match.start()
                end: int = match.end()
                if start != 0:
                    print("something wrong")  # for debug
                AddressDataForFormatting.city[index] = "余市郡"
                AddressDataForFormatting.town[index] = AddressDataForFormatting.town[index][end:]
                if AddressDataForFormatting.town[index] == "" and re.search(
                    "[町]$", AddressDataForFormatting.district[index]
                ):
                    # 文字列の分解位置をずらす
                    AddressDataForFormatting.town[index] = AddressDataForFormatting.district[index]
                    AddressDataForFormatting.district[index] = ""
    # 市貝町
    for index in range(len(AddressDataForFormatting.city)):
        if re.search("-市$", AddressDataForFormatting.city[index]):
            match = re.search("-市$", AddressDataForFormatting.city[index])
            assert match is not None
            start: int = match.start()
            end: int = match.end()
            if AddressDataForFormatting.town[index] == "貝町":
                AddressDataForFormatting.town[index] = "市貝町"
                AddressDataForFormatting.city[index] = AddressDataForFormatting.city[index][:start]
    # 市川三郷町
    for index in range(len(AddressDataForFormatting.city)):
        if re.search("-市$", AddressDataForFormatting.city[index]):
            match = re.search("-市$", AddressDataForFormatting.city[index])
            assert match is not None
            start: int = match.start()
            end: int = match.end()
            if AddressDataForFormatting.town[index] == "川3郷町":
                AddressDataForFormatting.town[index] = "市川三郷町"
                AddressDataForFormatting.city[index] = AddressDataForFormatting.city[index][:start]
            elif AddressDataForFormatting.town[index] == "川三郷町":
                AddressDataForFormatting.town[index] = "市川三郷町"
                AddressDataForFormatting.city[index] = AddressDataForFormatting.city[index][:start]
    # 市ケ坂町
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] == "市" and AddressDataForFormatting.town[index] == "ケ坂町":
            AddressDataForFormatting.city[index] = "市ケ坂町"
            AddressDataForFormatting.town[index] = ""
