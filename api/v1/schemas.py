from pydantic import BaseModel, Field, validator

from app.exceptions import IbanLengthError
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
            raise IbanLengthError(
                iban, "IBAN length cannot be greater than 34 characters"
            )
        if len(iban) < 15:
            raise IbanLengthError(iban, "IBAN length cannot be less than 15 characters")
        return iban
