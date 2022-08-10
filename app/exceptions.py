from app.models import IbanModel


class BaseException(Exception):
    message: str
    iban: IbanModel

    def __init__(self, iban, message=None, **kwargs):
        super().__init__(iban or self.iban, message or self.message)
        self.kwargs = kwargs


class CountryDoesNotExist(BaseException):
    message = "IBAN is invalid since the country does not exist"


class IbanLengthError(BaseException):
    message = "IBAN length is Invalid"


class NotAlphaNumericError(BaseException):
    message = "The IBAN can contain only characters A-Z and 0-9"


class Mod97CheckError(BaseException):
    message = "mod-97 operation as described in ISO 7064 has failed to validate the IBAN"


class IbanDoesNotMatchCountryFormatError(BaseException):
    message = "IBAN Does not match corresponding country format"
