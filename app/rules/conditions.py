from app.models import IbanModel


def iban_does_not_match_country_specific_length(iban: IbanModel) -> bool:
    return not iban.is_iban_size_valid()


def not_alpha_numeric(iban: IbanModel) -> bool:
    return not iban.is_alphanumeric()


def mod_97_not_eq_to_one(iban: IbanModel) -> bool:
    return not iban.is_mod_97()


def iban_does_not_match_country_format(iban: IbanModel) -> bool:
    return not iban.matches_country_specific_format()
