from pydantic import ValidationError
import pytest
from utils.file_reader import read_json_resource
from models.user_model import User, UserTestData

users_list = read_json_resource("data", "users_data.json", UserTestData)
user_ids = [user.expected_name for user in users_list]

@pytest.mark.parametrize("user_test_data", users_list, ids=user_ids)
def test_user_names(user_client, user_test_data):
    api_user = user_client.get_user(user_test_data.user_id)
    assert api_user.name == user_test_data.expected_name

def test_get_all_users_status_code(user_client):
    response = user_client.get_users()
    assert response.status_code == 200

def test_user_data_contains_id(user_client):
    user = user_client.get_user(1)
    assert user.id == 1

def test_get_user_by_id(user_client):
    user = user_client.get_user(1)
    assert user.id == 1
    assert user.name is not None
    assert isinstance(user.email, str)

def test_create_user(user_client, sample_user_data):
    user = user_client.create_user(sample_user_data)
    assert user.name == sample_user_data["name"]

def test_delete_functionality(user_client, temp_user):
    user_id = temp_user.id
    response = user_client.delete_user(user_id)
    assert response.status_code in [200, 202, 204]

def test_user_model_invalid_data():
    bad_data = {
        "id": "not-a-number",
        "name": "Test User",
        "email": "test@example.com"
    }

    with pytest.raises(ValidationError) as exc_info:
        UserTestData(**bad_data)

    assert "id" in str(exc_info.value)

def test_create_user_with_invalid_email(user_client):
    invalid_payload = {
        "name": "Wrong Email",
        "email": "this-is-not-an-email"
    }

    response = user_client.create_user(invalid_payload)

    assert response.status_code in [
        400, 422], f"Expected error code, got {response.status_code}"
