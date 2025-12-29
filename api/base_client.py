import requests
import logging

# English comments as requested
class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        self.logger = logging.getLogger(__name__)

    def _request(self, method, endpoint, **kwargs):
        # Ensure exactly one slash between base_url and endpoint
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

        # English comment: Log the final URL to verify it's correct
        print(f"\nDEBUG: {method} {url}")

        response = self.session.request(method, url, **kwargs)

        if not response.ok:
            # English comment: Log body only on failure to keep logs clean
            print(f"DEBUG: Response body: {response.text}")

        return response

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
