from app.exceptions import Mod97CheckError, NotAlphaNumericError


def raise_not_alpha_numeric_error(iban):
    raise NotAlphaNumericError(iban)


def raise_mod_97_check_error(iban):
    raise Mod97CheckError(iban)
