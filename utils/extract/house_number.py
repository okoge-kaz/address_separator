import re


def extract_house_number(others: list):
    """
    args: others: list
    return: (others_head: list, house_numbers: list, others_tail: list)
    1-7-6 のような番地を抽出する。
    """
    house_numbers: list = []
    others_head: list = []
    others_tail: list = []

    def extract_house_number(string: str) -> None:
        """
        args: string: str
        return: void
        """
        index = re.search("(([0-9]+)-)+([0-9]+)", string)
        if index is None:
            house_numbers.append("")
            others_head.append("")
            others_tail.append(string)
        else:
            house_numbers.append(string[index.start() : index.end()])
            others_head.append(string[0 : index.start()])
            others_tail.append(string[index.end() :])

    for other in others:
        extract_house_number(other)
    return (others_head, house_numbers, others_tail)
