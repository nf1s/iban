from app import rules
from app.models import IbanModel


def validate_iban(iban):
    return rules.iban(IbanModel(iban))
