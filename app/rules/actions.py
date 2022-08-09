from app.exceptions import (IbanDoesNotMatchCountryFormatError,
                            IbanLengthError, Mod97CheckError,
                            NotAlphaNumericError)
from app.models import IbanModel


def raise_not_alpha_numeric_error(iban: IbanModel):
    raise NotAlphaNumericError(iban)


def raise_mod_97_check_error(iban: IbanModel):
    raise Mod97CheckError(iban)


def raise_iban_length_does_not_match_country_length_error(iban: IbanModel):
    raise IbanLengthError(
        iban,
        "IBAN length is not valid for the specified country, "
        f"country={iban.country}, size={iban.size}, "
        f"required_size={iban.country_specific_iban_size}",
    )


def raise_iban_does_not_match_country_format_error(iban: IbanModel):
    raise IbanDoesNotMatchCountryFormatError(
        iban,
        "IBAN format is not valid for the specified country, "
        f"country={iban.country}, format={iban.iban_format}",
    )
