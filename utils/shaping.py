import re


def find_prefacture(string: str):
    # 北海道,大阪府,京都府,東京都は別扱い
    special_prefactures: list = ["北海道", "大阪府", "京都府", "東京都"]
    for _ in special_prefactures:
        if _ in string:
            return (_,)


def erase_special_address_expression(string: str, index: int):
    size: int = len(string)
    # 丁目を置換することのみ行う
    if index == 1:
        res: str = ""
        i: int = 0
        while i < (size):
            if i == size - 1:
                res = res + string[i]
                i += 1
            else:
                if(string[i] == '丁' and string[i + 1] == '目'):
                    # 丁目店などは特殊ケースとして除外
                    if i + 2 < size and string[i + 2] == "店":
                        res = res + string[i]
                        i += 1
                        continue
                    res = res + ("-")
                    i += 2
                else:
                    res = res + (string[i])
                    i += 1
        return res
    # 番地を置換することのみ行う
    if index == 2:
        res: str = ""
        i: int = 0
        while i < size:
            if i == size - 1:
                res = res + string[i]
                i += 1
            else:
                if(string[i] == "番" and string[i + 1] == "地"):
                    res = res + ("-")
                    i += 2
                else:
                    res = res + (string[i])
                    i += 1
        return res
    # 番を置換することのみ行う
    if index == 3:
        res: str = ""
        for i in range(size):
            if string[i] == "番":
                res = res + ("-")
            else:
                res = res + (string[i])
        return res
    # の を置換する
    if index == 4:
        res: str = ""

        numbers: list = []
        for i in range(10):
            numbers.append(str(i))
        for i in range(size):
            if i > 0 and i + 1 < size and string[i] == "の" and string[i - 1] in numbers:
                res = res + "-"
            else:
                res = res + string[i]
        return res
    if index == 5:
        return string.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))


def replace_japanese_address_expression(string: str):
    # ~丁目,~番,~番地を-に変換
    # 注意: 番地 -> 番 の順番に行わないとデータが壊れる
    if "丁目" in string:
        string = erase_special_address_expression(string, 1)
    if "番地" in string:
        string = erase_special_address_expression(string, 2)
    if "番" in string:
        string = erase_special_address_expression(string, 3)
    if "の" in string:
        string = erase_special_address_expression(string, 4)
    string = erase_special_address_expression(string, 5)
    return string


def erase_last_hyphen(string: str):
    if string[-1] == "-":
        return string[0:len(string) - 1]
    else:
        return string


def replace_slash_with_hyphen(string: str):
    # 空白を取り除く
    string = string.replace(' ', '-')
    string = string.replace('　', '-')
    # 正規表現で/を-に置き換える
    return re.sub("/", "-", string)


def japanese_style_number_to_number(string: str):
    def function(char: str):
        dictionary_japanese_style_number: dict =  \
            {"一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6",
                "七": "7", "八": "8", "九": "9", "十": "10", "〇": "0"}
        return dictionary_japanese_style_number[char]

    def full_width_to_half_width(char: str):
        mapping_dictionary: dict = \
            {"１": "1", "２": "2", "３": "3", "４": "4", "５": "5",
                "６": "6", "７": "7", "８": "8", "９": "9", "０": "10"}
        full_width_number: list = ["１", "２", "３", "４", "５", "６", "７", "８", "９", "０"]
        if char in full_width_number:
            return mapping_dictionary[c]
        else:
            return char
    japanese_style_number: list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "〇"]
    # 十と表記する際は高確率で地名なので
    res: str = ""
    for c in string:
        if c in japanese_style_number:
            res = res + full_width_to_half_width(function(c))
        else:
            res = res + full_width_to_half_width(c)
    return res


def full_width_hyphen_to_half_width_hyphen(string: str):
    res: str = ""
    for char in string:
        if char == "ー":
            res = res + "-"
        else:
            res = res + char
    return res


def operation(string: str):
    return full_width_hyphen_to_half_width_hyphen(japanese_style_number_to_number(
        replace_slash_with_hyphen(erase_last_hyphen(replace_japanese_address_expression(string)))))
