import pandas as pd


def main():
    '''main.py実行時に実行される関数ではなく、main関数の処理を実行する際に参照するデータ作成用の関数'''
    csv_data = pd.read_csv('../../data/zenkoku.csv')
    print(csv_data)
    data: dict = {}
    city_name_data = csv_data['市区町村']
    print(city_name_data)
    detail_data = csv_data['町域']
    print(detail_data)
    for index in range(len(city_name_data)):
        data[city_name_data['市区町村'][index]] = detail_data['町域'][index]
    df = pd.DataFrame(data)
    df.to_csv('../../data/data_set.csv', encoding='utf-8_sig')


if __name__ == '__main__':
    main()
