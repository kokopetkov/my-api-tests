import pytest
import os
from api.user_client import UserClient

@pytest.fixture(scope="session")
def user_client():
    client = UserClient()
    print("\n--- Starting API Session ---")
    yield client
    print("\n--- Closing API Session ---")

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
    # SETUP: Create a user before the test
    user_payload = {
        "name": "Cleanup Test",
        "username": "cleanup_user",
        "email": "cleanup@example.com"
    }

    response = user_client.create_user(user_payload)
    if response.status_code != 201:
        pytest.fail(
            f"Fixture Setup Failed: Could not create user. Status: {response.status_code}")

    user_data = response.json()
    user_id = user_data["id"]

    yield user_data  # The test runs here

    # TEARDOWN: Delete the user after the test is finished
    delete_response = user_client.delete_user(user_id)

    if delete_response.status_code == 200 or delete_response.status_code == 204:
        print(f"\nSuccessfully cleaned up user with ID: {user_id}")
    else:
        print(
            f"\nFailed to cleanup user {user_id}. Status: {delete_response.status_code}")
