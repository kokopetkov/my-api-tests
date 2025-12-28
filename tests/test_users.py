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
