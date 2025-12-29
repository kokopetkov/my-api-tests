import pytest
from utils.file_reader import read_json_resource
from models.user_model import UserResponseModel, UserTestData

users_list = read_json_resource("data", "users_data.json", UserTestData)
user_ids = [user.expected_name for user in users_list]

@pytest.mark.parametrize("user", users_list, ids=user_ids)
def test_user_names(user_client, user: UserTestData):

    response = user_client.get_user(user.user_id)
    assert response.status_code == 200

    api_data = UserResponseModel(**response.json())

    assert api_data.name == user.expected_name
    print(f"Validated user: {api_data.username} with email {api_data.email}")

def test_get_all_users_status_code(user_client):
    response = user_client.get_all_users()
    assert response.status_code == 200

def test_user_data_contains_id(user_client):
    response = user_client.get_user(1)
    data = response.json()
    assert data["id"] == 1

def test_get_user_by_id(user_client):
    # Now user_client comes directly from conftest.py
    response = user_client.get_user(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_create_user(user_client, sample_user_data):
    # Using two fixtures at once
    response = user_client.create_user(sample_user_data)
    assert response.status_code == 201

def test_delete_functionality(user_client, temp_user):
    # We use the user created by the fixture
    user_id = temp_user["id"]

    # We can manually delete it or just let the fixture handle it
    response = user_client.delete_user(user_id)
    assert response.status_code in [200, 202, 204]
