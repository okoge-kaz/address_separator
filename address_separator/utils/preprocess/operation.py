import pandas as pd
import utils.preprocess.post.fix_special_name_address as post
import utils.preprocess.pre.process_japanese_address_expression as pre


def pretreatment(CSV_DATA: pd.DataFrame) -> list[str]:
    """
    pretreatment: 分割処理を行う前の前処理を行う。

    Parameters
    ----------
    CSV_DATA : pd.DataFrame
        入力データ(元データ: original data)

    Returns
    -------
    list[str]
        分割後のデータ
    """
    address_data_array: pd.Series = CSV_DATA["address"]

    formatted_address_data_array = list(map(pre.process_japanese_style_address_expression, address_data_array))
    post.reshape_exceptional_address_address_data_array(formatted_address_data_array)

    return formatted_address_data_array
