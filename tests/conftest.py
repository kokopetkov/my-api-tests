import pytest
import os
from api.user_client import UserClient

@pytest.fixture(scope="session")
def user_client():
    base_url = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    client = UserClient(base_url=base_url)
    return client

@pytest.fixture
def sample_user_data():
    """
    Provide a static dictionary representing a valid user for POST/PUT requests.
    """
    return {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }

@pytest.fixture
def temp_user(user_client):
    user_payload = {
        "name": "Cleanup Test",
        "username": "cleanup_user",
        "email": "cleanup@example.com"
    }

    # This now returns a User object, not a Response!
    user = user_client.create_user(user_payload)

    yield user  # The test runs here

    user_client.delete_user(user.id)
