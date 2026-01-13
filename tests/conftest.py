import pytest
from utils.api_client import PaymentClient

@pytest.fixture
def payment_client():
    # IMPORTANT: use mock base URL, not real one
    return PaymentClient(base_url="https://mock-gateway")

