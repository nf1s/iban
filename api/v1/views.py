from functools import lru_cache
from http import HTTPStatus

from fastapi import APIRouter

from api.v1 import schemas
from app import controllers

router = APIRouter(prefix="/api/v1")


@lru_cache(maxsize=100)
@router.post(
    "/iban",
    response_model=schemas.Response,
    status_code=HTTPStatus.OK,
    responses={422: {"model": schemas.Response}},
)
def validate_iban(payload: schemas.Payload):
    message = {
        "description": "IBAN Validation",
        "content": {
            "iban": payload.iban,
            "valid": controllers.validate_iban(payload.iban),
            "message": "IBAN validation was successful",
        },
    }
    return message
