import os
import re

import pandas as pd
from utils.dataclass.HomemadeClass import make_DataclassForOutput


def shape(AddressDataForFormatting):
    """
    args: AddressDataForFormatting
    return: AddressDataForOutput

    出力するcsvファイルとして望ましい形に整形する
    """
    AddressDataForOutput = make_DataclassForOutput
    # 政令指定都市かどうかを判別するためのデータ
    Current_Path = os.getcwd()
    PATH = Current_Path + "/data/Ordinance_designated_city.csv"
    Ordinance_designated_city_csv = pd.read_csv(PATH)
    # データをコピー
    AddressDataForOutput.original = AddressDataForFormatting.original
    AddressDataForOutput.prefecture = AddressDataForFormatting.prefecture
    # 最終出力結果に合わせて整形 市区町村郡
    address1: list = []
    for index in range(len(AddressDataForFormatting.city)):
        if AddressDataForFormatting.city[index] in list(Ordinance_designated_city_csv):
            # 政令指定都市ならば
            address1.append(AddressDataForFormatting.city[index] + AddressDataForFormatting.town[index])
            AddressDataForFormatting.town[index] = ""
        elif re.search("郡$", AddressDataForFormatting.city[index]):
            # 郡ならば
            address1.append(AddressDataForFormatting.city[index] + AddressDataForFormatting.town[index])
            AddressDataForFormatting.town[index] = ""
        else:
            address1.append(AddressDataForFormatting.city[index])
    AddressDataForOutput.address1 = address1
    # 町域について
    address2: list = []
    for index in range(len(AddressDataForFormatting.town)):
        if re.search("[0-9 -]", AddressDataForFormatting.town[index]) or re.search(
            "[0-9 -]", AddressDataForFormatting.district[index]
        ):
            # 不正な文字が存在する caution
            address2.append(AddressDataForFormatting.town[index] + AddressDataForFormatting.district[index])
        else:
            address2.append(AddressDataForFormatting.town[index] + AddressDataForFormatting.district[index])
    AddressDataForOutput.address2 = address2
    # 番地について
    address3: list = []
    for index in range(len(AddressDataForFormatting.house_number)):
        if re.search("(([0-9]+)-)* [0-9]+", AddressDataForFormatting.house_number[index]):
            address3.append(AddressDataForFormatting.house_number[index])
        else:
            # 不正な文字が存在 caution
            address3.append(AddressDataForFormatting.house_number[index])
    AddressDataForOutput.address3 = address3
    # 建物名
    address4: list = []
    for index in range(len(AddressDataForFormatting.building_info)):
        if AddressDataForFormatting.special_characters[index]:
            # special_charactersのセルが空ではない caution
            address4.append(
                AddressDataForFormatting.special_characters[index] + AddressDataForFormatting.building_info[index]
            )
        else:
            # special_charactersが空
            address4.append(AddressDataForFormatting.building_info[index])
    AddressDataForOutput.address4 = address4
    # 部屋番号
    address5: list = []
    for index in range(len(AddressDataForFormatting.building_detail_info)):
        address5.append(AddressDataForFormatting.building_detail_info[index])
    AddressDataForOutput.address5 = address5
    # caution
    AddressDataForOutput.error1 = AddressDataForFormatting.error1
    AddressDataForOutput.error2 = AddressDataForFormatting.error2
    AddressDataForOutput.caution = AddressDataForFormatting.caution
    # address4について
    for index in range(len(AddressDataForOutput.address4)):
        if re.search("[0-9]+$", AddressDataForOutput.address4[index]):
            match = re.search("[0-9]+$", AddressDataForOutput.address4[index])
            assert match is not None
            start: int = match.start()
            end: int = match.end()
            if AddressDataForOutput.address5[index] == "":
                AddressDataForOutput.address5[index] = AddressDataForOutput.address4[index][start:end]
                AddressDataForOutput.address4[index] = AddressDataForOutput.address4[index][:start]
            else:
                AddressDataForOutput.caution[index] += "CAUTION: address4に何らかの問題がある可能性があります。  "
    # address 4の - ハイフン除去
    for index in range(len(AddressDataForOutput.address4)):
        if AddressDataForOutput.address4[index] == "":
            continue
        if AddressDataForOutput.address4[index][0] == "-":
            AddressDataForOutput.address4[index] = AddressDataForOutput.address4[index][1:]
        if AddressDataForOutput.address4[index][-1] == "-":
            if re.search("[ア-ン]$", AddressDataForOutput.address4[index][:-1]) is None:
                AddressDataForOutput.address4[index] = AddressDataForOutput.address4[index][:-1]
            else:
                # タワーなどのカタカナが入った名詞かもしれないので
                AddressDataForOutput.address4[index] = AddressDataForOutput.address4[index][:-1] + "ー"
    # address4の表記修正
    for index in range(len(AddressDataForOutput.address4)):
        # タワー,センターなどの表記が破壊されてしまっている場合は修正する
        if AddressDataForOutput.address4[index] == "":
            continue
        if re.search("センタ$", AddressDataForOutput.address4[index]):
            match = re.search("センタ$", AddressDataForOutput.address4[index])
            assert match is not None
            start: int = match.start()
            AddressDataForOutput.address4[index] = AddressDataForOutput.address4[index][:start] + "センター"
        if re.search("タワ$", AddressDataForOutput.address4[index]):
            match = re.search("タワ$", AddressDataForOutput.address4[index])
            assert match is not None
            start: int = match.start()
            AddressDataForOutput.address4[index] = AddressDataForOutput.address4[index][:start] + "タワー"
        if re.search("^ー*$", AddressDataForOutput.address4[index]):
            # 空白が-に置換されたことで生じるーを消去
            AddressDataForOutput.address4[index] = ""
    # invalid について
    for index in range(len(AddressDataForFormatting.invalid)):
        if AddressDataForFormatting.invalid[index] != "":
            AddressDataForOutput.error1[index] += "ERROR: データは、整形不可能な状態です。自動整形システムは正しく動作しません。この行の全ての結果を確認することを推奨します。  "
    # address3がなく、address4がある場合 caution
    for index in range(len(AddressDataForOutput.address4)):
        if AddressDataForOutput.address3[index] == "" and AddressDataForOutput.address4[index] != "":
            AddressDataForOutput.caution[index] += "CAUTION: address4の情報は本来あるべきではない場所にある可能性があります。  "
    # address4 or address5 に ? があったら caution
    for index in range(len(AddressDataForOutput.address4)):
        if "?" in AddressDataForOutput.address4[index]:
            AddressDataForOutput.caution[index] += "CAUTION: データには?が含まれており、文字コードに関わる何かしらの表示揺れがある可能性があります。  "
        elif "?" in AddressDataForOutput.address5[index]:
            AddressDataForOutput.caution[index] += "CAUTION: データには?が含まれており、文字コードに関わる何かしらの表示揺れがある可能性があります。  "
    # address4 が空かつ address5も空でかつ、 address3に-が3つあり、かつ最後の数字が302のような形であったらそれをaddress5に移す
    for index in range(len(AddressDataForOutput.address4)):
        if AddressDataForOutput.address4[index] == "" and AddressDataForOutput.address5[index] == "":
            if re.search("([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)", AddressDataForOutput.address3[index]):
                if re.search("([0-9]+)-([0-9]+)-([0-9]+)-([0-9]{3,})", AddressDataForOutput.address3[index]):
                    match = re.search("-[0-9]+$", AddressDataForOutput.address3[index])
                    assert match is not None
                    start: int = match.start()
                    # 3-5-4-809 の809の部分をaddress5に移行する
                    AddressDataForOutput.address5[index] = AddressDataForOutput.address3[index][start + 1 :]
                    AddressDataForOutput.address3[index] = AddressDataForOutput.address3[index][:start]
                else:
                    AddressDataForOutput.caution[index] += "CAUTION: 番地の中に、部屋番号が含まれている可能性があります。 "
            elif re.search("([0-9]+)-([0-9]+)-([1-9][0-1][0-9])", AddressDataForOutput.address3[index]):
                # 3-8-902 のような場合にcautionを出す
                AddressDataForOutput.caution[index] += "CAUTION: 番地の中に、部屋番号が含まれている可能性があります。 "
            elif re.search("([0-9]+)-([0-9]+)-([1-9][0-9][0-1][0-9])", AddressDataForOutput.address3[index]):
                # 3-8-902 のような場合にcautionを出す
                AddressDataForOutput.caution[index] += "CAUTION: 番地の中に、部屋番号が含まれている可能性があります。"
    # 一宮, 三谷などの町域が不正に分割された場合にERROR
    for index in range(len(AddressDataForOutput.address3)):
        if re.search("^[0-9]$", AddressDataForOutput.address3[index]):
            # address3が数字一つ
            if len(AddressDataForOutput.address4[index]) == 1 and AddressDataForOutput.address5[index] != "":
                AddressDataForOutput.error2[index] += "ERROR: 町域が不正に分割されている恐れがあります。 "
            else:
                AddressDataForOutput.caution[index] = "CAUTION: 町域名に含まれる漢数字が不正に分割されている恐れがあります。 "
    # address5に1-6-10などのものがあったらerror
    for index in range(len(AddressDataForOutput.address5)):
        if re.search("([0-9]+)+", AddressDataForOutput.address5[index]):
            AddressDataForOutput.error2[index] += "ERROR: address5の建物情報の箇所に番地と思しき情報が存在します"
    # アルファベット + ーについては消去
    for index in range(len(AddressDataForOutput.address4)):
        if re.search("[A-Z]+ー$", AddressDataForOutput.address4[index]):
            AddressDataForOutput.address4[index] = AddressDataForOutput.address4[index][:-1]
    # 返値
    return AddressDataForOutput
