from rules_engine import Otherwise, Rule, RulesEngine, then

from app.rules.actions import (
    raise_mod_97_check_error,
    raise_not_alpha_numeric_error,
    raise_iban_length_does_not_match_country_length_error,
    raise_iban_does_not_match_country_format_error,
)

from app.rules.conditions import (
    mod_97_not_eq_to_one,
    not_alpha_numeric,
    iban_does_not_match_country_specific_length,
    iban_does_not_match_country_format,
)


def iban(iban: str) -> bool:
    return RulesEngine(
        Rule(not_alpha_numeric, raise_not_alpha_numeric_error),
        Rule(
            iban_does_not_match_country_specific_length,
            raise_iban_length_does_not_match_country_length_error,
        ),
        Rule(mod_97_not_eq_to_one, raise_mod_97_check_error),
        Rule(
            iban_does_not_match_country_format,
            raise_iban_does_not_match_country_format_error,
        ),
        Otherwise(then(True)),
    ).run(iban)
