import utils.data_create.shapping


def detail_check(data: dict[str, list[str]]):
    # 町域に関するテスト
    data_set = utils.data_create.shapping.main()
    for index in range(len(data["address1"])):
        address1_value = data["address1"][index]
        if address1_value == "":
            data["error2"][index] += "ERROR: address1の列の情報がありません。市区町村以降の自動チェック機構はこの行には働きません。  "
            continue
        address2_value = data["address2"][index]
        try:
            if address2_value in data_set[address1_value]:
                pass
            else:
                data["error1"][index] += "ERROR: address2のデータは、自動チェック機構が参照する日本郵便のデータセットに合致しません。  "
        except KeyError:
            data["error1"][
                index
            ] += "ERROR: address2のデータは、address1のデータから推測されるデータに一致しません。（自動チェック機構が参照するデータセットに合致しないか、表記が異なります。  "
    # 番地に関するテスト
    for index in range(len(data["address3"])):
        if data["address3"][index] == "":
            data["error2"][index] += "ERROR: address3の列の情報がありません。  "
