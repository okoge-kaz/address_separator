import time

import utils.extract.detail.check.detail_data_check
import utils.shape.output_data_shaping
from utils.modify.operation import post_process
from utils.os.input import get_input_csv_data
from utils.os.output import create_output_data
from utils.preprocess.operation import pretreatment
from utils.split.splitByAddressField import split_by_address_field


def main():

    CSV_DATA = get_input_csv_data()

    formatted_address_data_array: list[str] = pretreatment(CSV_DATA)

    splitedAddressDataDictionarys = split_by_address_field(formatted_address_data_array, CSV_DATA)

    # 出力形式用にデータを再整形
    splitedAddressDataDictionarys = utils.shape.output_data_shaping.shape(splitedAddressDataDictionarys)

    # 特殊な町域などの経験則的修正
    post_process(splitedAddressDataDictionarys)

    # 実在する町域かどうかのチェック + 出力形式チェック
    utils.extract.detail.check.detail_data_check.detail_check(splitedAddressDataDictionarys)

    create_output_data(splitedAddressDataDictionarys)


if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)
