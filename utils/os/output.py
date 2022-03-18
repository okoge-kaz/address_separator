import pandas as pd
import os

def create_output_data(formated_dictionary_data: dict, Relative_PATH: str = "/output/output.csv") -> None:
    """
    args: formated_dictionary_data: dict
    return: void
    """
    Current_PATH = os.getcwd()
    PATH = Current_PATH + Relative_PATH
    output_data = pd.DataFrame(formated_dictionary_data)
    output_data.to_csv(PATH, encoding="utf-8_sig")
