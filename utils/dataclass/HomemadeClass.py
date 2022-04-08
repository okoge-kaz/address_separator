from dataclasses import dataclass

def make_DataclassForFormatting():
    @dataclass
    class DataclassForFormatting():
        original: list[str]
        prefecture: list[str]
        city: list[str]
        town: list[str]
        district: list[str]
        invalid: list[str]
        house_number: list[str]
        special_characters: list[str]
        building_detail_info: list[str]
        building_info: list[str]
        error1: list[str]
        error2: list[str]
        caution: list[str]  

    x = DataclassForFormatting
    return x

def make_DataclassForOutput():
    @dataclass
    class DataclassForOutput():
        original: list[str]
        prefecture: list[str]
        address1: list[str]
        address2: list[str]
        address3: list[str]
        address4: list[str]
        address5: list[str]
        error1: list[str]
        error2: list[str]
        caution: list[str]  

    x = DataclassForOutput
    return x