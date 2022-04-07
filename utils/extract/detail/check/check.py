import re


def check(data) -> list[str]:
    """
    args: data
    return: void
    cautionの配列を生成する
    """

    def check_vaild_word_or_not(index: int) -> str:
        if re.search("^([0-9ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠])+$", data.invalid[index]) is not None:
            mapping_arithmetic_number_to_japanese_number: dict = {
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
            numbers: list = [str(i) for i in range(1, 10)]
            res: str = ""
            for char in data.invalid[index]:
                if char in numbers:
                    res = res + mapping_arithmetic_number_to_japanese_number[char]
                else:
                    res = res + char
            return res
        else:
            return ""

    caution: list = []
    for index in range(len(data.invalid)):
        response: str = check_vaild_word_or_not(index)
        if data.invalid[index] == "":
            caution.append("")
        elif response == "":
            # 不正な文字列
            caution.append("ERROR: データは、整形不可能な状態です。自動整形システムは正しく動作しません。この行の全ての結果を確認することを推奨します。  ")
        else:
            caution.append("")
            data.invalid[index] = ""
            data.district[index] += response
    return caution
