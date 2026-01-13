import pytest
import responses
from utils.test_data import *

@responses.activate
@pytest.mark.smoke
def test_payment_authorization_success(payment_client):

    responses.add(
        responses.POST,
        "https://mock-gateway/authorize",  # MUST MATCH EXACTLY
        json={
            "status": "APPROVED",
            "transactionId": "TXN123",
            "amount": 100,
            "currency": "USD"
        },
        status=200
    )

    response = payment_client.authorize_payment(
        payload=VALID_PAYMENT,
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "APPROVED"

def test_payment_authorization_failure(payment_client):
    responses.add(
        responses.POST,
        "https://mock-gateway/authorize",
        json={
            "status": "REJECTED",
            "transaction id": "TXN124",
            "amount": 100,
            "currency": "USD"
        },
        status=422
    )
    response = payment_client.authorize_payment(
        payload=INVALID_PAYMENT,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422
    assert response.json()["status"]=="REJECTED"