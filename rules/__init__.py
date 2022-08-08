from rules_engine import Otherwise, Rule, RulesEngine

from rules.actions import (raise_mod_97_check_error,
                           raise_not_alpha_numeric_error)
from rules.conditions import mod_97_not_eq_to_one, not_alpha_numeric


def iban(iban: str) -> bool | None:
    RulesEngine(
        Rule(not_alpha_numeric, raise_not_alpha_numeric_error),
        Rule(mod_97_not_eq_to_one, raise_mod_97_check_error),
        Otherwise(True),
    ).run(iban)
