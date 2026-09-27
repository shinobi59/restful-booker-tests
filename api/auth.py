from api.client import ApiClient


class AuthApi:
    def __init__(self, client: ApiClient):
        self.client = client

    def get_token(self, username="admin", password="password123"):
        payload = {"username": username, "password": password}
        response = self.client.post("/auth", json=payload)
        if response.status_code == 200:
            return response.json().get("token")
        return None

    def get_headers(self, token):
        return {"Cookie": f"token={token}"}