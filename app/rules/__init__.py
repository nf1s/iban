from rules_engine import Otherwise, Rule, RulesEngine, then

from app.rules.actions import (
    raise_iban_length_does_not_match_country_length_error,
    raise_mod_97_check_error, raise_not_alpha_numeric_error)
from app.rules.conditions import (iban_does_not_match_country_specific_length,
                                  mod_97_not_eq_to_one, not_alpha_numeric)


def iban(iban: str) -> bool:
    return RulesEngine(
        Rule(not_alpha_numeric, raise_not_alpha_numeric_error),
        Rule(
            iban_does_not_match_country_specific_length,
            raise_iban_length_does_not_match_country_length_error,
        ),
        Rule(mod_97_not_eq_to_one, raise_mod_97_check_error),
        Otherwise(then(True)),
    ).run(iban)
