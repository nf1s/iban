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


def test_iban_endpoint_returns_error_response_when_called_with_iban_with_size_gt_required_size(
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
            "message": "IBAN length is not valid for the specified country, country=United Kingdom, size=23, required_size=22",
        },
    }


def test_iban_endpoint_returns_error_response_when_called_with_iban_with_size_lt_required_size(
    api_client,
):
    iban = "GB82 WEST 1234 5698 7654 3"
    response = api_client.post("/api/v1/iban", json=dict(iban=iban))
    response.status_code = 422
    assert response.json() == {
        "description": "IBAN Validation",
        "content": {
            "iban": trim(iban),
            "valid": False,
            "message": "IBAN length is not valid for the specified country, country=United Kingdom, size=21, required_size=22",
        },
    }


def test_iban_endpoint_returns_error_response_when_called_with_invalid_country_code(
    api_client,
):
    iban = "HM91100000000123456789"
    response = api_client.post("/api/v1/iban", json=dict(iban=iban))
    response.status_code = 422

    assert response.json() == {
        "description": "IBAN Validation",
        "content": {
            "iban": "HM91100000000123456789",
            "valid": False,
            "message": "Country code HM is invalid",
        },
    }
