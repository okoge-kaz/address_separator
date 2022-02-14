import os

import pandas as pd


def main():
    """data/zenkoku.csvから町域チェック機能に必要な情報を取得後、取得したデータを参照しやすい形に整形し、dict(辞書）型として返す。"""
    Current_Path = os.getcwd()
    csv_data = pd.read_csv(Current_Path + "/data/zenkoku.csv")
    csv_data = csv_data.fillna("")
    data: dict = {}
    city_name: list = list(csv_data["市区町村"])
    temporaly_list: list = []
    # 市区町村名が変化したら追加
    last_city_name = ""
    for index in range(len(city_name)):
        if csv_data["市区町村"][index] != last_city_name:
            if last_city_name == "":
                # 最初の一つ目
                last_city_name = csv_data["市区町村"][index]
                temporaly_list.append(csv_data["町域"][index])
            else:
                data[last_city_name] = temporaly_list
                last_city_name = csv_data["市区町村"][index]
                temporaly_list = []  # 新たにつくる
                temporaly_list.append(csv_data["町域"][index])
        else:
            temporaly_list.append(csv_data["町域"][index])
    data[last_city_name] = temporaly_list
    return data
