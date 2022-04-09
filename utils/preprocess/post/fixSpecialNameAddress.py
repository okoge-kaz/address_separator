from __future__ import annotations

import re


def reshape_exceptional_address_address_data_array(address_data_array: list[str]) -> None:
    """
    args: address_data_array: list[str], 住所データ
    return: void, 配列データ自体を修正する
    """

    ADDRESS_address_data_array_ARRAY_SIZE: int = len(address_data_array)

    # ‐ -> - 変換
    for index in range(ADDRESS_address_data_array_ARRAY_SIZE):
        address_data_array[index] = re.sub("‐", "-", address_data_array[index])

    # ｰ -> - 変換
    for index in range(ADDRESS_address_data_array_ARRAY_SIZE):
        address_data_array[index] = re.sub("ｰ", "-", address_data_array[index])

    # 漢数字が含まれる市町村名、町域などを正常な形に直す
    for index in range(ADDRESS_address_data_array_ARRAY_SIZE):
        """
        地名に漢数字が含まれている地名を正常な形に直す
        ルールベースの処理
        """
        # 佐賀市鍋島町大字八戸溝
        address_data_array[index] = re.sub("佐賀市鍋島町大字8戸溝", "佐賀市鍋島町大字八戸溝", address_data_array[index])
        # 佐賀市三瀬村
        address_data_array[index] = re.sub("佐賀市3瀬村", "佐賀市三瀬村", address_data_array[index])
        # 佐賀市三瀬村三瀬
        address_data_array[index] = re.sub("佐賀市3瀬村3瀬", "佐賀市三瀬村三瀬", address_data_array[index])
        # 久留米市三瀦郡
        address_data_array[index] = re.sub("久留米市3瀦郡", "久留米市三瀦郡", address_data_array[index])
        # 佐賀市嘉瀬町大字萩野字四本柳籠
        address_data_array[index] = re.sub("佐賀市嘉瀬町大字萩野字4本柳籠", "佐賀市嘉瀬町大字萩野字四本柳籠", address_data_array[index])
        # 久留米市三瀦郡
        address_data_array[index] = re.sub("久留米市3瀦郡", "久留米市三瀦郡", address_data_array[index])
        # 早良区四箇田団地
        address_data_array[index] = re.sub("早良区4箇田団地", "早良区四箇田団地", address_data_array[index])
        # 早良区四箇田団地
        address_data_array[index] = re.sub("早良区4箇田団地", "早良区四箇田団地", address_data_array[index])
        # 佐賀市嘉瀬町十五
        address_data_array[index] = re.sub("佐賀市嘉瀬町十5", "佐賀市嘉瀬町十五", address_data_array[index])
        # 佐賀市鍋島町島田八戸溝
        address_data_array[index] = re.sub("佐賀市鍋島町島田8戸溝", "佐賀市鍋島町島田八戸溝", address_data_array[index])
        # 佐賀市鍋島町8戸
        address_data_array[index] = re.sub("佐賀市鍋島町8戸", "佐賀市鍋島町八戸", address_data_array[index])
        # 三瀬村三瀬
        address_data_array[index] = re.sub("3瀬村3瀬", "三瀬村三瀬", address_data_array[index])
        # 三瀬村三瀬
        address_data_array[index] = re.sub("三瀬村3瀬", "三瀬村三瀬", address_data_array[index])
        # 三瀬村三瀬
        address_data_array[index] = re.sub("3瀬村三瀬", "三瀬村三瀬", address_data_array[index])
        # 3瀬村今原
        address_data_array[index] = re.sub("3瀬村今原", "三瀬村今原", address_data_array[index])
        # 3瀬村杠
        address_data_array[index] = re.sub("3瀬村杠", "三瀬村杠", address_data_array[index])
        # 3瀬町3瀬
        address_data_array[index] = re.sub("3瀬町3瀬", "三瀬町三瀬", address_data_array[index])
        # 嘉瀬町大字十5
        address_data_array[index] = re.sub("嘉瀬町大字十5", "嘉瀬町大字十五", address_data_array[index])
        # 鍋島町大字8戸
        address_data_array[index] = re.sub("鍋島町大字8戸", "鍋島町大字八戸", address_data_array[index])
        # 鍋島8戸溝
        address_data_array[index] = re.sub("鍋島8戸溝", "鍋島八戸溝", address_data_array[index])
        # 大和町8反原
        address_data_array[index] = re.sub("大和町8反原", "大和町八反原", address_data_array[index])
        # 高知市1宮
        address_data_array[index] = re.sub("高知市1宮", "高知市一宮", address_data_array[index])
        # 高知市9反田
        address_data_array[index] = re.sub("高知市9反田", "高知市九反田", address_data_array[index])
        # 高知市8反町
        address_data_array[index] = re.sub("高知市8反町", "高知市八反町", address_data_array[index])
        # 高知市2葉町
        address_data_array[index] = re.sub("高知市2葉町", "高知市二葉町", address_data_array[index])
        # 6泉寺町
        address_data_array[index] = re.sub("6泉寺町", "六泉寺町", address_data_array[index])
        # 高知市3谷
        address_data_array[index] = re.sub("高知市3谷", "高知市三谷", address_data_array[index])
        # 5台山
        address_data_array[index] = re.sub("5台山", "五台山", address_data_array[index])
        # 9反田
        address_data_array[index] = re.sub("9反田", "九反田", address_data_array[index])
        # 8反町
        address_data_array[index] = re.sub("8反町", "八反町", address_data_array[index])
        # 2葉町
        address_data_array[index] = re.sub("2葉町", "二葉町", address_data_array[index])
        # 豊4季
        address_data_array[index] = re.sub("豊4季", "豊四季", address_data_array[index])
        # 船橋市3山
        address_data_array[index] = re.sub("船橋市3山", "船橋市三山", address_data_array[index])
        # 船橋市2宮
        address_data_array[index] = re.sub("船橋市2宮", "船橋市二宮", address_data_array[index])
        # 8千代
        address_data_array[index] = re.sub("8千代", "八千代", address_data_array[index])
        # 船橋市2和
        address_data_array[index] = re.sub("船橋市2和", "船橋市二和", address_data_array[index])
        # 船橋市3咲
        address_data_array[index] = re.sub("船橋市3咲", "船橋市三咲", address_data_array[index])
        # 那覇市3原
        address_data_array[index] = re.sub("那覇市3原", "那覇市三原", address_data_array[index])
        # 8重瀬町
        address_data_array[index] = re.sub("8重瀬町", "八重瀬町", address_data_array[index])
        # 3鷹市
        address_data_array[index] = re.sub("3鷹市", "三鷹市", address_data_array[index])
        # 3鷹
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+3鷹", address_data_array[index]):
            if re.search("[0-9]+3鷹", address_data_array[index]):
                continue
            if re.search("([0-9]+)-3鷹", address_data_array[index]):
                continue
            address_data_array[index] = re.sub("3鷹", "三鷹", address_data_array[index])
        # 三重城
        address_data_array[index] = re.sub("3重城", "三重城", address_data_array[index])
        # 八町
        if re.search("[ぁ-んァ-ヶｱ-ﾝﾞﾟ一-龠]+8町", address_data_array[index]):
            if re.search("[0-9]+8町", address_data_array[index]):
                continue
            if re.search("([0-9]+)-8町", address_data_array[index]):
                continue
            address_data_array[index] = re.sub("8町", "八町", address_data_array[index])
        # 佐賀県3養
        address_data_array[index] = re.sub("佐賀県3養", "佐賀県三養", address_data_array[index])
        # 佐賀市8戸
        address_data_array[index] = re.sub("佐賀市8戸", "佐賀市八戸", address_data_array[index])
        # 3王崎
        address_data_array[index] = re.sub("3王崎", "三王崎", address_data_array[index])
        # 小城市3日月
        address_data_array[index] = re.sub("小城市3日月", "小城市三日月", address_data_array[index])
        # 白木1色
        address_data_array[index] = re.sub("白木1色", "白木一色", address_data_array[index])
        # 3重県
        address_data_array[index] = re.sub("3重県", "三重県", address_data_array[index])
        # 3園平
        address_data_array[index] = re.sub("3園平", "三園平", address_data_array[index])
        #
        address_data_array[index] = re.sub("", "", address_data_array[index])

    # 文字化け関連
    for index in range(len(address_data_array)):
        # アパ-ト
        address_data_array[index] = re.sub("アパ-ト", "アパート", address_data_array[index])
        # コ-ポ
        address_data_array[index] = re.sub("コ-ポ", "コーポ", address_data_array[index])
        # フラワ-
        address_data_array[index] = re.sub("フラワ-", "フラワー", address_data_array[index])
        # ベリ-ズコ-ト
        address_data_array[index] = re.sub("ベリ-ズコ-ト", "ベリーズコート", address_data_array[index])
        # パ-クハイム
        address_data_array[index] = re.sub("パ-クハイム", "パークハイム", address_data_array[index])
        # パ-クハウス
        address_data_array[index] = re.sub("パ-クハウス", "パークハウス", address_data_array[index])
        # テ-ラ-
        address_data_array[index] = re.sub("テ-ラ-", "テーラー", address_data_array[index])

    # -が2回連続する箇所を-に直す
    for index in range(len(address_data_array)):
        address_data_array[index] = re.sub("-{1,}", "-", address_data_array[index])

    # -の を -に置換する
    for index in range(len(address_data_array)):
        if re.search("-の[0-9]+", address_data_array[index]):
            address_data_array[index] = re.sub("-の", "-", address_data_array[index])
        if re.search("[0-9]+の[0-9]+", address_data_array[index]):
            shaped_string: str = ""
            for id in range(len(address_data_array[index])):
                if address_data_array[index][id] == "の" and id > 0 and id + 1 < len(address_data_array[index]):
                    if (
                        "0" <= address_data_array[index][id - 1]
                        and address_data_array[index][id - 1] <= "9"
                        and address_data_array[index][id + 1] >= "0"
                        and address_data_array[index][id + 1] <= "9"
                    ):
                        # 〜の〜　前後が数字であるとき
                        shaped_string += "-"
                    else:
                        shaped_string += address_data_array[index][id]
                else:
                    shaped_string += address_data_array[index][id]
            address_data_array[index] = shaped_string
