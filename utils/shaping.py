import re


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
    elif index == 2:
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
    elif index == 3:
        res: str = ""
        for i in range(size):
            if string[i] == "番":
                res = res + ("-")
            else:
                res = res + (string[i])
        return res
    # 1の4 -> 1-4に置換する && 全角数字の置き換え
    elif index == 4:
        while re.search('[0-9 ０-９]+の[0-9 ０-９]', string) is not None:
            start: int = re.search('[0-9 ０-９]+の[0-9 ０-９]', string).start()
            end: int = re.search('[0-9 ０-９]+の[0-9 ０-９]', string).end()
            res: str = ""
            res += string[:start]
            for index in range(start, end):
                if string[index] == 'の':
                    res += '-'
                else:
                    if re.search('[０-９]', string[index]) is not None:
                        mapping_dictionary: dict = \
                            {"１": "1", "２": "2", "３": "3", "４": "4", "５": "5",
                             "６": "6", "７": "7", "８": "8", "９": "9", "０": "10"}
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
    # 空白を取り除く
    string = re.sub(' ', '-', string)
    string = re.sub('　', '-', string)
    string = re.sub('\t', '-', string)
    # 日本語で数字をつなぐ際に出現しうる
    string = re.sub('−', '-', string)
    string = re.sub('─', '-', string)
    # 正規表現で/を-に置き換える
    return re.sub("/", "-", string)


def japanese_style_number_to_number(string: str):
    def function(char: str):
        dictionary_japanese_style_number: dict =  \
            {"一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6",
                "七": "7", "八": "8", "九": "9", "十": "10", "〇": "0"}
        return dictionary_japanese_style_number[char]

    def full_width_to_half_width(char: str):
        '''全角数字を半角数字に変換'''
        mapping_dictionary: dict = \
            {"１": "1", "２": "2", "３": "3", "４": "4", "５": "5",
                "６": "6", "７": "7", "８": "8", "９": "9", "０": "0"}
        if re.search('[０-９]', char):
            # 全角数字が存在する
            return mapping_dictionary[char]
        else:
            return char
    # 以降実際の処理
    japanese_style_number: list = [
        "一", "二", "三", "四", "五", "六", "七", "八", "九", "〇"]
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
