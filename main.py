import os
import time

import pandas as pd

import utils.extract.city
import utils.extract.detail.building_detail
import utils.extract.detail.check.caution
import utils.extract.detail.check.check
import utils.extract.detail.check.data_check
import utils.extract.detail.check.detail_data_check
import utils.extract.detail.house_number
import utils.extract.detail.munipulate
import utils.extract.detail.shaping
import utils.extract.detail.shaping_building_info
import utils.extract.district
import utils.extract.prefecture
import utils.extract.town
import utils.revise
import utils.shape.detail_shape
import utils.shape.output_data_shaping
import utils.shaping


def input_data(PATH: str):
    csv_data = pd.read_csv(PATH)
    return csv_data


def shape(csv_data):
    """
    整形作業を行う。ここでは、出力形式とは異なり独自の形での分割となっている。
    分割の形は以下の通り
    original,prefecture,city,town,district,invalid,house_number,special_characters,building_detail_info,building_info,error1,error2,caution
    """
    replaced_address_data: list = []
    # addressという名前がついた列しかデータを収集しない
    for address_data in csv_data["address"]:
        replaced_address_data.append(utils.shaping.operation(address_data))
    utils.revise.revise_data(replaced_address_data)
    # 出力データのもととなるdata: dictを作成
    data: dict = {}
    # dataに整形後のデータを入れる
    data["original"] = csv_data["address"]
    prefectures: list = []
    non_prefecture_address_data: list = []
    for string in replaced_address_data:
        tuple_data: tuple = utils.extract.prefecture.extract_prefecture(string)
        prefectures.append(tuple_data[0])
        non_prefecture_address_data.append(tuple_data[1])
    # dataに都道府県、市町村、町域をいれる
    data["prefecture"] = prefectures
    city_data = utils.extract.city.extract_city(non_prefecture_address_data)
    data["city"] = city_data[0]
    non_city_address_data: list = city_data[1]
    town_data = utils.extract.town.extract_town(non_city_address_data)
    data["town"] = town_data[0]
    non_town_address_data: list = town_data[1]
    district_data = utils.extract.district.extract_district(non_town_address_data)
    data["district"] = district_data[0]
    others: list = district_data[1]
    # 番地をいれる
    house_number_data = utils.extract.detail.house_number.operation(others)
    others_head: list = house_number_data[0]
    house_numbers: list = house_number_data[1]
    others_tail: list = house_number_data[2]
    data["invalid"] = others_head
    data["house_number"] = house_numbers
    # check 不正なデータが存在しないかどうかを確認
    caution: list = utils.extract.detail.check.check.check(data)
    # データ整形＋分裂してしまったデータを統合整理
    munipulated_others_tail = utils.extract.detail.munipulate.munipulate(data, others_tail)
    # ビルや建物情報の詳細を取得
    data["building_detail_info"] = utils.extract.detail.building_detail.extract_building_detail(data)
    # ビル情報のうちデータ散逸しているものを適切に統合
    utils.extract.detail.shaping_building_info.shaping_and_extracting_building_info(data, munipulated_others_tail)
    # others_tail内のデータを整形
    utils.extract.detail.shaping.shaping(data)
    # caution
    utils.extract.detail.check.caution.caution(data, munipulated_others_tail, caution)
    return data


def main():
    # path
    CurrentPath = os.getcwd()
    PATH = CurrentPath + "/input/input.csv"
    csv_data = input_data(PATH)
    # operation
    data = shape(csv_data)
    # 出力形式用にデータを再整形
    data = utils.shape.output_data_shaping.shape(data)
    # 特殊な町域などの経験則的修正
    utils.shape.detail_shape.shape(data)
    # 実在する町域かどうかのチェック + 出力形式チェック
    utils.extract.detail.check.detail_data_check.detail_check(data)
    # dict -> dataFrame
    df = pd.DataFrame(data)
    # output
    df.to_csv(CurrentPath + "/output/output.csv", encoding="utf-8_sig")


if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)
