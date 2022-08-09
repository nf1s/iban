from functools import lru_cache

from app import rules
from app.models import IbanModel


@lru_cache(maxsize=100)
def validate_iban(iban) -> bool:
    """Method handles IBAN Rules

    Args:
        iban (str): iban

    Returns:
        bool: True when IBAN is valid

    Raises:
        NotAlphaNumericError: when IBAN is not alphanumeric
        Mod97CheckError: when mod 97 is not equal to 1
        IbanLengthError: When Iban does not match country specific length
        IbanDoesNotMatchCountryFormatError: when IBAN format does not match the country
    """
    return rules.iban(IbanModel(iban))
