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
