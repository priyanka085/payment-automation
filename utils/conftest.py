import pytest
from utils.api_client import PaymentClient

@pytest.fixture(scope="session")
def base_url():
    return "https://api.mockpayment.com"

@pytest.fixture(scope="session")
def payment_client(base_url):
    return PaymentClient(base_url)

