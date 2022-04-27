class AddressData:
    """ """

    def __init__(
        self,
        original_address_data: str,
        prefecture: str,
        city: str,
        town: str,
        district: str,
        house_number: str,
        special_characters: str,
        building_info: str,
        building_detail_info: str,
        error1: str,
        error2: str,
        caution: str,
    ) -> None:
        self.original: str = original_address_data
        self.prefecture: str = prefecture
        self.city: str = city
        self.town: str = town
        self.district: str = district
        self.house_number: str = house_number
        self.special_characters: str = special_characters
        self.building_info: str = building_info
        self.building_detail_info: str = building_detail_info
        self.error1: str = error1
        self.error2: str = error2
        self.caution: str = caution

    def __dict__(self) -> dict[str, str]:
        return {
            "original": self.original,
            "prefecture": self.prefecture,
            "city": self.city,
            "town": self.town,
            "district": self.district,
            "house_number": self.house_number,
            "special_characters": self.special_characters,
            "building_info": self.building_info,
            "building_detail_info": self.building_detail_info,
            "error1": self.error1,
            "error2": self.error2,
            "caution": self.caution,
        }


class formattedAddressData:
    """_summary_"""

    def __init__(
        self,
        original: str,
        prefecture: str,
        address1: str,
        address2: str,
        address3: str,
        address4: str,
        address5: str,
        error1: str,
        error2: str,
        caution: str,
    ) -> None:
        self.original: str = original
        self.prefecture: str = prefecture
        self.address1: str = address1
        self.address2: str = address2
        self.address3: str = address3
        self.address4: str = address4
        self.address5: str = address5
        self.error1: str = error1
        self.error2: str = error2
        self.caution: str = caution

    def __dict__(self):
        return {
            "original": self.original,
            "prefecture": self.prefecture,
            "address1": self.address1,
            "address2": self.address2,
            "address3": self.address3,
            "address4": self.address4,
            "address5": self.address5,
            "error1": self.error1,
            "error2": self.error2,
            "caution": self.caution,
        }
