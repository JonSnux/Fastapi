# На вход подается словарь user_data. 
# Напишите модель Pydantic для этого словаря, сериализуйте словарь в JSON и десериализуйте JSON обратно в экземпляр модели.

from pydantic import BaseModel

user_data = {"id": 1, "name": "Иван", "email": "ivan@example.com"}

class User(BaseModel):
    id: int
    name: str
    email: str


new_user = User(**user_data)
print(new_user)
new_user_json = new_user.model_dump_json(indent=4) #Сериализовали в JSON
print(new_user_json)

user = User.model_validate_json(new_user_json) #Десериализовали обратно
print(user)
print(user.email)