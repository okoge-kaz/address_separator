import re


def shaping(data: dict):
    '''分割等が終了したデータに対して、これらを出力用に整形する'''
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
    # 上記と同様のことをtownでもやる。ただし漢字+ひらがな+算用数字のときのみ
    for index in range(len(data['town'])):
        if data['town'][index] == "":
            continue
        if re.search('[1-9]', data['town'][index]) is not None:
            shaped: str = ""
            mapping_dictionary: dict = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五",
                                        "6": "六", "7": "七", "8": "八", "9": "九"}
            numbers: list = [
                "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for char in data['town'][index]:
                if char in numbers:
                    shaped += mapping_dictionary[char]
                else:
                    shaped += char
            # 一-町 -> 一番町に変える
            if re.search('[一-九]-町', shaped):
                start: int = re.search('[一-九]-町', shaped).start()
                shaped = shaped[:start + 1] + '番' + shaped[start + 2:]

            data['town'][index] = shaped
        else:
            pass
    # city の先頭または末尾に-があったら除去
    for index in range(len(data['city'])):
        if data['city'][index] == "":
            continue
        if data['city'][index][0] == '-':
            data['city'][index] = data['city'][index][1:]
        if data['city'][index][-1] == '-':
            data['city'][index] = data['city'][index][:-1]
    # town の先頭または末尾に-があったら除去
    for index in range(len(data['town'])):
        if data['town'][index] == "":
            continue
        if data['town'][index][0] == '-':
            data['town'][index] = data['town'][index][1:]
        if data['town'][index][-1] == '-':
            data['town'][index] = data['town'][index][:-1]
    # district の先頭または末尾に-があったら除去
    for index in range(len(data['district'])):
        if data['district'][index] == '':
            continue
        if data['district'][index][0] == '-':
            data['district'][index] = data['district'][index][1:]
        if data['district'][index][-1] == '-':
            data['district'][index] = data['district'][index][:-1]
    # 東京都 町田など、固有名詞に 市、町、区、町、村があるもの
    # 町田市
    for index in range(len(data['district'])):
        if data['district'][index] == "":
            continue
        if data['district'][index] == "田":
            if data['town'][index] == '':
                continue
            if data['town'][index][-1] == "町":
                data['town'][index] += "田"
                data['district'][index] = ""
            else:
                pass
        else:
            pass
    # 市川市
    for index in range(len(data['city'])):
        if data['city'][index] == '市' and re.search('^川市', data['district'][index]):
            start: int = re.search('^川市', data['district'][index]).start()
            end: int = re.search('^川市', data['district'][index]).end()
            if start != 0:
                print('something wrong')  # for debug
            data['city'][index] = '市川市'
            data['district'][index] = data['district'][index][end:]

        elif data['district'][index] == '':
            # どこに残骸があるか不明なので
            if data['city'][index] == '市' and re.search('^川市', data['town'][index]):
                start: int = re.search('^川市', data['town'][index]).start()
                end: int = re.search('^川市', data['town'][index]).end()
                if start != 0:
                    print('something wrong')  # for debug
                data['city'][index] = '市川市'
                data['town'][index] = data['town'][index][end:]
    # 市原市
    for index in range(len(data['city'])):
        if data['city'][index] == '市' and re.search('^原市', data['district'][index]):
            start: int = re.search('^原市', data['district'][index]).start()
            end: int = re.search('^原市', data['district'][index]).end()
            if start != 0:
                print('something wrong')  # for debug
            data['city'][index] = '市原市'
            data['district'][index] = data['district'][index][end:]

        elif data['district'][index] == '':
            # どこに残骸があるか不明なので
            if data['city'][index] == '市' and re.search('^原市', data['town'][index]):
                start: int = re.search('^原市', data['town'][index]).start()
                end: int = re.search('^原市', data['town'][index]).end()
                if start != 0:
                    print('something wrong')  # for debug
                data['city'][index] = '市原市'
                data['town'][index] = data['town'][index][end:]
    # 野々市市
    for index in range(len(data['city'])):
        if data['city'][index] == '野々市' and re.search('^市', data['district'][index]):
            start: int = re.search('^市', data['district'][index]).start()
            end: int = re.search('^市', data['district'][index]).end()
            if start != 0:
                print('something wrong')  # for debug
            data['city'][index] = '野々市市'
            data['district'][index] = data['district'][index][end:]

        elif data['district'][index] == '':
            # どこに残骸があるか不明なので
            if data['city'][index] == '野々市' and re.search('^市', data['town'][index]):
                start: int = re.search('^市', data['town'][index]).start()
                end: int = re.search('^市', data['town'][index]).end()
                if start != 0:
                    print('something wrong')  # for debug
                data['city'][index] = '野々市市'
                data['town'][index] = data['town'][index][end:]
    # 四日市市
    for index in range(len(data['city'])):
        if data['city'][index] == '四日市' and re.search('^市', data['district'][index]):
            start: int = re.search('^市', data['district'][index]).start()
            end: int = re.search('^市', data['district'][index]).end()
            if start != 0:
                print('something wrong')  # for debug
            data['city'][index] = '四日市市'
            data['district'][index] = data['district'][index][end:]

        elif data['district'][index] == '':
            # どこに残骸があるか不明なので
            if data['city'][index] == '四日市' and re.search('^市', data['town'][index]):
                start: int = re.search('^市', data['town'][index]).start()
                end: int = re.search('^市', data['town'][index]).end()
                if start != 0:
                    print('something wrong')  # for debug
                data['city'][index] = '四日市市'
                data['town'][index] = data['town'][index][end:]
    # 廿日市市
    for index in range(len(data['city'])):
        if data['city'][index] == '廿日市' and re.search('^市', data['district'][index]):
            start: int = re.search('^市', data['district'][index]).start()
            end: int = re.search('^市', data['district'][index]).end()
            if start != 0:
                print('something wrong')  # for debug
            data['city'][index] = '廿日市市'
            data['district'][index] = data['district'][index][end:]

        elif data['district'][index] == '':
            # どこに残骸があるか不明なので
            if data['city'][index] == '廿日市' and re.search('^市', data['town'][index]):
                start: int = re.search('^市', data['town'][index]).start()
                end: int = re.search('^市', data['town'][index]).end()
                if start != 0:
                    print('something wrong')  # for debug
                data['city'][index] = '廿日市市'
                data['town'][index] = data['town'][index][end:]
    # 余市軍
    for index in range(len(data['city'])):
        if data['city'][index] == '余市' and re.search('^郡', data['district'][index]):
            start: int = re.search('^郡', data['district'][index]).start()
            end: int = re.search('^郡', data['district'][index]).end()
            if start != 0:
                print('something wrong')  # for debug
            data['city'][index] = '余市郡'
            data['district'][index] = data['district'][index][end:]

        elif data['district'][index] == '':
            # どこに残骸があるか不明なので
            if data['city'][index] == '余市' and re.search('^郡', data['town'][index]):
                start: int = re.search('^郡', data['town'][index]).start()
                end: int = re.search('^郡', data['town'][index]).end()
                if start != 0:
                    print('something wrong')  # for debug
                data['city'][index] = '余市郡'
                data['town'][index] = data['town'][index][end:]
        elif re.search('^[- 0-9 町 市]', data['district'][index]) is None:
            # どこに残骸があるか不明なので
            if data['city'][index] == '余市' and re.search('^郡', data['town'][index]):
                start: int = re.search('^郡', data['town'][index]).start()
                end: int = re.search('^郡', data['town'][index]).end()
                if start != 0:
                    print('something wrong')  # for debug
                data['city'][index] = '余市郡'
                data['town'][index] = data['town'][index][end:]
                if data['town'][index] == '' and re.search('[町]$', data['district'][index]):
                    # 文字列の分解位置をずらす
                    data['town'][index] = data['district'][index]
                    data['district'][index] = ''
    # 市貝町
    for index in range(len(data['city'])):
        if re.search('-市$', data['city'][index]):
            start: int = re.search('-市$', data['city'][index]).start()
            end: int = re.search('-市$', data['city'][index]).end()
            if data['town'][index] == '貝町':
                data['town'][index] = '市貝町'
                data['city'][index] = data['city'][index][:start]
    # 市川三郷町
    for index in range(len(data['city'])):
        if re.search('-市$', data['city'][index]):
            start: int = re.search('-市$', data['city'][index]).start()
            end: int = re.search('-市$', data['city'][index]).end()
            if data['town'][index] == '川3郷町':
                data['town'][index] = '市川三郷町'
                data['city'][index] = data['city'][index][:start]
            elif data['town'][index] == '川三郷町':
                data['town'][index] = '市川三郷町'
                data['city'][index] = data['city'][index][:start]
    # 市ケ坂町
    for index in range(len(data['city'])):
        if data['city'][index] == '市' and data['town'][index] == 'ケ坂町':
            data['city'][index] = '市ケ坂町'
            data['town'][index] = ''
