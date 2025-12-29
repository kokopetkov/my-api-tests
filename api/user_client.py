import logging
import os
import requests

logger = logging.getLogger(__name__)

class UserClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL", "https://localhost") + "/users"

    def get_all_users(self):
        return requests.get(self.base_url)

    def get_user(self, user_id):
        url = f"{self.base_url}/{user_id}"
        logger.info(f"Sending GET request to: {url}")

        response = requests.get(url)

        logger.info(f"Response received: Status {response.status_code}")

        return response

    def create_user(self, payload):
        url = f"{self.base_url}"
        # This will show in console with 'pytest -s'
        print(f"\nDEBUG: Sending POST to {url}")
        return requests.post(url, json=payload)

    def delete_user(self, user_id):
        # Delete a user by their unique ID
        url = f"{self.base_url.rstrip('/')}/{user_id}"
        return requests.delete(url)
