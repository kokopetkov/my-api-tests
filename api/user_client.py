from api.base_client import BaseClient

class UserClient(BaseClient):
    """
    Client for interacting with the /users endpoint.
    Inherits technical HTTP logic from BaseClient.
    """

    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/users"

    def get_users(self):
        # Must pass self.endpoint to the parent get method
        return self.get(self.endpoint)

    def create_user(self, payload):
        # Payload goes into 'json' argument of requests
        return self.post(self.endpoint, json=payload)

    def get_user(self, user_id):
        # Combine the base endpoint with the specific user ID
        return self.get(f"{self.endpoint}/{user_id}")

    def delete_user(self, user_id):
        return self.delete(f"{self.endpoint}/{user_id}")
