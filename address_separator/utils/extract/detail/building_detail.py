import re


def extract_building_detail(data: dict, manipulated_others_tail):
    # special_chractersのなかの F のみ抽出
    building_detail_info: list = []

    for i in range(len(manipulated_others_tail)):
        building_detail_info.append("")

    def search_x(x: str, subject):
        """ """

        def cutting_number_from_last(index: int):
            if re.search("-([0-9]+)$", data["house_number"][index]) is None:
                print(
                    "something wrong1()"
                )  # for debug(1-7-16のような住所が記載されている前提であり、荒川 207号のように住所(○-○-○)がなく、号がある場合も引っかかる)
            else:

                start: int = 0
                end: int = 0

                regular_expression_start = re.search("-([0-9]+)$", data["house_number"][index])
                if regular_expression_start is not None:
                    start = regular_expression_start.start()

                regular_expression_end = re.search("-([0-9]+)$", data["house_number"][index])
                if regular_expression_end is not None:
                    end = regular_expression_end.end()

                if end != len(data["house_number"][index]):
                    print("index which driven by regular expression is something wrong.")  # for debug
                # start+1 にしているのは-{数字}Fとなっているので - を除いている
                building_detail_info[index] = data["house_number"][index][start + 1 : end] + x
                data["house_number"][index] = data["house_number"][index][:start]

        for i in range(len(subject)):
            if subject[i] == x:
                # 空白に変える
                subject[i] = ""
                # special_charactersから数字をfetch
                cutting_number_from_last(i)
            else:
                pass  # building_detail_info.append("")

    search_x("F", data["special_characters"])
    search_x("階", manipulated_others_tail)
    search_x("号", manipulated_others_tail)

    return building_detail_info
