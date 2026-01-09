import pytest
import responses
import json
from jsonschema import validate
from utils.test_data import VALID_PAYMENT

@pytest.mark.smoke
def test_payment_authorization_success(payment_client):
    response = payment_client.authorize_payment(
        payload=VALID_PAYMENT,
        headers={"Content-Type": "application/json"}
    )

@pytest.mark.smoke
def test_payment_authorization_approved(payment_client):
    responses.add(
        responses.POST,
        "https://mock-gateway/authorize",
        json={
            "status": "APPROVED",
            "transactionId": "TXN123456",
            "amount": 100,
            "currency": "USD"
        },
        status=200
    )

    payment_client.base_url = "https://mock-gateway"

    response = payment_client.authorize_payment(
        payload=VALID_PAYMENT,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "APPROVED"

def test_payment_schema_validation(payment_client):
    responses.add(
        responses.POST,
        "https://mock-gateway/authorize",
        json={
            "status": "APPROVED",
            "transactionId": "TX123",
            "amount": 100,
            "currency": "USD"
        },
        status=200
    )

    payment_client.base_url = "https://mock-gateway"

    response = payment_client.authorize_payment({}, {})

    with open("schemas/payment_response_schema.json") as f:
        schema = json.load(f)

    validate(instance=response.json(), schema=schema)