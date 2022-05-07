from __future__ import annotations

import re


def operation(others: list):
    """1-7-6 のような番地を抽出する。"""
    house_numbers: list = []
    others_head: list = []
    others_tail: list = []

    def extract_house_number(string: str):
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
