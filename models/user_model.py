from models.base_model import MyBaseModel

# Това е за данните, които ЧЕТЕМ от нашия JSON
class UserTestData(MyBaseModel):
    user_id: int
    expected_name: str

# Това са вложените модели за ОТГОВОРА от API-то
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

# Това е основният модел за ОТГОВОРА от API-то
class UserResponseModel(MyBaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company
