from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str | None = None

user_data = {'id': 123, 'name': 'Alice', 'email': 'alice@example.com'}

user = User(**user_data)

user_json = user.model_dump_json(indent=4)

print(user_json)

