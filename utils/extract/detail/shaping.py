import re


def shaping(data: dict):
    # データの最終整形 都市名のうち半角数字のものは漢字に直す
    for index in range(len(data['city'])):
        if data['city'][index] == "":
            continue
        if re.search('[1-9]', data['city'][index]) is not None:
            shaped: str = ""
            mapping_dictionary: dict = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五",
                                        "6": "六", "7": "七", "8": "八", "9": "九"}
            numbers: list = [
                "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for char in data['city'][index]:
                if char in numbers:
                    shaped += mapping_dictionary[char]
                else:
                    shaped += char
            data['city'][index] = shaped
        else:
            pass
    # 東京都 町田など、固有名詞に 市、町、区、町、村があるもの
    # 町田市
    for index in range(len(data['district'])):
        if data['district'][index] == "":
            continue
        if data['district'][index] == "田":
            if data['town'][index][-1] == "町":
                data['town'][index] += "田"
                data['district'][index] = ""
            else:
                pass
        else:
            pass
    # 市川市
    # 市原市
    # 野々市市
    # 四日市市
    # 陶火待ちし