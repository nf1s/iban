from app.models import IbanModel


def test_iban_model_properties_evaluated_correctly():
    iban = IbanModel("DE91 1000 0000 0123 4567 89")
    assert iban.iban == "DE91100000000123456789"
    assert iban.country == "Germany"
    assert iban.country_code == "DE"
    assert iban.header == "DE91"
    assert iban.bban == "100000000123456789"
    assert iban.country_specific_info == {
        "country_code": "DE",
        "country": "Germany",
        "size": "22",
        "bban_format": "18n",
        "iban_format": "DEkk bbbb bbbb cccc cccc cc",
    }

    assert iban.country_specific_iban_size == 22
    assert iban.bban_format == "18n"
    assert iban.iban_format == "DEkk bbbb bbbb cccc cccc cc"
    assert iban.bban_regex == "^[0-9]{18}$"
    assert iban.inverted_iban == "100000000123456789DE91"
    assert iban.iban_in_numbers == 100000000123456789131491
    assert iban.mod_97 == 1
    assert iban.is_mod_97() is True
    assert iban.is_iban_size_valid() is True
    assert iban.is_alphanumeric() is True
    assert iban.matches_country_specific_format() is True
