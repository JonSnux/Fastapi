from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip: str


class Order(BaseModel):
    order_id: int
    items: list[str]


class User(BaseModel):
    user_id: int
    username: str
    address: Address
    orders: list[Order]


user_data = {
    "user_id": 2,
    "username": "John",
    "address": {
        "street": "Main str.",
        "city": "Anytown",
        "zip": "12345"
    },
    "orders": [
        {"order_id": 1, "items": ["item1", "item2"]},
        {"order_id": 2, "items": ["item3"]}
    ]
}

user = User(**user_data)
user_json = user.model_dump_json(indent=4)
print(user_json)