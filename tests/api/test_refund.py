import pytest
import responses
from utils.test_data import *

@responses.activate
@pytest.mark.smoke
def test_successful_refund(payment_client):
    responses.add(
        responses.POST,
        "https://mock-gateway/refund",
        json={
            "status": "REFUNDED",
            "transactionId": "TXN123",
            "amount": 100,
            "currency": "USD"
        },
        status=200
    )
    response = payment_client.refund_payment(
        payload=VALID_REFUND,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "REFUNDED"
    assert response.json()["transactionId"] == "TXN123"
    assert response.json()["amount"] == 100

@responses.activate
@pytest.mark.smoke
def test_refund_exceeds_amount(payment_client):
    responses.add(
        responses.POST,
        "https://mock-gateway/refund",
        json={
            "status": "DECLINED",
            "reason": "REFUND_AMOUNT_EXCEEDS_TRANSACTION"
        },
        status=422
    )
    response = payment_client.refund_payment(
        payload=REFUND_EXCEEDS_AMOUNT,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422
    assert response.json()["status"] == "DECLINED"

