import re


def shape(data: dict):
    # 一宮
    for index in range(len(data["address3"])):
        if data["address3"][index] == "1" and data["address4"][index] == "宮":
            if data["address2"][index] != "":
                data["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                data["address2"][index] = "一宮"
                data["address3"][index] = data["address5"][index]
                data["address4"][index] = ""
                data["address5"][index] = ""
    # 一宮徳谷
    for index in range(len(data["address3"])):
        if data["address3"][index] == "1" and data["address4"][index] == "宮徳谷":
            if data["address2"][index] != "":
                data["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                data["address2"][index] = "一宮徳谷"
                data["address3"][index] = data["address5"][index]
                data["address4"][index] = ""
                data["address5"][index] = ""
    # 五台山
    for index in range(len(data["address3"])):
        if data["address3"][index] == "5" and data["address4"][index] == "台山":
            if data["address2"][index] != "":
                data["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                data["address2"][index] = "五台山"
                data["address3"][index] = data["address5"][index]
                data["address4"][index] = ""
                data["address5"][index] = ""
    # 五台山〜
    for index in range(len(data["address3"])):
        if data["address3"][index] == "5" and re.search("^台山.+", data["address4"][index]):
            if data["address2"][index] != "":
                data["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                data["address2"][index] = ""
                data["address3"][index] = ""
                data["address4"][index] = "五" + data["address4"][index]
    # 三谷
    for index in range(len(data["address3"])):
        if data["address3"][index] == "3" and data["address4"][index] == "谷":
            if data["address2"][index] != "":
                data["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                data["address2"][index] = "三谷"
                data["address3"][index] = data["address5"][index]
                data["address4"][index] = ""
                data["address5"][index] = ""
    # 三原
    for index in range(len(data["address3"])):
        if data["address3"][index] == "3" and data["address4"][index] == "原":
            if data["address2"][index] != "":
                data["error1"][index] += "ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  "
            else:
                data["address2"][index] = "三原"
                data["address3"][index] = data["address5"][index]
                data["address4"][index] = ""
                data["address5"][index] = ""
    # 三重城
    for index in range(len(data["address4"])):
        if data["address3"][index] == "":
            continue
        if re.search("^重城", data["address4"][index]) and data["address3"][index][-1] == "3":
            if len(data["address3"][index]) < 2:
                continue
            data["address3"][index] = data["address3"][index][:-2]
            data["address4"][index] = "三" + data["address4"][index]
    # マンション名らしくないもの
    for index in range(len(data["address4"])):
        if re.search("^.[0-9]+.$", data["address4"][index]):
            data["caution"][index] += "CAUTION: address4の値が不適切な可能性があります。  "
    # address4が号のみのとき
    for index in range(len(data["address4"])):
        if data["address4"][index] == "号":
            data["address4"][index] = ""
            data["caution"][index] += "CAUTION: address4の'号'は意味をなさないと判断され、削除されました。  "
    # 番地らしきものがaddress4に紛れ込んでいないかどうか
    for index in range(len(data["address4"])):
        if re.search("[0-9]+ー", data["address4"][index]):
            data["caution"][index] += "CAUTION: address4に番地の残骸が含まれている場合があります。  "
    # address4に単独で 棟 とあったら
    for index in range(len(data["address4"])):
        if data["address3"][index] != "" and data["address4"][index] == "棟":
            if re.search("-[0-9]+$", data["address3"][index]):
                start: int = re.search("-[0-9]+$", data["address3"][index]).start()
                data["address5"][index] = data["address3"][index][start + 1 :] + "棟" + data["address5"][index]
                data["address3"][index] = data["address3"][index][:start]
                data["address4"][index] = ""
    # address4に単独で 号棟 とあったら
    for index in range(len(data["address4"])):
        if data["address3"][index] != "" and data["address4"][index] == "号棟":
            if re.search("-[0-9]+$", data["address3"][index]):
                start: int = re.search("-[0-9]+$", data["address3"][index]).start()
                data["address5"][index] = data["address3"][index][start + 1 :] + "号棟" + data["address5"][index]
                data["address3"][index] = data["address3"][index][:start]
                data["address4"][index] = ""
    # address4に単独で 号室 とあったら
    for index in range(len(data["address4"])):
        if data["address3"][index] != "" and data["address4"][index] == "号室":
            if re.search("-[0-9]+$", data["address3"][index]):
                start: int = re.search("-[0-9]+$", data["address3"][index]).start()
                data["address5"][index] = data["address3"][index][start + 1 :] + "号室" + data["address5"][index]
                data["address3"][index] = data["address3"][index][:start]
                data["address4"][index] = ""
    # address4に〜号室があるとき
    for index in range(len(data["address4"])):
        # 902号室のようなもの
        if re.search("^[0-9]+号室$", data["address4"][index]):
            if data["address5"] != "":
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
        # c号室のようなもの
        elif re.search("^[a-z]号室$", data["address4"][index]):
            if data["address5"] != "":
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
        # C号室のようなもの
        elif re.search("^[A-Z]号室$", data["address4"][index]):
            if data["address5"] != "":
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
    # address4の先頭のーを除去
    for index in range(len(data["address4"])):
        if data["address4"][index] == "ー":
            data["address4"][index] = data["address4"][index][1:]
    # address4に 号室だけがあるとき
    for index in range(len(data["address4"])):
        if data["address4"][index] == "号室":
            if re.search("-[0-9]+", data["address3"][index]):
                start: int = re.search("-[0-9]+", data["address3"][index]).start()
                if data["address5"] != "":
                    data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                    continue
                data["address5"][index] = data["address3"][index][start + 1 :] + "号室"
                data["address4"][index] = ""
                data["address3"][index] = data["address3"][index][:start]
    # address4にある()のようなデータのかっこをはずし、適切な位置へ
    for index in range(len(data["address4"])):
        if re.search("^\\(.+\\)$", data["address4"][index]):
            data["address4"][index] = data["address4"][index][1:-1]
        # 3桁以上の数字
        if re.search("^[0-9]{3,}$", data["address4"][index]):
            if data["address5"][index] != "":
                # address5が空ではない
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
        # 3F
        elif re.search("^[0-9]F$", data["address4"][index]):
            if data["address5"][index] != "":
                # address5が空ではない
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
        # 3階
        elif re.search("^[0-9]階$", data["address4"][index]):
            if data["address5"][index] != "":
                # address5が空ではない
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
        # c号室(半角)
        elif re.search("^[a-z]号室$", data["address4"][index]):
            if data["address5"][index] != "":
                # address5が空ではない
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
        # c号室（全角)
        elif re.search("^[a-z]号室$", data["address4"][index]):
            if data["address5"][index] != "":
                # address5が空ではない
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
        # 204号室
        elif re.search("^[0-9]+号室$", data["address4"][index]):
            if data["address5"][index] != "":
                # address5が空ではない
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
        # C号室(半角)
        elif re.search("^[A-Z]号室$", data["address4"][index]):
            if data["address5"][index] != "":
                # address5が空ではない
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
        # C号室(全角)
        elif re.search("^[A-Z]号室$", data["address4"][index]):
            if data["address5"][index] != "":
                # address5が空ではない
                data["caution"][index] += "CAUTION: address4のデータはaddress5にあるべきデータである可能性があります。 "
                continue
            data["address5"][index] = data["address4"][index]
            data["address4"][index] = ""
    # address4の先頭に の[数字]ー があったとき
    for index in range(len(data["address4"][index])):
        if re.search("^の[0-9]+ー", data["address4"][index]):
            end: int = re.search("^の[0-9]+ー", data["address4"][index]).end()
            data["address3"][index] += data["address4"][index][1 : end - 1]
            data["address4"][index] = data["address4"][index][end:]
    # address4に # が単独であったら
    for index in range(len(data["address4"])):
        if data["address4"][index] == "#":
            data["caution"][index] += "CAUTION: address4の'#'は意味をなさないかもしれません。  "
    # address4の先頭の ー を消去
    for index in range(len(data["address4"])):
        if data["address4"][index] == "":
            continue
        if data["address4"][index][0] == "ー" and len(data["address4"][index]) >= 1:
            data["address4"][index] = data["address4"][index][1:]
    # address2に-があったらerror
    for index in range(len(data["address2"])):
        if re.search("-", data["address2"][index]):
            data["error1"][index] += "ERROR: address2に存在する情報は秩序だっていません。整形エラーが発生している可能性が高いです。  "
    # address5に~号 とあるがaddress4が空で、かつaddress3に-が2未満なとき
    for index in range(len(data["address5"])):
        if re.search("^[0-9]+号$", data["address5"][index]) and data["address4"][index] == "":
            if re.search("^[0-9]+(-[0-9]+)*$", data["address3"][index]):
                # address3が正常かどうか
                if re.search("^[0-9]+(-[0-9]+){2,}$", data["address3"][index]):
                    # ハイフンが2回以上
                    continue
                else:
                    # 2回未満
                    # ~号というものをaddress3に追加する(号を消して)
                    data["address3"][index] += "-" + data["address5"][index][:-1]
                    data["address5"][index] = ""
            else:
                data["error1"][index] += "ERROR: address3のデータ形式が不正です。 "
    # ()をはずした後の処理 数字
    for index in range(len(data["address4"])):
        if re.search("[0-9]+(ー[0-9]+)*", data["address4"][index]):
            if data["address5"][index] != "":
                data["caution"][index] += "CAUTION: address4にはaddress5にあるべきデータが存在するやもしれません。  "
                continue
            data["address5"][index] = re.sub("ー", "-", data["address4"][index])
            data["address4"][index] = ""
    # 番地がないデータの処理
    for index in range(len(data["address4"])):
        if data["address4"][index] != "" and data["address3"][index] == "":
            # address4にある町域データと思しきものを移動
            if re.search("[a-z A-Z 0-9 - ?]", data["address4"][index]):
                # マンション名にありそうなものを除く
                continue
            if re.search(
                "地|事務所|会館|パーク|ハウス|ホーム|メール|コート|団地|ハイム|コーポ|メゾン|棟|グランド|株式会社|有限会社|（株）|ビル|北口店|南口店|西口店|東口店|組合|荘|建設|プラザ|パレス|サロン|レジデンス|レジデンシャル|ハイム|NPO|NGO|NPO|NGO|㈲|メゾン|ロイヤル|テーラー|亭",
                data["address4"][index],
            ):
                continue
            else:
                data["address2"][index] = data["address2"][index] + data["address4"][index]
                data["address4"][index] = ""
    # address2に - が入っているパターン
    for index in range(len(data["address2"])):
        if re.search("-", data["address2"][index]):
            data["caution"][index] += "CAUTION: 自動整形システムが推測によって分割している箇所があります。この行の分割が正しいか確認することを強く推奨します。 "
            # 西一-一八-一六-カモミ-ル西町 のようになっているはず
            mapping: dict = {
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
            japanese_numbers: list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "〇"]
            string: str = ""
            for id in range(len(data["address2"][index])):
                if data["address2"][index][id] in japanese_numbers:
                    string += mapping[data["address2"][index][id]]
                else:
                    string += data["address2"][index][id]
            # 分割作業
            if re.search("[0-9]+", string):
                # 数字がある
                address3_start: int = re.search("[0-9]+", string).start()
                address3_end: int = re.search("[0-9]+(-[0-9]+)*", string).end()
                # 数字で終わる
                if len(string) == re.search("[0-9]+(-[0-9]+)*", string).end():
                    if data["address3"][index] == "":
                        data["address2"][index] = string[:address3_start]
                        data["address3"][index] = string[address3_start:address3_end]
                    else:
                        data["address2"][index] = string[:address3_start]
                        data["address3"][index] = string[address3_start:address3_end] + data["address3"][index]
                else:
                    # 建物名らしきものが存在する
                    if data["address3"][index] == "":
                        # 番地情報が空
                        data["address2"][index] = string[:address3_start]
                        data["address3"][index] = string[address3_start:address3_end]
                        building_information_data: str = string[address3_end:]
                        if re.search("[0-9]", building_information_data):
                            # 建物名の情報に部屋番号が紛れ込んでいる
                            start_index: int = re.search("[0-9]", building_information_data).start()
                            data["address4"][index] = building_information_data[:start_index]
                            # 先頭の-を削除
                            if data["address4"][index] != "" and data["address4"][index][0] == "-":
                                if len(data["address4"][index]) >= 2:
                                    data["address4"][index] = data["address4"][index][1:]
                            # address4の-をーに変更
                            data["address4"][index] = re.sub("-", "ー", data["address4"][index])
                            # address5
                            data["aadress5"][index] = building_information_data[start_index:]
                        else:
                            # 建物情報のみ
                            data["address4"][index] = building_information_data
                            # 先頭の-を削除
                            if data["address4"][index] != "" and data["address4"][index][0] == "-":
                                if len(data["address4"][index]) >= 2:
                                    data["address4"][index] = data["address4"][index][1:]
                            # address4の-をーに変更
                            data["address4"][index] = re.sub("-", "ー", data["address4"][index])
                    else:
                        # 番地情報に数字がある
                        # 建物情報の可能性が高いのでaddress5に移す
                        data["address5"][index] = data["address3"][index]
                        data["address2"][index] = string[:address3_start]
                        data["address3"][index] = string[address3_start:address3_end]
                        data["address4"][index] = string[address3_end:]
                        # 先頭の-を削除
                        if data["address4"][index] != "" and data["address4"][index][0] == "-":
                            if len(data["address4"][index]) >= 2:
                                data["address4"][index] = data["address4"][index][1:]
                        # address4の-をーに変更
                        data["address4"][index] = re.sub("-", "ー", data["address4"][index])
            else:
                continue
    # address1に - が入っているパターン
    for index in range(len(data["address1"])):
        if re.search("-", data["address1"][index]):
            data["caution"][index] += "CAUTION: 自動整形システムが推測によって分割している箇所があります。この行の分割が正しいか確認することを強く推奨します。 "
            # 羽若町四九三-一-市 のようになっているはず
            mapping: dict = {
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
            japanese_numbers: list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "〇"]
            string: str = ""
            for id in range(len(data["address1"][index])):
                if data["address1"][index][id] in japanese_numbers:
                    string += mapping[data["address1"][index][id]]
                else:
                    string += data["address1"][index][id]
            # 分割作業
            if re.search("[0-9]+", string):
                # 数字がある
                address3_start: int = re.search("[0-9]+", string).start()
                address3_end: int = re.search("[0-9]+(-[0-9]+)*", string).end()
                # 数字で終わる
                if len(string) == re.search("[0-9]+(-[0-9]+)*", string).end():
                    if data["address3"][index] == "":
                        data["address1"][index] = string[:address3_start]
                        data["address3"][index] = string[address3_start:address3_end]
                    else:
                        data["address1"][index] = string[:address3_start]
                        data["address3"][index] = string[address3_start:address3_end] + data["address3"][index]
                else:
                    # 建物名らしきものが存在する
                    if data["address3"][index] == "":
                        # 番地情報が空
                        data["address1"][index] = string[:address3_start]
                        data["address3"][index] = string[address3_start:address3_end]
                        building_information_data: str = string[address3_end:]
                        if re.search("[0-9]", building_information_data):
                            # 建物名の情報に部屋番号が紛れ込んでいる
                            start_index: int = re.search("[0-9]", building_information_data).start()
                            data["address4"][index] = building_information_data[:start_index]
                            # 先頭の-を削除
                            if data["address4"][index] != "" and data["address4"][index][0] == "-":
                                if len(data["address4"][index]) >= 2:
                                    data["address4"][index] = data["address4"][index][1:]
                            # address4の-をーに変更
                            data["address4"][index] = re.sub("-", "ー", data["address4"][index])
                            # address5
                            data["aadress5"][index] = building_information_data[start_index:]
                        else:
                            # 建物情報のみ
                            data["address4"][index] = building_information_data
                            # 先頭の-を削除
                            if data["address4"][index] != "" and data["address4"][index][0] == "-":
                                if len(data["address4"][index]) >= 2:
                                    data["address4"][index] = data["address4"][index][1:]
                            # address4の-をーに変更
                            data["address4"][index] = re.sub("-", "ー", data["address4"][index])
                    else:
                        # 番地情報に数字がある
                        # 建物情報の可能性が高いのでaddress5に移す
                        data["address5"][index] = data["address3"][index]
                        data["address1"][index] = string[:address3_start]
                        data["address3"][index] = string[address3_start:address3_end]
                        data["address4"][index] = string[address3_end:]
                        # 先頭の-を削除
                        if data["address4"][index] != "" and data["address4"][index][0] == "-":
                            if len(data["address4"][index]) >= 2:
                                data["address4"][index] = data["address4"][index][1:]
                        # address4の-をーに変更
                        data["address4"][index] = re.sub("-", "ー", data["address4"][index])
            else:
                continue
