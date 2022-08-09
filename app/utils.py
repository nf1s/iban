from app.consts import char_to_num


def convert_iban_to_num(iban: str) -> int:
    return int("".join(char_to_num[char] for char in iban))


def move_the_1st_4_char_to_the_end(iban: str) -> str:
    return iban[4:] + iban[:4]


def mod_97(num: int) -> int:
    return num % 97


def trim(string: str) -> str:
    return string.replace(" ", "")
