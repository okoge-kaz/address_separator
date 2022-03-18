import pandas as pd
import utils.preprocess.post.fixSpecialNameAddress as post
import utils.preprocess.pre.processJapaneseAddressExpression as pre


def pretreatment(CSV_DATA: pd.DataFrame) -> list[str]:
    """
    分割処理を行う前の前処理を行う。
    """
    address_data_array = CSV_DATA["address"]

    formatted_address_data_array = list(map(pre.process_japanese_style_address_expression, address_data_array))
    post.reshape_exceptional_address_address_data_array(formatted_address_data_array)

    return formatted_address_data_array
