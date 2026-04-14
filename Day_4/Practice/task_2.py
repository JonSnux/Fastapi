# На вход подается словарь user_data и словарь user_data2. 
# Напишите модель Pydantic для этих словарей, учитывая, что поле age необязательное. 
# Сериализуйте оба словаря.

from pydantic import BaseModel

user_data = {"id": 1, "name": "Иван", "email": "ivan@example.com", "age": 30}
user_data2 = {"id": 2, "name": "Петр", "email": "petr@example.com"}


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None


user_1 = User(**user_data)
user_1_json = user_1.model_dump_json(indent=4)
print(user_1_json)

user_2 = User(**user_data2)
user_2_json = user_2.model_dump_json(indent=4)
print(user_2_json)