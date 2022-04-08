import pandas as pd
import os
from utils.dataclass.ConvertDataclassForOutputToDict import outputclass_to_dict
from dataclasses import asdict
from typing import List

def create_output_data(AddressDataForOutput, Relative_PATH: str = "/output/output.csv") -> None:
    """
    args: DataclassForOutput
    return: void
    """

    #DataclassForOutputを辞書型に変換
    formated_dictionary_data = outputclass_to_dict(AddressDataForOutput)
    Current_PATH = os.getcwd()
    PATH = Current_PATH + Relative_PATH
    output_data = pd.DataFrame(formated_dictionary_data)
    output_data.to_csv(PATH, encoding="utf-8_sig")
