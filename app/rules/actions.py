from app.exceptions import Mod97CheckError, NotAlphaNumericError, IbanLengthError


def raise_not_alpha_numeric_error(iban):
    raise NotAlphaNumericError(iban)


def raise_mod_97_check_error(iban):
    raise Mod97CheckError(iban)


def raise_iban_length_does_not_match_country_length_error(iban):
    raise IbanLengthError(iban, "IBAN length is not valid for the specified country")
