import pytest

from app import controllers
from app.exceptions import (
    IbanDoesNotMatchCountryFormatError,
    IbanLengthError,
    Mod97CheckError,
    NotAlphaNumericError,
)


def test_iban_controllers(valid_ibans):
    for iban in valid_ibans:
        assert controllers.validate_iban(iban) is True


def test_invalid_iban_raises_length_error():
    german_iban = "DE91100000000123456789"
    assert controllers.validate_iban(german_iban) is True

    invalid_german_iban = german_iban + "1"

    with pytest.raises(IbanLengthError):
        controllers.validate_iban(invalid_german_iban)

    invalid_german_iban = german_iban[:-1]

    with pytest.raises(IbanLengthError):
        controllers.validate_iban(invalid_german_iban)


def test_invalid_iban_raises_not_alpha_numeric_error():
    invalid_iban = "DE91100000000#23456@89"
    with pytest.raises(NotAlphaNumericError):
        controllers.validate_iban(invalid_iban)


def test_invalid_iban_raises_invalid_mod_97_operation_error():
    invalid_iban = "DE91T00000000123456789"
    with pytest.raises(IbanDoesNotMatchCountryFormatError):
        controllers.validate_iban(invalid_iban)


def test_invalid_iban_raises_invalid_country_format():
    invalid_iban = "DET1100000000123456789"
    with pytest.raises(Mod97CheckError):
        controllers.validate_iban(invalid_iban)
