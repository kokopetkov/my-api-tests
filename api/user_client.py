from api.base_client import BaseClient
from models.user_model import User

class UserClient(BaseClient):
    """
    Client for interacting with the /users endpoint.
    Inherits technical HTTP logic from BaseClient.
    """

    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/users"

    def get_users(self):
        return self.get(self.endpoint)

    def get_user(self, user_id):
        """
        Fetches a user and automatically validates the response using Pydantic.
        """
        response = self.get(f"{self.endpoint}/{user_id}")

        # English comment: If the request was successful, parse it into the User model
        response.raise_for_status()
        return User(**response.json())

    def create_user(self, payload):
        """
        Creates a user and returns the validated User object.
        """
        response = self.post(self.endpoint, json=payload)

        if response.status_code == 201:
            return User(**response.json())

        return response

    def delete_user(self, user_id):
        return self.delete(f"{self.endpoint}/{user_id}")
