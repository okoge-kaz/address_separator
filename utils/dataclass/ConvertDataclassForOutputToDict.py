def outputclass_to_dict(AddressDataForOutput) -> dict:
    """
    args: AddressDataForOutput
    return: formated_dictionary_data: dict
    AddressDataForOutputを辞書型に変更
    """
    
    size = len(AddressDataForOutput.original)
    formated_dictionary_data: dict = {
        "original" : [], "prefecture" : [], "address1" : [], "address2" : [], "address3" : [],
        "address4" : [], "address5" : [], "error1" : [], "error2" : [], "caution" : []
    }

    for i in range(size):
        formated_dictionary_data["original"].append(AddressDataForOutput.original[i])
        formated_dictionary_data["prefecture"].append(AddressDataForOutput.prefecture[i])
        formated_dictionary_data["address1"].append(AddressDataForOutput.address1[i])
        formated_dictionary_data["address2"].append(AddressDataForOutput.address2[i])
        formated_dictionary_data["address3"].append(AddressDataForOutput.address3[i])
        formated_dictionary_data["address4"].append(AddressDataForOutput.address4[i])
        formated_dictionary_data["address5"].append(AddressDataForOutput.address5[i])
        formated_dictionary_data["error1"].append(AddressDataForOutput.error1[i])
        formated_dictionary_data["error2"].append(AddressDataForOutput.error2[i])
        formated_dictionary_data["caution"].append(AddressDataForOutput.caution[i])

    return formated_dictionary_data