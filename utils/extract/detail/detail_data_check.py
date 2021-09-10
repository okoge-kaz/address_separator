import utils.data_create.shapping


def detail_check(data: dict):
    # 町域に関するテスト
    data_set = utils.data_create.shapping.main()
    for index in range(len(data['address1'])):
        address1_value = data['address1'][index]
        if address1_value == '':
            continue
        address2_value = data['address2'][index]
        try:
            if address2_value in data_set[address1_value]:
                pass
            else:
                data['caution'][index] += "ERROR: The address2's value doesn't match the data set. Please CHECK the Address2 column's cell. "
        except KeyError:
            data['caution'][index] += "ERROR: The address2's value doesn't match the address3's data. Please CHECK the Address2 AND Address3 column's cells.  Maybe, One of the column's data is something wrong. "
