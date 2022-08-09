from rules_engine import Otherwise, Rule, RulesEngine, not_, then

from app.models import IbanModel
from app.rules.actions import (
    raise_iban_does_not_match_country_format_error,
    raise_iban_length_does_not_match_country_length_error,
    raise_mod_97_check_error, raise_not_alpha_numeric_error)
from app.rules.conditions import (alpha_numeric, matches_country_format,
                                  matches_country_specific_length, mod_97)


def iban(iban: IbanModel) -> bool:
    return RulesEngine(
        Rule(not_(alpha_numeric), raise_not_alpha_numeric_error),
        Rule(
            not_(matches_country_specific_length),
            raise_iban_length_does_not_match_country_length_error,
        ),
        Rule(
            not_(matches_country_format),
            raise_iban_does_not_match_country_format_error,
        ),
        Rule(not_(mod_97), raise_mod_97_check_error),
        Otherwise(then(True)),
    ).run(iban)
