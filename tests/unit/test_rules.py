from app import rules, utils


def test_iban_rules(valid_ibans):
    for iban in valid_ibans:
        assert rules.iban(utils.trim_iban(iban)) is True
