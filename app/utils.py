from app.consts import IBAN_CHAR_TO_NUM, IBAN_FORMATS_PER_COUNTRY


def convert_iban_to_num(iban: str) -> int:
    return int("".join(IBAN_CHAR_TO_NUM[char] for char in iban))


def move_the_1st_4_char_to_the_end(iban: str) -> str:
    return iban[4:] + iban[:4]


def mod_97(num: int) -> int:
    return num % 97


def trim(string: str) -> str:
    return string.replace(" ", "")


def get_country_specific_format(iban: str) -> dict:
    country_code = get_country_code(iban)
    return IBAN_FORMATS_PER_COUNTRY[country_code.upper()]


def get_country_code(iban: str) -> str:
    return iban[:2].upper()


def get_bban(iban: str) -> str:
    return iban[4:]


def bban_format_to_regex(bban_format):
    bban_format_list = bban_format.split("-")
    for bban_format in bban_format_list:
        type_ = bban_format[-1]
        size = bban_format[:-1]
        if type_ == "a":
            yield f"[A-Z]{{{size}}}"
        elif type_ == "c":
            yield f"[A-Za-z0-9]{{{size}}}"
        elif type_ == "n":
            yield f"[0-9]{{{size}}}"


def get_bban_regex(bban_format: str) -> str:
    regex = "".join(list(bban_format_to_regex(bban_format)))
    return f"^{regex}$"
