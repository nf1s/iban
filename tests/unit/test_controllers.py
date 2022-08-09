from app import controllers, utils


def test_iban_rules(valid_ibans):
    for iban in valid_ibans:
        assert controllers.validate_iban(utils.trim_iban(iban)) is True
