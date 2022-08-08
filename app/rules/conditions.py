from app.utils import (convert_iban_to_num, mod_97,
                       move_the_1st_4_char_to_the_end)


def not_alpha_numeric(iban: str) -> bool:
    return not iban.isalnum()


def mod_97_not_eq_to_one(iban: str) -> bool:
    inverted_iban = move_the_1st_4_char_to_the_end(iban)
    iban_num = convert_iban_to_num(inverted_iban)
    return mod_97(iban_num) != 1
