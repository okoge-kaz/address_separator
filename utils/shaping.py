import re


def erase_special_address_expression(string: str, index: int):
    """string: 住所データ１つ, index: 処理番号
    処理番号によって処理する内容が変化する。
    """
    size: int = len(string)

    # 丁目を置換することのみ行う
    if index == 1:
        # 正規表現で書くのが困難なため文字列を直接処理
        res: str = ""
        i: int = 0
        while i < (size):
            if i == size - 1:
                res = res + string[i]
                i += 1
            else:
                if string[i] == "丁" and string[i + 1] == "目":
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
    elif index == 2:
        return re.sub("番地", "-", string)
    # 番を置換することのみ行う
    elif index == 3:
        return re.sub("番", "-", string)
    # 1の4 -> 1-4に置換する && 全角数字の置き換え
    elif index == 4:
        while re.search("[0-9 ０-９]+の[0-9 ０-９]", string) is not None:

            start: int
            end: int

            regular_expression_start = re.search("[0-9 ０-９]+の[0-9 ０-９]", string)
            if regular_expression_start is not None:
                start = regular_expression_start.start()

            regular_expression_end = re.search("[0-9 ０-９]+の[0-9 ０-９]", string)
            if regular_expression_end is not None:
                end = regular_expression_end.end()

            res: str = ""
            res += string[:start]
            for index in range(start, end):
                if string[index] == "の":
                    res += "-"
                else:
                    if re.search("[０-９]", string[index]) is not None:
                        mapping_dictionary: dict = {
                            "１": "1",
                            "２": "2",
                            "３": "3",
                            "４": "4",
                            "５": "5",
                            "６": "6",
                            "７": "7",
                            "８": "8",
                            "９": "9",
                            "０": "10",
                        }
                        res += mapping_dictionary[string[index]]
                    else:
                        res += string[index]
            res += string[end:]
            string = res
        return string
    elif index == 5:
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
        return string[0:-1]
    else:
        return string


def replace_slash_with_hyphen(string: str):
    """半角ハイフンに置き換える"""
    string = re.sub(" ", "-", string)
    string = re.sub("　", "-", string)
    string = re.sub("\t", "-", string)
    # 日本語で数字をつなぐ際に出現しうる
    string = re.sub("−", "-", string)
    string = re.sub("─", "-", string)
    string = re.sub("—", "-", string)
    # 改行を半角スペースで置き換える
    string = re.sub("\n", "-", string)
    # 正規表現で/を-に置き換える
    return re.sub("/", "-", string)


def japanese_style_number_to_number(string: str):
    def function(char: str):
        dictionary_japanese_style_number: dict = {
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
        return dictionary_japanese_style_number[char]

    def full_width_to_half_width(char: str):
        """全角数字を半角数字に変換"""
        mapping_dictionary: dict = {
            "１": "1",
            "２": "2",
            "３": "3",
            "４": "4",
            "５": "5",
            "６": "6",
            "７": "7",
            "８": "8",
            "９": "9",
            "０": "0",
        }
        if re.search("[０-９]", char):
            # 全角数字が存在する
            return mapping_dictionary[char]
        else:
            return char

    # 以降実際の処理
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
    return re.sub("ー", "-", string)


def operation(string: str):
    """すべての処理をまとめた関数"""
    res: str = replace_japanese_address_expression(string)
    res = erase_last_hyphen(res)
    res = replace_slash_with_hyphen(res)
    res = japanese_style_number_to_number(res)
    res = full_width_hyphen_to_half_width_hyphen(res)
    return res
