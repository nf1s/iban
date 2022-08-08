from http import HTTPStatus

from fastapi import APIRouter

from api.v1 import schemas
from app import controllers

router = APIRouter(prefix="/api/v1")


@router.post(
    "/iban", response_model=schemas.IbanCheckResponse, status_code=HTTPStatus.OK
)
def validate_iban(payload: schemas.Payload):
    message = {
        "description": "Validate IBAN",
        "content": {
            "iban": payload.iban,
            "valid": controllers.validate_iban(payload.iban),
        },
    }
    return message
