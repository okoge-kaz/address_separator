def modify_exception_case_address2(splitedAddressDataDictionarys: dict[str, list[str]], target_index: int):
    """
    address2が不正な形になっている(具体的には、 - が混在している状態: 屋一-三八-二二-二0二-エステスクエア町)
    このような際に行われる再整形（際分割）処理後もなお、正しく整形されない例外的ケースに対応する処理
    """

    # 町 屋 1-38-22-202 となるケース
    if (
        splitedAddressDataDictionarys["address1"][target_index] == "町"
        and splitedAddressDataDictionarys["address2"][target_index] == "屋"
    ):
        splitedAddressDataDictionarys["address2"][target_index] = "町屋"
        splitedAddressDataDictionarys["address1"][target_index] = ""


def modify_exception_case_address1(splitedAddressDataDictionarys: dict[str, list[str]], target_index: int):
    """
    address1が不正な形になっている(具体的には、 - が混在している状態: 屋一-三八-二二-二0二-エステスクエア町)
    このような際に行われる再整形（際分割）処理後もなお、正しく整形されない例外的ケースに対応する処理
    """
    pass