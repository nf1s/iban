import pytest

from app import rules
from app.exceptions import (
    IbanDoesNotMatchCountryFormatError,
    IbanLengthError,
    Mod97CheckError,
    NotAlphaNumericError,
)


def test_iban_rules(valid_ibans):
    for iban in valid_ibans:
        assert rules.iban(iban) is True


def test_invalid_iban_raises_length_error():
    german_iban = "DE91100000000123456789"
    assert rules.iban(german_iban) is True

    invalid_german_iban = german_iban + "1"

    with pytest.raises(IbanLengthError):
        rules.iban(invalid_german_iban)

    invalid_german_iban = german_iban[:-1]

    with pytest.raises(IbanLengthError):
        rules.iban(invalid_german_iban)


def test_invalid_iban_raises_not_alpha_numeric_error():
    invalid_iban = "DE91100000000#23456@89"
    with pytest.raises(NotAlphaNumericError):
        rules.iban(invalid_iban)


def test_invalid_iban_raises_invalid_mod_97_operation_error():
    invalid_iban = "DE91T00000000123456789"
    with pytest.raises(IbanDoesNotMatchCountryFormatError):
        rules.iban(invalid_iban)


def test_invalid_iban_raises_invalid_country_format():
    invalid_iban = "DET1100000000123456789"
    with pytest.raises(Mod97CheckError):
        rules.iban(invalid_iban)
