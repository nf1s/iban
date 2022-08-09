from pydantic import BaseModel, Field, validator

from app.consts import IBAN_FORMATS_PER_COUNTRY
from app.exceptions import CountryDoesNotExist
from app.utils import trim


class Content(BaseModel):
    iban: str
    valid: bool
    message: str


class Response(BaseModel):
    description: str
    content: Content


class Payload(BaseModel):
    iban: str = Field(
        default="GB82 WEST 1234 5698 7654 32",
        description="IBAN must be between 15 and 34 characters",
    )

    @validator("iban")
    def validate_iban(cls, iban):
        iban = trim(iban)
        if len(iban) > 34:
            raise ValueError(
                iban,
                f"IBAN length={len(iban)}, IBAN length cannot be greater than 34 characters",
            )
        if len(iban) < 15:
            raise ValueError(iban, "IBAN length cannot be less than 15 characters")

        country_code = iban[:2]
        try:
            IBAN_FORMATS_PER_COUNTRY[country_code.upper()]
        except KeyError:
            raise CountryDoesNotExist(iban, f"Country code {country_code} is invalid")
        return iban
