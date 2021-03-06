import re
from typing import Union

import utils.data_create.shapping


def detail_check(splitted_address_data_dictionaries: dict[str, list[str]]):
    # 町域に関するテスト
    splitted_address_data_dictionaries_set = utils.data_create.shapping.main()
    for index in range(len(splitted_address_data_dictionaries["address1"])):
        address1_value = splitted_address_data_dictionaries["address1"][index]
        if address1_value == "":
            splitted_address_data_dictionaries["error2"][
                index
            ] += "ERROR: address1の列の情報がありません。市区町村以降の自動チェック機構はこの行には働きません。  "
            continue
        address2_value = splitted_address_data_dictionaries["address2"][index]
        try:
            if address2_value in splitted_address_data_dictionaries_set[address1_value]:
                pass
            else:
                # イロハなどの特殊な番地名の場合 address2 に値が混入している場合がある
                is_unexpected_address2_value: Union[re.Match[str], None] = re.search("(イ|ロ|ハ)+$", address2_value)
                if is_unexpected_address2_value is not None:
                    split_index: int = is_unexpected_address2_value.start()

                    unexpected_address3_value_in_address2: str = address2_value[split_index:]
                    address2_value = address2_value[0:split_index]

                    # データを更新
                    splitted_address_data_dictionaries["address2"][index] = address2_value
                    if splitted_address_data_dictionaries["address3"][index] == "":
                        # address3 が空の場合は - の追加は必要ない
                        splitted_address_data_dictionaries["address3"][index] = unexpected_address3_value_in_address2
                    else:
                        splitted_address_data_dictionaries["address3"][index] = (
                            unexpected_address3_value_in_address2
                            + "-"
                            + splitted_address_data_dictionaries["address3"][index]
                        )

                splitted_address_data_dictionaries["error1"][
                    index
                ] += "ERROR: address2のデータは、自動チェック機構が参照する日本郵便のデータセットに合致しません。  "
        except KeyError:
            splitted_address_data_dictionaries["error1"][
                index
            ] += "ERROR: address2のデータは、address1のデータから推測されるデータに一致しません。（自動チェック機構が参照するデータセットに合致しないか、表記が異なります。  "
    # 番地に関するテスト
    for index in range(len(splitted_address_data_dictionaries["address3"])):
        if splitted_address_data_dictionaries["address3"][index] == "":
            splitted_address_data_dictionaries["error2"][index] += "ERROR: address3の列の情報がありません。  "
