from typing import Optional
from pydantic import ConfigDict
from models.base_model import MyBaseModel

class UserTestData(MyBaseModel):
    user_id: int
    expected_name: str

class Geo(MyBaseModel):
    lat: str
    lng: str

class Address(MyBaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo

class Company(MyBaseModel):
    name: str
    catchPhrase: str
    bs: str

class User(MyBaseModel):
    # Ignore fields we haven't defined
    model_config = ConfigDict(extra='ignore')

    id: int
    name: str
    username: str
    email: str
    # Use Optional or | None to tell Pydantic these are not mandatory
    address: Optional[dict] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    company: Optional[dict] = None
