from app.models import IbanModel


def matches_country_specific_length(iban: IbanModel) -> bool:
    """Function checks if IBAN length is equal to country specific length

    Args:
        iban (IbanModel): iban

    Returns:
        bool: True if the IBAN length matches country specific length else False
    """
    return iban.is_iban_size_valid()


def alpha_numeric(iban: IbanModel) -> bool:
    """Function checks if IBAN is alpha-numeric

    Args:
        iban (IbanModel): iban

    Returns:
        bool: True if alphanumeric else False
    """
    return iban.is_alphanumeric()


def mod_97(iban: IbanModel) -> bool:
    """Function checks if IBAN mod 97 is equal to 1

    Args:
        iban (IbanModel): iban

    Returns:
        bool: True if IBAN mod 97 is equal to 1
    """
    return iban.is_mod_97()


def matches_country_format(iban: IbanModel) -> bool:
    """Function checks if IBAN matches its corresponding country format

    Args:
        iban (IbanModel): iban

    Returns:
        bool: True if IBAN matches corresponding country format
    """
    return iban.matches_country_specific_format()
