import re


def extract_building_detail(data: dict):
    # special_chractersのなかの F のみ抽出
    building_detail_info: list = []

    def find_F(string: str):
        '''special_charactersに存在するFという文字単体を検知する'''
        if string == 'F':
            return True
        else:
            return False

    def cutting_number_from_last(index: int):
        '''上記の関数と同時に使用する。8Fのように、建物の階数情報のみを抽出する'''
        start: int = re.search(
            '-([0-9]+)$', data['house_number'][index]).start()
        end: int = re.search(
            '-([0-9]+)$', data['house_number'][index]).end()
        if end != len(data['house_number'][index]):
            print('somethin wrong2')  # for debug
        # start+1 にしているのは-{数字}Fとなっているので - を除いている
        building_detail_info.append(
            data['house_number'][index][start + 1:end] + 'F')
        data['house_number'][index] = data['house_number'][index][:start]

    for i in range(len(data['special_characters'])):
        if(find_F(data['special_characters'][i])):
            # 空白に変える
            data['special_characters'][i] = ""
            # special_charactersから数字をfetch
            cutting_number_from_last(i)
        else:
            building_detail_info.append('')
    return building_detail_info
