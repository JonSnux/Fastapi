# На вход подается список словарей users_data. 
# Напишите модель Pydantic для этих словарей и десериализуйте список словарей в список экземпляров модели.

from pydantic import BaseModel

users_data = [
    {"id": 1, "name": "Иван", "email": "ivan@example.com"},
    {"id": 2, "name": "Петр", "email": "petr@example.com"}
]


class User(BaseModel):
    id: int
    name: str
    email: str

user_list = [User(**user) for user in users_data]

print(user_list)

