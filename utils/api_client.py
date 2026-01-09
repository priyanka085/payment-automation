import request

class PaymentClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def authorize_payment(self, payload, headers):
        return request.post(
            f"{self.base_url}/authorize",
            json=payload,
            headers=headers
        )
