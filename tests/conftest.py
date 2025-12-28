import pytest
from api.user_client import UserClient


@pytest.fixture
def user_client():
    return UserClient()
