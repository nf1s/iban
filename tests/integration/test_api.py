from app.utils import trim


def test_iban_endpoint_returns_success_response_when_called_with_valid_ibans(
    api_client, valid_ibans
):
    for iban in valid_ibans:
        response = api_client.post("/api/v1/iban", json=dict(iban=iban))
        response.status_code = 200
        assert response.json() == {
            "description": "IBAN Validation",
            "content": {
                "iban": trim(iban),
                "valid": True,
                "message": "IBAN validation was successful",
            },
        }


def test_iban_endpoint_returns_error_response_when_called_with_invalid_ibans(
    api_client,
):
    iban = "GB82 WEST 1234 5698 7654 321"
    response = api_client.post("/api/v1/iban", json=dict(iban=iban))
    response.status_code = 422
    assert response.json() == {
        "description": "IBAN Validation",
        "content": {
            "iban": trim(iban),
            "valid": False,
            "message": "IBAN length is not valid for the specified country",
        },
    }