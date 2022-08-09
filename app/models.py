import re
from dataclasses import dataclass

from app.consts import IBAN_CHAR_TO_NUM, IBAN_FORMATS_PER_COUNTRY
from app.utils import trim


@dataclass
class IbanModel:
    def __init__(self, iban) -> None:
        self.iban = trim(iban)

    @property
    def country_code(self) -> str:
        return self.iban[:2].upper()

    @property
    def header(self) -> str:
        return self.iban[:4]

    @property
    def bban(self) -> str:
        return self.iban[4:]

    @property
    def country_specific_format(self) -> dict:
        return IBAN_FORMATS_PER_COUNTRY[self.country_code.upper()]

    @property
    def country(self) -> str:
        return self.country_specific_format["country"]

    @property
    def country_specific_iban_size(self) -> int:
        return int(self.country_specific_format["size"])

    @property
    def bban_format(self) -> str:
        return self.country_specific_format["bban_format"]

    @property
    def bban_format_to_regex(self):
        bban_format_list = self.bban_format.split("-")
        for bban_format in bban_format_list:
            type_ = bban_format[-1]
            size = bban_format[:-1]
            if type_ == "a":
                yield f"[A-Z]{{{size}}}"
            elif type_ == "c":
                yield f"[A-Za-z0-9]{{{size}}}"
            elif type_ == "n":
                yield f"[0-9]{{{size}}}"

    @property
    def bban_regex(self) -> str:
        regex = "".join(list(self.bban_format_to_regex))
        return f"^{regex}$"

    @property
    def inverted_iban(self) -> str:
        return self.bban + self.header

    @property
    def iban_in_numbers(self) -> int:
        return int("".join(IBAN_CHAR_TO_NUM[char] for char in self.inverted_iban))

    @property
    def mod_97(self) -> int:
        return self.iban_in_numbers % 97

    @property
    def size(self) -> int:
        return len(self.iban)

    def is_mod_97(self) -> bool:
        return self.mod_97 == 1

    def is_iban_size_valid(self) -> bool:
        return self.size == self.country_specific_iban_size

    def is_alphanumeric(self) -> bool:
        return self.iban.isalnum()

    def matches_country_specific_format(self) -> bool:
        return True if re.match(self.bban_regex, self.bban) else False
