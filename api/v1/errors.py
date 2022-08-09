from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import (CountryDoesNotExist, IbanLengthError,
                            Mod97CheckError, NotAlphaNumericError)


def error_response(exc):
    iban, message = exc.args
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={
            "description": "IBAN Validation",
            "content": {
                "iban": str(iban),
                "valid": False,
                "message": message,
            },
        },
    )


def register_errors(app):
    @app.exception_handler(ValueError)
    def value_error_exception_handler(request: Request, exc: ValueError):
        return error_response(exc)

    @app.exception_handler(CountryDoesNotExist)
    def country_does_not_exist_exception_handler(
        request: Request, exc: CountryDoesNotExist
    ):
        return error_response(exc)

    @app.exception_handler(Mod97CheckError)
    def mod_97_exception_handler(request: Request, exc: Mod97CheckError):
        return error_response(exc)

    @app.exception_handler(IbanLengthError)
    def iban_length_exception_handler(request: Request, exc: IbanLengthError):
        return error_response(exc)

    @app.exception_handler(IbanLengthError)
    def not_alpha_numeric_exception_handler(
        request: Request, exc: NotAlphaNumericError
    ):
        return error_response(exc)
