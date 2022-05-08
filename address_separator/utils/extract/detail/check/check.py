from __future__ import annotations

import re


def check(data: dict, others_tail: list[str]) -> list[str]:
    """
    cautionの配列を生成する
    """

    def check_valid_word_or_not(index: int):
        if re.search("^([0-9ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠-])+$", data["invalid"][index]) is not None:
            # 愛知県名古屋市天白区天白町平針黒石２８４５平針住宅14-24
            if re.search("^[0-9]{2,}", data["invalid"][index]) is not None:
                match = re.search("^[0-9]{2,}", data["invalid"][index])
                assert match is not None
                invalid_word = data["invalid"][index]
                if index is not None:
                    others_tail[index] = invalid_word[match.end() :] + data["house_number"][index] + others_tail[index]
                    data["house_number"][index] = invalid_word[0 : match.end()]
                    data["invalid"][index] = ""

            MAPPING_ARITHMETIC_NUMBER_TO_JAPANESE_NUMBER: dict = {
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
            for char in data["invalid"][index]:
                if char in numbers:
                    res = res + MAPPING_ARITHMETIC_NUMBER_TO_JAPANESE_NUMBER[char]
                else:
                    res = res + char
            return res
        else:
            return ""

    caution: list = []
    for index in range(len(data["invalid"])):
        response: str = check_valid_word_or_not(index)
        if data["invalid"][index] == "":
            caution.append("")
        elif response == "":
            # 不正な文字列
            caution.append("ERROR: データは、整形不可能な状態です。自動整形システムは正しく動作しません。この行の全ての結果を確認することを推奨します。  ")
        else:
            caution.append("")
            data["invalid"][index] = ""
            data["district"][index] += response
    return caution
