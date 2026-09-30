from api.client import ApiClient


class BookingApi:
    def __init__(self, client, auth):
        self.client = client
        self.auth = auth

    def get_booking_ids(self, params=None):
        response = self.client.get("/booking", params=params)
        return response.json()

    def get_booking(self, booking_id):
        response = self.client.get(f"/booking/{booking_id}")
        return response.json()

    def create_booking(self, booking_data):
        response = self.client.post("/booking", json=booking_data)
        return response.json()

    def update_booking(self, booking_id, booking_data, token):
        headers = self.auth.get_headers(token)
        response = self.client.put(f"/booking/{booking_id}", json=booking_data, headers=headers)
        return response.json()

    def partial_update_booking(self, booking_id, booking_data, token):
        headers = self.auth.get_headers(token)
        response = self.client.patch(f"/booking/{booking_id}", json=booking_data, headers=headers)
        return response.json()

    def delete_booking(self, booking_id, token):
        headers = self.auth.get_headers(token)
        response = self.client.delete(f"/booking/{booking_id}", headers=headers)
        return response.status_code

    def get_booking_response(self, booking_id):
        response = self.client.get(f"/booking/{booking_id}")
        return response