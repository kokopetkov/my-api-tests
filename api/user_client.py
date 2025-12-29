import logging
import os
import requests

from api.base_client import BaseClient

logger = logging.getLogger(__name__)

class UserClient(BaseClient):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/users"

    def get_users(self):
        # Pass the endpoint to the parent get method
        return self.get(self.endpoint)

    def create_user(self, payload):
        # Pass the endpoint here! This was missing.
        return self.post(self.endpoint, json=payload)

    def get_user(self, user_id):
        # Combine endpoint and ID
        return self.get(f"{self.endpoint}/{user_id}")

    def delete_user(self, user_id):
        return self.delete(f"{self.endpoint}/{user_id}")
