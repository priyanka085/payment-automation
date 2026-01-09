import pytest
from utils.test_data import VALID_PAYMENT

@pytest.mark.smoke
def test_payment_authorization_success(payment_client):
    response = payment_client.authorize_payment(
        payload=VALID_PAYMENT,
        headers={"Content-Type": "application/json"}
    )
