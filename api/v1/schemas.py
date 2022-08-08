from pydantic import BaseModel


class Content(BaseModel):
    iban: str
    valid: bool


class IbanCheckResponse(BaseModel):

    description: str
    content: Content
