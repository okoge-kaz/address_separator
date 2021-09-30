import re


import pandas as pd


def revise_data(data: list):
    # ‐ -> - 変換
    for index in range(len(data)):
        data[index] = re.sub('‐', '-', data[index])

    # ｰ -> - 変換
    for index in range(len(data)):
        data[index] = re.sub('ｰ', '-', data[index])

    # 漢数字が含まれる市町村名、町域などを正常な形に直す
    for index in range(len(data)):
        # 佐賀市鍋島町大字八戸溝
        data[index] = re.sub('佐賀市鍋島町大字8戸溝', '佐賀市鍋島町大字八戸溝', data[index])
        # 佐賀市三瀬村
        data[index] = re.sub('佐賀市3瀬村', '佐賀市三瀬村', data[index])
        # 佐賀市三瀬村三瀬
        data[index] = re.sub('佐賀市3瀬村3瀬', '佐賀市三瀬村三瀬', data[index])
        # 久留米市三瀦郡
        data[index] = re.sub('久留米市3瀦郡', '久留米市三瀦郡', data[index])
        # 佐賀市嘉瀬町大字萩野字四本柳籠
        data[index] = re.sub('佐賀市嘉瀬町大字萩野字4本柳籠', '佐賀市嘉瀬町大字萩野字四本柳籠', data[index])
        # 久留米市三瀦郡
        data[index] = re.sub('久留米市3瀦郡', '久留米市三瀦郡', data[index])
        # 早良区四箇田団地
        data[index] = re.sub('早良区4箇田団地', '早良区四箇田団地', data[index])
        # 早良区四箇田団地
        data[index] = re.sub('早良区4箇田団地', '早良区四箇田団地', data[index])
        # 佐賀市嘉瀬町十五
        data[index] = re.sub('佐賀市嘉瀬町十5', '佐賀市嘉瀬町十五', data[index])
        # 佐賀市鍋島町島田八戸溝
        data[index] = re.sub('佐賀市鍋島町島田8戸溝', '佐賀市鍋島町島田八戸溝', data[index])
        # 佐賀市鍋島町8戸
        data[index] = re.sub('佐賀市鍋島町8戸', '佐賀市鍋島町八戸', data[index])
        # 三瀬村三瀬
        data[index] = re.sub('3瀬村3瀬', '三瀬村三瀬', data[index])
        # 三瀬村三瀬
        data[index] = re.sub('三瀬村3瀬', '三瀬村三瀬', data[index])
        # 三瀬村三瀬
        data[index] = re.sub('3瀬村三瀬', '三瀬村三瀬', data[index])
        # 3瀬村今原
        data[index] = re.sub('3瀬村今原', '三瀬村今原', data[index])
        # 3瀬村杠
        data[index] = re.sub('3瀬村杠', '三瀬村杠', data[index])
        # 3瀬町3瀬
        data[index] = re.sub('3瀬町3瀬', '三瀬町三瀬', data[index])
        # 嘉瀬町大字十5
        data[index] = re.sub('嘉瀬町大字十5', '嘉瀬町大字十五', data[index])
        # 鍋島町大字8戸
        data[index] = re.sub('鍋島町大字8戸', '鍋島町大字八戸', data[index])
        # 鍋島8戸溝
        data[index] = re.sub('鍋島8戸溝', '鍋島八戸溝', data[index])
        # 大和町8反原
        data[index] = re.sub('大和町8反原', '大和町八反原', data[index])
        # 高知市1宮
        data[index] = re.sub('高知市1宮', '高知市一宮', data[index])
        # 高知市9反田
        data[index] = re.sub('高知市9反田', '高知市九反田', data[index])
        # 高知市8反町
        data[index] = re.sub('高知市8反町', '高知市八反町', data[index])
        # 高知市2葉町
        data[index] = re.sub('高知市2葉町', '高知市二葉町', data[index])
        # 6泉寺町
        data[index] = re.sub('6泉寺町', '六泉寺町', data[index])
        # 高知市3谷
        data[index] = re.sub('高知市3谷', '高知市三谷', data[index])
        # 5台山
        data[index] = re.sub('5台山', '五台山', data[index])
        # 9反田
        data[index] = re.sub('9反田', '九反田', data[index])
        # 8反町
        data[index] = re.sub('8反町', '八反町', data[index])
        # 2葉町
        data[index] = re.sub('2葉町', '2葉町', data[index])
        # 豊4季
        data[index] = re.sub('豊4季', '豊四季', data[index])
        # 船橋市3山
        data[index] = re.sub('船橋市3山', '船橋市三山', data[index])
        # 船橋市2宮
        data[index] = re.sub('船橋市2宮', '船橋市二宮', data[index])
        # 8千代
        data[index] = re.sub('8千代', '八千代', data[index])
        # 船橋市2和
        data[index] = re.sub('船橋市2和', '船橋市二和', data[index])
        # 船橋市3咲
        data[index] = re.sub('船橋市3咲', '船橋市三咲', data[index])
        # 那覇市3原
        data[index] = re.sub('那覇市3原', '那覇市三原', data[index])
        # 8重瀬町
        data[index] = re.sub('8重瀬町', '八重瀬町', data[index])
        # 3鷹市
        data[index] = re.sub('3鷹市', '三鷹市', data[index])
        # 三重城
        data[index] = re.sub('3重城', '三重城', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])
        #
        data[index] = re.sub('', '', data[index])

    # 文字化け関連
    for index in range(len(data)):
        # アパ-ト
        data[index] = re.sub('アパ-ト', 'アパート', data[index])
        # コ-ポ
        data[index] = re.sub('コ-ポ', 'コーポ', data[index])
        # フラワ-
        data[index] = re.sub('フラワ-', 'フラワー', data[index])
        # ベリ-ズコ-ト
        data[index] = re.sub('ベリ-ズコ-ト', 'ベリーズコート', data[index])
        # パ-クハイム
        data[index] = re.sub('パ-クハイム', 'パークハイム', data[index])
        # パ-クハウス
        data[index] = re.sub('パ-クハウス', 'パークハウス', data[index])
        # テ-ラ-
        data[index] = re.sub('テ-ラ-', 'テーラー', data[index])

    # -が2回連続する箇所を-に直す
    for index in range(len(data)):
        data[index] = re.sub('-{1,}', '-', data[index])

    # -の を -に置換する
    for index in range(len(data)):
        if re.search('-の[0-9]+', data[index]):
            data[index] = re.sub('-の', '-', data[index])
        if re.search('[0-9]+の[0-9]+', data[index]):
            data[index] = re.sub('[0-9]+の[0-9]+', data[index])

    # for debug
    df = pd.DataFrame(data)
    df.to_csv('data.csv', encoding='utf-8_sig')
    # for debug end
