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


def test_iban_endpoint_returns_error_response_when_called_with_iban_is_gt_34(
    api_client,
):
    iban = "GB82 WEST 1234 5698 7654 321 12312312346512341231412341241"
    response = api_client.post("/api/v1/iban", json=dict(iban=iban))
    response.status_code = 422
    assert response.json() == {
        "description": "IBAN Validation",
        "content": {
            "iban": "GB82WEST12345698765432112312312346512341231412341241",
            "valid": False,
            "message": "IBAN length=52, IBAN length cannot be greater than 34 characters",
        },
    }


def test_iban_endpoint_returns_error_response_when_called_with_iban_is_lt_15(
    api_client,
):
    iban = "GB82"
    response = api_client.post("/api/v1/iban", json=dict(iban=iban))
    response.status_code = 422
    assert response.json() == {
        "description": "IBAN Validation",
        "content": {
            "iban": "GB82",
            "valid": False,
            "message": "IBAN length cannot be less than 15 characters",
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


def test_iban_endpoint_returns_error_response_when_called_with_non_alphanumeric_iban(
    api_client,
):
    iban = "GB82 WEST 1234 5698 7654 32&"
    response = api_client.post("/api/v1/iban", json=dict(iban=iban))
    response.status_code = 422
    assert response.json() == {
        "description": "IBAN Validation",
        "content": {
            "iban": "GB82WEST12345698765432&",
            "valid": False,
            "message": "The IBAN can contain only characters A-Z and 0-9",
        },
    }


def test_iban_endpoint_returns_error_response_when_called_with_iban_invalid_country_format(
    api_client,
):
    iban = "BI00 a234 5678 9123"
    response = api_client.post("/api/v1/iban", json=dict(iban=iban))
    response.status_code = 422
    assert response.json() == {
        "description": "IBAN Validation",
        "content": {
            "iban": "BI00a23456789123",
            "valid": False,
            "message": "IBAN format is not valid for the specified country, country=Burundi, format=BIkk nnnn nnnn nnnn",
        },
    }


def test_iban_endpoint_returns_error_response_when_called_with_iban_invalid_mod_97_operation(
    api_client,
):
    iban = "BI00 1234 5678 9123"
    response = api_client.post("/api/v1/iban", json=dict(iban=iban))
    response.status_code = 422
    assert response.json() == {
        "description": "IBAN Validation",
        "content": {
            "iban": "BI00123456789123",
            "valid": False,
            "message": "mod-97 operation as described in ISO 7064 has failed to validate the IBAN",
        },
    }
