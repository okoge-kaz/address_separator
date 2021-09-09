import re


def munipulate(data: dict, others_tail: list):
    '''番地を取り除いた後のデータに関して、処理を行い後の操作で処理を行いやすくする。'''
    munipulated_others_tail: list = []

    for id in range(len(others_tail)):
        if re.match('[0-9]+$', others_tail[id]):
            print(others_tail[id])
            data['house_number'][id] = data['house_number'][id] + others_tail[id]
            munipulated_others_tail.append("")
        else:
            munipulated_others_tail.append(others_tail[id])

    def extract_number_and_alphabet1(string: str):
        if(string == ""):
            return None
        return re.match('^(-[A-Z 0-9]+)*([A-Z 0-9]+)*$', string)

    def extract_number_and_alphabet2(string: str):
        if(string == ""):
            return None
        return re.match('^([A-Z 0-9]+)*(-[A-Z 0-9]+)*$', string)

    special_characters: list = []
    for i in range(len(munipulated_others_tail)):
        if extract_number_and_alphabet1(munipulated_others_tail[i]):
            special_characters.append(munipulated_others_tail[i])
            munipulated_others_tail[i] = ""
        else:
            special_characters.append("")
        if extract_number_and_alphabet2(munipulated_others_tail[i]):
            special_characters[i] = (munipulated_others_tail[i])
            munipulated_others_tail[i] = ""
        else:
            pass

    data['special_characters'] = special_characters

    def extract_number_from_others_tail(string: str):
        if string == "":
            return None
        else:
            return re.match('^([0-9]+)', string)

    for i in range(len(munipulated_others_tail)):
        if extract_number_from_others_tail(munipulated_others_tail[i]):
            start: int = extract_number_from_others_tail(munipulated_others_tail[i]).start()
            end: int = extract_number_from_others_tail(munipulated_others_tail[i]).end()
            if start != 0:
                print('something wrong')  # for debug
            data['house_number'][i] = data['house_number'][i] + munipulated_others_tail[i][start:end]
            munipulated_others_tail[i] = munipulated_others_tail[i][end:]
        else:
            pass

    # others_tailの整形
    def eliminate_hypen(string: str):
        if string == "":
            return string
        else:
            if string[0] == "-":
                return string[1:]
            else:
                return string

    for i in range(len(munipulated_others_tail)):
        munipulated_others_tail[i] = eliminate_hypen(munipulated_others_tail[i])
    return munipulated_others_tail
