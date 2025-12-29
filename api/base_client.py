import requests
import logging

class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        self.logger = logging.getLogger(__name__)

    def _request(self, method, endpoint, **kwargs):
        # Safely join base_url and endpoint
        # Example: "http://api.com/" + "/users" -> "http://api.com/users"
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

        self.logger.info(f"Sending {method} to {url}")
        response = self.session.request(method, url, **kwargs)

        # English comment: Log response status for Allure visibility
        self.logger.info(f"Response Status: {response.status_code}")
        return response

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
