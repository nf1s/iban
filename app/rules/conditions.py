from app.utils import (convert_iban_to_num, get_bban, get_country_code,
                       get_country_specific_format, mod_97,
                       move_the_1st_4_char_to_the_end)


def iban_does_not_match_country_specific_length(iban: str) -> bool:
    country_code = get_country_code(iban)
    country = get_country_specific_format(country_code)
    return len(iban) != int(country["size"])


def not_alpha_numeric(iban: str) -> bool:
    return not iban.isalnum()


def mod_97_not_eq_to_one(iban: str) -> bool:
    inverted_iban = move_the_1st_4_char_to_the_end(iban)
    iban_num = convert_iban_to_num(inverted_iban)
    return mod_97(iban_num) != 1
