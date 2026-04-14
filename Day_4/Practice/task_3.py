# На вход подается словарь user_data. 
# Напишите модели Pydantic для этого словаря, учитывая вложенный адрес. 
# Сериализуйте и десериализуйте словарь.

from pydantic import BaseModel


user_data = {
    "id": 1,
    "name": "Иван",
    "email": "ivan@example.com",
    "address": {"street": "Тверская", "city": "Москва", "zip_code": "123456"}
}


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address


new_user = User(**user_data)
user_json = new_user.model_dump_json(indent=4) #Сериализовали
print(user_json)

user = User.model_validate_json(user_json) #Десериализовали
print(user)
print(user.address.city)