import utils.data_create.shapping


def detail_check(data: dict):
    # 町域に関するテスト
    data_set = utils.data_create.shapping.main()
    for index in range(len(data['address1'])):
        address1_value = data['address1'][index]
        if address1_value == '':
            data['caution'][index] += "ERROR: The address1 column's data is empty.  "
            continue
        address2_value = data['address2'][index]
        try:
            if address2_value in data_set[address1_value]:
                pass
            else:
                data['caution'][index] += "ERROR: The address2's value doesn't match the data set. Please CHECK the address2 column's cell.  "
        except KeyError:
            data['caution'][index] += "ERROR: The address2's value doesn't match the address1's data. Please CHECK the address1 AND address2 column's cells.  Maybe, One of the column's data is something wrong.  "
    # 番地に関するテスト
    for index in range(len(data['address3'])):
        if data['address3'][index] == '':
            data['caution'][index] += "ERROR: The address3's column's data is empty.  "
