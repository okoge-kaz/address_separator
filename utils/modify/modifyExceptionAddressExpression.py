def modify_exception_case_address2(AddressDataForOutput: dict[str, list[str]], target_index: int) -> None:
    """
    address2が不正な形になっている(具体的には、 - が混在している状態: 屋一-三八-二二-二0二-エステスクエア町)
    このような際に行われる再整形（際分割）処理後もなお、正しく整形されない例外的ケースに対応する処理
    """

    # 町 屋 1-38-22-202 となるケース
    if (
        AddressDataForOutput["address1"][target_index] == "町"
        and AddressDataForOutput["address2"][target_index] == "屋"
    ):
        AddressDataForOutput["address2"][target_index] = "町屋"
        AddressDataForOutput["address1"][target_index] = ""


def modify_exception_case_address1(AddressDataForOutput: dict[str, list[str]], target_index: int) -> None:
    """
    address1が不正な形になっている(具体的には、 - が混在している状態: 屋一-三八-二二-二0二-エステスクエア町)
    このような際に行われる再整形（際分割）処理後もなお、正しく整形されない例外的ケースに対応する処理
    """
    pass
