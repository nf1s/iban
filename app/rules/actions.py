from app.exceptions import (
    IbanDoesNotMatchCountryFormatError,
    IbanLengthError,
    Mod97CheckError,
    NotAlphaNumericError,
)
from app.models import IbanModel


def raise_not_alpha_numeric_error(iban: IbanModel):
    """Function is called when IBAN is not alpha-numeric.

    Args:
        iban (IbanModel): iban

    Raises:
        NotAlphaNumericError: when IBAN is not alphanumeric
    """
    raise NotAlphaNumericError(iban)


def raise_mod_97_check_error(iban: IbanModel):
    """Function is called when IBAN mod 97 operation is not equal to 1.

    Args:
        iban (IbanModel): iban

    Raises:
        Mod97CheckError: when mod 97 is not equal to 1
    """
    raise Mod97CheckError(iban)


def raise_iban_length_does_not_match_country_length_error(iban: IbanModel):
    """Function is called when IBAN length does not match country specific length.

    Args:
        iban (IbanModel): iban

    Raises:
        IbanLengthError: When Iban does not match country specific length
    """
    raise IbanLengthError(
        iban,
        "IBAN length is not valid for the specified country, "
        f"country={iban.country}, size={iban.size}, "
        f"required_size={iban.country_specific_iban_size}",
    )


def raise_iban_does_not_match_country_format_error(iban: IbanModel):
    """Method is called when IBAN format does not match the country.

    Args:
        iban (IbanModel): iban

    Raises:
        IbanDoesNotMatchCountryFormatError: when IBAN format does not match the country
    """
    raise IbanDoesNotMatchCountryFormatError(
        iban,
        "IBAN format is not valid for the specified country, "
        f"country={iban.country}, format={iban.iban_format}",
    )
