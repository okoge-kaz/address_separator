import re


def shape(data: dict):
    # 一宮
    for index in range(len(data['address3'])):
        if data['address3'][index] == '1' and data['address4'][index] == '宮':
            if data['address2'][index] != '':
                data['error1'][index] += 'ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  '
            else:
                data['address2'][index] = '一宮'
                data['address3'][index] = data['address5'][index]
                data['address4'][index] = ''
                data['address5'][index] = ''
    # 一宮徳谷
    for index in range(len(data['address3'])):
        if data['address3'][index] == '1' and data['address4'][index] == '宮徳谷':
            if data['address2'][index] != '':
                data['error1'][index] += 'ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  '
            else:
                data['address2'][index] = '一宮徳谷'
                data['address3'][index] = data['address5'][index]
                data['address4'][index] = ''
                data['address5'][index] = ''
    # 五台山
    for index in range(len(data['address3'])):
        if data['address3'][index] == '5' and data['address4'][index] == '台山':
            if data['address2'][index] != '':
                data['error1'][index] += 'ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  '
            else:
                data['address2'][index] = '五台山'
                data['address3'][index] = data['address5'][index]
                data['address4'][index] = ''
                data['address5'][index] = ''
    # 五台山〜
    for index in range(len(data['address3'])):
        if data['address3'][index] == '5' and re.search('^台山.+', data['address4'][index]):
            if data['address2'][index] != '':
                data['error1'][index] += 'ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  '
            else:
                data['address2'][index] = ''
                data['address3'][index] = ''
                data['address4'][index] = '五' + data['address4'][index]
    # 三谷
    for index in range(len(data['address3'])):
        if data['address3'][index] == '3' and data['address4'][index] == '谷':
            if data['address2'][index] != '':
                data['error1'][index] += 'ERROR: 町域と判断される文字列が２つあります。自動整形システムは正しく動作しません。  '
            else:
                data['address2'][index] = '三谷'
                data['address3'][index] = data['address5'][index]
                data['address4'][index] = ''
                data['address5'][index] = ''